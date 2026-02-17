
import re
import requests
from bs4 import BeautifulSoup
import pytest

# --- Pure Functions (Testable) ---

def fetch_text(url: str) -> str:
    """Fetches text from a URL. (Impure - side effect)"""
    try:
        r = requests.get(url, timeout=20)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")
        return soup.get_text(" ", strip=True)
    except Exception as e:
        print(f"Error: {e}")
        return ""

def parse_cues(text: str) -> dict:
    """Extracts privacy cues from text. (Pure - deterministic)"""
    return {
        "choices_controls": bool(re.search(r"\b(opt\s?-?out|preferences|your choices|controls?)\b", text, re.I)),
        "retention": bool(re.search(r"\b(retention|retain)\b", text, re.I)),
        "third_party": bool(re.search(r"\b(third\s?-?party|sharing|share)\b", text, re.I)),
    }

def normalize_row(url: str, cues: dict) -> dict:
    """Combines URL and cues into a flat dictionary. (Pure)"""
    return {"url": url, **cues}

# --- Tests ---

def test_parse_cues():
    sample_text = "You can opt out in settings. We retain data for 30 days."
    cues = parse_cues(sample_text)
    assert cues["choices_controls"] is True
    assert cues["retention"] is True
    assert cues["third_party"] is False

# --- Pipeline ---

def main():
    urls = [
        "https://www.mozilla.org/en-US/privacy/",
        "https://www.nist.gov/privacy-framework",
    ]
    
    # Functional pipeline: Map URLs -> Text -> Cues -> Rows
    print("Running pipeline...")
    results = [
        normalize_row(u, parse_cues(fetch_text(u))) 
        for u in urls
    ]
    
    print("\nResults:")
    for row in results:
        print(row)

    # Run manual test
    print("\nRunning unit tests...")
    test_parse_cues()
    print("Tests passed!")

if __name__ == "__main__":
    main()
