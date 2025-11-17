## README: `star_wars_api.py`

A command-line tool to explore data from the Star Wars universe using Star Wars API (SWAPI).

### Features
- Fetch data from various endpoints.
- User can choose which type of data to explore.
- Displays the names (or titles for films) of all entities retrieved.
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

1.  When prompted, enter the type of Star Wars data you want to explore. Available options are:
    - `people`
    - `planets`
    - `films`
    - `species`
    - `vehicles`
    - `starships`
2.  The script will connect to `swapi.info`, fetch the data, and print the names of all entities (use `title` for films).
3.  If an error occurs, an error message will be displayed.
4.  If no data is returned, it will print "Unable to download data".

