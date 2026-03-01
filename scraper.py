import requests
from bs4 import BeautifulSoup
import json

def fetch_data(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check for HTTP errors
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def parse_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    results = []

    # Example: Scraping all headlines from <h2> tags
    # Adjust the selector to match your target site
    items = soup.find_all('h2')
    
    for item in items:
        data_point = {
            "title": item.get_text(strip=True),
            "link": item.find('a')['href'] if item.find('a') else None
        }
        results.append(data_point)
    
    return results

def save_raw_data(data, filename="raw_data.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print(f"Successfully saved {len(data)} items to {filename}")

if __name__ == "__main__":
    TARGET_URL = "http://books.toscrape.com/"  
    html = fetch_data(TARGET_URL)
    
    if html:
        extracted_data = parse_html(html)
        save_raw_data(extracted_data)
