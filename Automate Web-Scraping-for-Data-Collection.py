import requests
from bs4 import BeautifulSoup
import csv

def scrape_website(url, output_file):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Example: Scrape product names and prices
    products = []
    for item in soup.select('.product-item'):
        name = item.select_one('.product-name').text.strip()
        price = item.select_one('.product-price').text.strip()
        products.append([name, price])

    # Save to CSV
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Product Name', 'Price'])
        writer.writerows(products)
    
    print(f"Scraped data saved to {output_file}.")

if __name__ == "__main__":
    url = "https://www.example.com/products"
    output_file = "products.csv"
    scrape_website(url, output_file)
