# Jason Isbell Concert Data - Claude Code Project

This project contains all the data and analysis tools for our 8 Jason Isbell concerts (2022-2025).

## 📁 Project Structure

```
claude-code-project/
├── concert_analysis.py      # Main analysis class
├── data/
│   └── setlists.csv         # Complete setlist data (154 songs)
├── notebooks/
│   └── concert_analysis.ipynb  # Jupyter notebook for exploration
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## 🚀 Quick Start with Claude Code

### 1. Open in your IDE
```bash
cd claude-code-project
code .  # or your preferred IDE
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Use with Claude Code

Ask Claude Code to:
- "Analyze which songs were played most frequently"
- "Create a visualization of songs per show over time"
- "Find all Drive-By Truckers covers"
- "Compare setlists between venues"
- "Identify the most unique show"
- "Create a heatmap of song appearances"
- "Generate statistics about cover songs"
- "Find patterns in encore songs"

## 📊 Available Data

The `JasonIsbellConcertData` class provides:
- `get_stats()` - Overall statistics
- `get_top_songs(n)` - Most played songs
- `get_show_setlist(date)` - Setlist for specific show
- `get_rare_songs()` - Songs played only once
- `get_venue_stats()` - Statistics by venue
- `find_song_appearances(song)` - Track specific songs
- `export_for_visualization()` - Export for viz tools

## 💡 Example Usage

```python
from concert_analysis import JasonIsbellConcertData

# Load data
concerts = JasonIsbellConcertData('data/setlists.csv')

# Get champion song
top_songs = concerts.get_top_songs(1)
print(f"Most played: {top_songs.iloc[0]['clean_song']}")

# Find a specific song
vampires = concerts.find_song_appearances("Vampires")
print(f"If We Were Vampires played at {len(vampires)} shows")

# Get rare songs
rare = concerts.get_rare_songs()
print(f"{len(rare)} songs were played only once")
```

## 🎯 Analysis Ideas

1. **Setlist Evolution**: How did setlists change over time?
2. **Venue Preferences**: Different songs for different venues?
3. **Cover Analysis**: Which artist's songs were covered most?
4. **Encore Patterns**: What songs typically closed shows?
5. **Rare Song Distribution**: Which shows had the most unique songs?
6. **Song Pairings**: Which songs were often played together?
7. **Show Length Trends**: Did shows get longer or shorter?
8. **Special Performances**: Analysis of dedications and special versions

## 📈 Visualization Suggestions

- Timeline of shows with song counts
- Heatmap of song appearances across shows
- Network graph of song relationships
- Chord diagram of venue-to-song connections
- Word cloud of most played songs
- Sankey diagram of setlist flow

## 🔗 Related Files

- **GitHub Repository**: Complete web infographic
- **Original Data**: From setlist.fm
- **Interactive Visualization**: index.html

---

Ready for Claude Code analysis! Just ask Claude to help you explore the data.
