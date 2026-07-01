import requests
from bs4 import BeautifulSoup
import csv
import time

def scrape():
    keyword1 = input("Enter product to search: ")
    search_query = keyword1.replace(" ", "+")
    filename = keyword1.replace(" ", "_")

    start_page = int(input("Enter starting page number: "))
    end_page = int(input("Enter ending page number: "))

    if start_page > end_page:
        print("Starting page cannot be greater than ending page.")
        return

    base_url = f"https://www.flipkart.com/search?q={search_query}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    }

    session = requests.Session()
    session.headers.update(headers)

    with open(f"flipkart_{filename}.csv", "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Sr No.", "Title", "Price"])
        count = 0
        for page in range(start_page, end_page + 1):
            url = f"{base_url}&page={page}"
            try:
                response = session.get(url, timeout=10)
                response.raise_for_status()
                soup = BeautifulSoup(response.text, "lxml")
                products = soup.find_all("div", attrs={"data-id": True})
                for product in products:
                    count += 1
                    title = product.find("a", class_="atJtCj")
                    price = product.find("div", class_="hZ3P6w")


                    if title and price:
                        writer.writerow([count, title.get("title"), price.text.strip()])
            except requests.RequestException as e:
                print(f"Connection error {e}")
            time.sleep(3)

if __name__ == "__main__":
    scrape()
