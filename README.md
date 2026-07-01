# Flipkart Product Scraper

Scrapes Flipkart search results and saves product titles and prices to a CSV file.

## Features

* Search any product by keyword
* Choose how many pages to scrape
* Results saved to a named CSV file
* Handles request errors gracefully

## Requirements

* Python 3
* requests
* beautifulsoup4
* lxml

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python flipkart_scraper.py
```

You'll be asked for:

* Product keyword
* Starting page number
* Ending page number

Output file will be named `flipkart_[keyword].csv`

## Sample Output

| Sr No. | Title                          | Price |
| ------ | ------------------------------ | ----- |
| 1      | Men & Women Solid Ankle Length | ₹164  |
| 2      | Men Solid Ankle Length         | ₹113  |

## Note

Built as a Python web scraping practice project.
