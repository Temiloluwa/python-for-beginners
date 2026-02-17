
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def get_sitemap_urls(base_url: str) -> list[str]:
    """Attempts to fetch and parse a sitemap.xml."""
    sitemap_url = base_url.rstrip("/") + "/sitemap.xml"
    print(f"Checking {sitemap_url}...")
    
    try:
        r = requests.get(sitemap_url, timeout=10, headers={"User-Agent": "HF-PrivacyCrawler/0.1"})
        if r.status_code != 200:
            print(f"No sitemap found (Status {r.status_code})")
            return []
        
        soup = BeautifulSoup(r.text, "xml")
        urls = [loc.get_text(strip=True) for loc in soup.find_all("loc")]
        print(f"Found {len(urls)} URLs in sitemap.")
        return urls
    except Exception as e:
        print(f"Error fetching sitemap: {e}")
        return []

def filter_relevant_urls(urls: list[str], keywords: list[str]) -> list[str]:
    """Filters URLs that contain interesting keywords."""
    return [u for u in urls if any(k in u.lower() for k in keywords)]

def main():
    base = "https://www.mozilla.org"
    
    # 1. Crawl
    all_urls = get_sitemap_urls(base)
    
    # 2. Filter
    keywords = ["privacy", "legal", "terms", "security"]
    relevant = filter_relevant_urls(all_urls, keywords)
    
    print(f"\nRelevant URLs ({len(relevant)} found):")
    for u in relevant[:10]:
        print(f"- {u}")
        
    # 3. Simple Scraping Loop (Sample)
    print("\nSampling first 3 pages...")
    data = []
    for u in relevant[:3]:
        try:
            r = requests.get(u, timeout=10)
            soup = BeautifulSoup(r.text, "html.parser")
            title = soup.title.get_text(strip=True) if soup.title else "No Title"
            data.append({"url": u, "title": title})
            time.sleep(1) # Be polite!
        except Exception as e:
            print(f"Failed to fetch {u}: {e}")

    # 4. Save
    if data:
        df = pd.DataFrame(data)
        print("\nDataset:")
        print(df)
        df.to_csv("crawled_sample.csv", index=False)
        print("Saved to crawled_sample.csv")

if __name__ == "__main__":
    main()
