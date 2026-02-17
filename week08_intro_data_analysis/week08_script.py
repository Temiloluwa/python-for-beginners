
import requests
from bs4 import BeautifulSoup
import time

def fetch_page(url):
    """Fetches a page and returns the HTML text."""
    try:
        response = requests.get(url, timeout=20)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def extract_title(html):
    """Parses HTML and extracts the title."""
    if html is None:
        return None
    soup = BeautifulSoup(html, "html.parser")
    return soup.title.get_text(strip=True) if soup.title else "No Title"

def main():
    """Main execution function."""
    urls = [
        "https://www.mozilla.org/en-US/privacy/",
        "https://www.nist.gov/privacy-framework",
        "https://www.w3.org/",
    ]
    
    results = []
    print(f"Starting scrape of {len(urls)} pages...\n")

    for url in urls:
        print(f"Fetching: {url}")
        html = fetch_page(url)
        title = extract_title(html)
        
        results.append({
            "url": url,
            "title": title
        })
        # Polite delay
        time.sleep(1)

    print("\nResults:")
    for row in results:
        print(f"- {row['url']}: {row['title']}")

if __name__ == "__main__":
    main()
