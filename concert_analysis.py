"""
Jason Isbell Concert Data Analysis
===================================
This module provides tools to analyze our Jason Isbell concert history.
Perfect for use with Claude Code for further analysis and visualization.
"""

import pandas as pd
import json
from datetime import datetime
from typing import Dict, List, Tuple

class JasonIsbellConcertData:
    """Analyze Jason Isbell concert data from 8 shows (2022-2025)"""
    
    def __init__(self, csv_path: str = 'data/setlists.csv'):
        """Initialize with the concert data CSV"""
        self.df = pd.read_csv(csv_path)
        self.df['Date'] = pd.to_datetime(self.df['Date'])
        self._process_songs()
    
    def _process_songs(self):
        """Clean and process song names"""
        self.df['clean_song'] = self.df['Song'].str.replace(r'\(.*\)', '', regex=True).str.strip()
        self.df['is_cover'] = self.df['Song'].str.contains('cover', case=False, na=False)
        self.df['is_special'] = self.df['Song'].str.contains(
            'first time|dedicated|with Sadler|bluegrass', 
            case=False, na=False
        )
    
    def get_stats(self) -> Dict:
        """Get overall statistics"""
        return {
            'total_shows': self.df['Date'].nunique(),
            'total_songs': len(self.df),
            'unique_songs': self.df['clean_song'].nunique(),
            'total_venues': self.df['Venue'].nunique(),
            'date_range': {
                'first_show': self.df['Date'].min().strftime('%Y-%m-%d'),
                'last_show': self.df['Date'].max().strftime('%Y-%m-%d')
            },
            'covers': self.df['is_cover'].sum(),
            'special_performances': self.df['is_special'].sum()
        }
    
    def get_top_songs(self, n: int = 10) -> pd.DataFrame:
        """Get the most frequently played songs"""
        song_counts = self.df.groupby('clean_song').size().reset_index(name='play_count')
        song_counts['percentage'] = (song_counts['play_count'] / self.df['Date'].nunique() * 100).round(1)
        return song_counts.sort_values('play_count', ascending=False).head(n)
    
    def get_show_setlist(self, date: str) -> List[str]:
        """Get the setlist for a specific show"""
        show_df = self.df[self.df['Date'] == pd.to_datetime(date)]
        return show_df['Song'].tolist()
    
    def get_rare_songs(self) -> List[str]:
        """Get songs played only once"""
        song_counts = self.df.groupby('clean_song').size()
        rare_songs = song_counts[song_counts == 1].index.tolist()
        return self.df[self.df['clean_song'].isin(rare_songs)]['Song'].unique().tolist()
    
    def get_venue_stats(self) -> pd.DataFrame:
        """Get statistics by venue"""
        venue_stats = self.df.groupby('Venue').agg({
            'Date': 'nunique',
            'Song': 'count'
        }).rename(columns={'Date': 'shows', 'Song': 'total_songs'})
        venue_stats['avg_songs_per_show'] = (venue_stats['total_songs'] / venue_stats['shows']).round(1)
        return venue_stats.sort_values('shows', ascending=False)
    
    def find_song_appearances(self, song_name: str) -> pd.DataFrame:
        """Find all appearances of a specific song"""
        matches = self.df[self.df['clean_song'].str.contains(song_name, case=False, na=False)]
        return matches[['Date', 'Venue', 'Song']].sort_values('Date')
    
    def export_for_visualization(self) -> Dict:
        """Export data in a format ready for visualization tools"""
        return {
            'shows': [
                {
                    'date': date.strftime('%Y-%m-%d'),
                    'venue': self.df[self.df['Date'] == date]['Venue'].iloc[0],
                    'songs': self.df[self.df['Date'] == date]['Song'].tolist(),
                    'song_count': len(self.df[self.df['Date'] == date])
                }
                for date in self.df['Date'].unique()
            ],
            'song_frequency': self.get_top_songs(20).to_dict('records'),
            'venue_stats': self.get_venue_stats().to_dict('index'),
            'rare_songs': self.get_rare_songs(),
            'stats': self.get_stats()
        }


# Example usage for Claude Code
if __name__ == "__main__":
    # Initialize the data
    concerts = JasonIsbellConcertData()
    
    # Get overall stats
    stats = concerts.get_stats()
    print("Concert Journey Statistics:")
    print(f"- {stats['total_shows']} shows")
    print(f"- {stats['total_songs']} total songs")
    print(f"- {stats['unique_songs']} unique songs")
    
    # Get top songs
    print("\nTop 5 Most Played Songs:")
    top_songs = concerts.get_top_songs(5)
    for _, row in top_songs.iterrows():
        print(f"- {row['clean_song']}: {row['play_count']} shows ({row['percentage']}%)")
    
    # Export for visualization
    viz_data = concerts.export_for_visualization()
    
    # Save to JSON for other tools
    with open('concert_data.json', 'w') as f:
        json.dump(viz_data, f, indent=2, default=str)
    
    print("\nData exported to concert_data.json for visualization!")
