import requests
from bs4 import BeautifulSoup

def scrape_with_params(url, tag='h2', class_name=None):
    """
    Scrape elements from a webpage using user-defined parameters.
    :param url: Target URL
    :param tag: HTML tag to search for (e.g., 'h2', 'div')
    :param class_name: Optional class attribute to filter by
    """
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    if class_name:
        elements = soup.find_all(tag, class_=class_name)
    else:
        elements = soup.find_all(tag)

    if elements:
        print(f"Found {len(elements)} element(s):")
        for idx, el in enumerate(elements, 1):
            print(f"{idx}. {el.get_text(strip=True)}")
    else:
        print("No elements found.")

# Example usage
scrape_with_params("https://example.com", tag="h2", class_name="title")
