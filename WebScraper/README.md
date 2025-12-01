
# Web Scraper

A flexible Python script to extract data from web pages using customizable parameters.

## Features

- Accepts user-defined HTML tag and class name
- Uses `requests` for HTTP fetching with error handling
- Parses HTML with `BeautifulSoup`
- Configurable via function parameters

## Prerequisites

- Python 3.6 or higher
- Install required packages:
```bash
pip install requests beautifulsoup4
```

## Usage

1. Save the script as `web_scraper.py`
2. Run:
```bash
python web_scraper.py
```

3. Modify the function call to scrape different elements:
```python
scrape_with_params("https://example.com", tag="h2", class_name="title")
```

Adjust the URL, tag, and class name to target your desired content.


