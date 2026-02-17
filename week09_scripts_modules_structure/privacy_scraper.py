
import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass
import re
import time

@dataclass
class ScrapeResult:
    url: str
    status: int | None
    title: str | None
    cues: dict
    error: str | None = None

class PolicyScraper:
    def __init__(self, user_agent: str = "HF-PrivacyScraper/0.1"):
        """Initialize the scraper with a session and specific headers."""
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": user_agent})

    def fetch(self, url: str) -> str:
        """Fetch the URL using the session."""
        print(f"Fetching {url}...")
        r = self.session.get(url, timeout=20)
        r.raise_for_status()
        return r.text

    def parse(self, url: str, html: str) -> ScrapeResult:
        """Parse HTML to extract title and privacy cues."""
        soup = BeautifulSoup(html, "html.parser")
        text = soup.get_text(" ", strip=True)
        
        # Regex search for keywords
        cues = {
            "choices_controls": bool(re.search(r"\b(opt\s?-?out|preferences|your choices|controls?)\b", text, re.I)),
            "retention": bool(re.search(r"\b(retention|retain)\b", text, re.I)),
            "third_party": bool(re.search(r"\b(third\s?-?party|sharing|share)\b", text, re.I)),
        }
        
        return ScrapeResult(
            url=url,
            status=200,
            title=soup.title.get_text(strip=True) if soup.title else None,
            cues=cues,
        )

    def scrape(self, url: str) -> ScrapeResult:
        """Orchestrate the fetch and parse process."""
        try:
            html = self.fetch(url)
            return self.parse(url, html)
        except Exception as e:
            print(f"Failed to scrape {url}: {e}")
            return ScrapeResult(url=url, status=None, title=None, cues={}, error=str(e))

def main():
    scraper = PolicyScraper()
    urls = [
        "https://www.mozilla.org/en-US/privacy/",
        "https://www.nist.gov/privacy-framework",
    ]
    
    for url in urls:
        result = scraper.scrape(url)
        print(f"Result for {result.url}:")
        print(f"  Title: {result.title}")
        print(f"  Cues: {result.cues}")
        print("-" * 40)
        time.sleep(1)

if __name__ == "__main__":
    main()
