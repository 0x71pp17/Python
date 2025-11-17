## README: `star_wars_api.py`

A command-line tool to explore data from the Star Wars universe using the SWAPI (The Star Wars API).

### Features
- Fetch data from various SWAPI endpoints (e.g., people, planets, films).
- User can choose which type of data to explore.
- Displays the names of all entities retrieved from the chosen endpoint.
- Handles HTTP errors gracefully.

### Prerequisites
- **Python 3.6 or later**
- `requests` library

### Installation
```bash
pip install requests
```

### Usage
Run the script:
```bash
python star_wars_api.py
```

1.  When prompted, enter the type of Star Wars data you want to explore (e.g., `people`, `planets`, `films`, `starships`).
2.  The script will connect to the SWAPI, fetch the data, and print the names of all entities.
3.  If an error occurs (e.g., invalid endpoint, network issue), an error message will be displayed.
4.  If no data is returned, it will print "Unable to download data".

