# 🗓️ 12-Week Project Curriculum: *Python Through Data Scraping*

## 🧠 Learning Philosophy

Each week delivers:
- One **Python concept**
- One **scraping/data task**
- One **analysis outcome**

By Week 12 they will have built:

✅ A reproducible scraper  
✅ Clean datasets (CSV/JSON)  
✅ Analytical summaries + plots  
✅ Modular Python package  
✅ Optional LLM enrichment pipeline  

---

# 📅 Phase 1 - Python Foundations Through Small Scrapers (Weeks 1-4)

Goal: Refresh Python while doing meaningful work immediately.

---

## Week 1 - Python as a Data Tool (Lists, Loops, Notebooks)

**Concepts**
- Lists
- For-loops
- Basic functions
- Printing structured output

**Project**
Scrape a simple table from Wikipedia.

Example target:
> List of countries by population (static HTML)

![How to Import a Wikipedia Table Using R - Displayr Help](https://help.displayr.com/hc/article_attachments/360006613596) ![How to inspect elements with developer tools - IONOS](https://www.ionos.com/digitalguide/fileadmin/DigitalGuide/Screenshots_2023/chrome-elements-styles.jpg) ![Tables in HTML documents](https://www.w3.org/TR/REC-html40-971218/images/mergedcells.gif) ![Web Design](https://content.dodea.edu/VS/HS/webdesign/masterz/s/module4/images/table-tag-example.gif) 

**Skills Introduced**
- Using `requests`
- Understanding HTML structure (tags)
- Extracting rows manually

**Python Concepts**
```python
for row in rows:
    print(row.text)
```

**Outcome**
→ A Python list of structured observations.

---

## Week 2 - Dictionaries + Structured Thinking

**Concepts**
- Dictionaries
- Key-value modeling
- Data normalization

**Project**
Convert Week-1 scrape into structured dataset.

```python
country = {
    "name": name,
    "population": population,
    "year": 2024
}
```

**New Idea**
> Python dict = row in a dataset.

**Outcome**
→ List of dictionaries → proto-DataFrame mindset.

---

## Week 3 - Functions + Reusability

**Concepts**
- Writing reusable functions
- Parameters
- Return values

**Project**
Turn scraper into reusable pipeline:

```python
def scrape_country_table(url):
    ...
    return data
```

**Lesson**
> Scientists don’t write scripts. They write *tools*.

---

## Week 4 - CSV vs JSON (Data Formats)

**Concepts**
- Serialization
- CSV vs JSON differences
- Writing files

**Project**
Export scraped dataset both ways.

```python
import csv
import json
```

**Discussion**
| CSV | JSON |
|-----|------|
Flat | Nested |
Analysis | APIs |
Small | Flexible |

**Outcome**
They understand **data engineering tradeoffs**.

---

# 📅 Phase 2 - Real Web Scraping + Pythonic Thinking (Weeks 5-8)

Now we introduce **BeautifulSoup + Python fluency.**

---

## Week 5 - BeautifulSoup + HTML Parsing

**Concepts**
- Parsing trees
- Finding elements
- CSS selectors

![Guide to Parsing HTML with BeautifulSoup in Python](https://stackabuse.s3.amazonaws.com/media/parsing-html-with-beautifulsoup-in-python-3.jpg) ![CSS and the DOM :: CIS 526 Textbook](https://textbooks.cs.ksu.edu/cis526/images/1.3.2.png) ![Get started viewing and changing the DOM - Microsoft Edge Developer  documentation | Microsoft Learn](https://learn.microsoft.com/en-us/microsoft-edge/devtools/dom/index-images/select-element-page-inspect.png) ![Get started with viewing and changing the DOM | Chrome DevTools | Chrome  for Developers](https://developer.chrome.com/static/docs/devtools/dom/image/inspecting-ul-node-d23485a3dcc19.png) 

**Project**
Scrape research article listings (e.g., arXiv category page).

**Key Skill**
```python
soup.find_all("div", class_="meta")
```

---

## Week 6 - List Comprehensions + Cleaner Code

**Concepts**
- List comprehensions
- Filtering logic
- Pythonic style

Before:
```python
items = []
for x in results:
    if condition:
        items.append(x)
```

After:
```python
items = [x for x in results if condition]
```

**Project**
Clean scraped metadata.

---

## Week 7 - Sets + Deduplication + Data Integrity

**Concepts**
- Sets
- Removing duplicates
- Data validation

**Project**
Scrape multiple pages → deduplicate papers.

```python
unique_titles = set(titles)
```

---

## Week 8 - Intro Data Analysis (Pandas + Descriptive Stats)

**Concepts**
- DataFrames
- Mean / distribution
- Grouping

**Project**
Analyze scraped dataset:
- Papers per year
- Authors per paper

**They now see Python as a research tool.**

---

# 📅 Phase 3 - Moving to Real Python Development (Weeks 9-10)

🚨 Transition from notebooks → VS Code.

---

## Week 9 - Scripts, Modules, and Project Structure

**Concepts**
- `.py` files
- `if __name__ == "__main__"`
- Imports
- Virtual environments

Project becomes:

```
scraper_project/
  scraper/
  analysis/
  data/
```

**Major milestone:** they feel like a developer.

---

## Week 10 - Classes + OOP for Scrapers

**Concepts**
- Classes
- Encapsulation
- Reusable scrapers

```python
class ArxivScraper:
    def fetch()
    def parse()
    def save()
```

Lesson:
> OOP = managing complexity, not “fancy Python”.

---

# 📅 Phase 4 - Functional Patterns + Scaling Thinking (Week 11)

**Concepts**
- `map`, `lambda`
- Functional pipelines
- Clean transformations

**Project**
Create transformation pipeline for scraped data.

---

# 📅 Phase 5 - LLM-Enhanced Scraping (Week 12)

Now we add modern AI workflows.

---

## Week 12 - Using Gemini/OpenAI to Enrich Data

**Concept**
LLMs as *post-processing engines*, not scrapers.

Example:
- Summarize papers
- Classify topics
- Extract entities

Pipeline becomes:

```
Scrape → Clean → Send to LLM → Enriched dataset
```

This is the **real modern research stack.**

---

# 🧰 Tools Introduced Gradually

| Stage | Tools |
|------|------|
Early | requests, notebooks |
Mid | BeautifulSoup, pandas |
Later | VS Code, modules |
Final | Gemini/OpenAI APIs |

---

# 📊 Final Deliverable (What They Build)

A complete reproducible pipeline:

```
python run_scraper.py
```

Outputs:
- Structured dataset
- Analysis plots
- AI-enriched insights

---

# 🎯 Concepts Learned (Without Ever Doing “Toy Exercises”)

✔ Lists, dicts, sets  
✔ Functions  
✔ Comprehensions  
✔ OOP  
✔ Functional programming  
✔ File formats  
✔ Data analysis  
✔ Real scraping  
✔ Research reproducibility  
✔ LLM integration  
