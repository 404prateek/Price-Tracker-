import requests
from bs4 import BeautifulSoup

def parse_flipkart(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to retrieve page, status code: {response.status_code}")
        return None, None

    soup = BeautifulSoup(response.content, 'html.parser')

    # Product title
    title_tag = soup.select_one('h1._6EBuvT')
    title = title_tag.get_text(strip=True) if title_tag else "Title not found"

    # Product price
    price_tag = soup.select_one('div.Nx9bqj.CxhGGd')
    if price_tag:
        price_text = price_tag.get_text(strip=True).replace('₹', '').replace(',', '')
        try:
            price = float(price_text)
        except ValueError:
            price = None
    else:
        price = None

    return title, price

if __name__ == "__main__":
    sample_url = "https://www.flipkart.com/apple-iphone-16-black-128-gb/p/itmb07d67f995271?pid=MOBH4DQFG8NKFRDY&lid=LSTMOBH4DQFG8NKFRDYNBDOZI&marketplace=FLIPKART&q=iphone+16&store=tyy%2F4io&spotlightTagId=default_BestsellerId_tyy%2F4io&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_2_2_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_2_na_na_na&fm=search-autosuggest&iid=680e6664-5cb0-4020-a696-80e6e131eb84.MOBH4DQFG8NKFRDY.SEARCH&ppt=sp&ppn=sp&ssid=yq5vft2pio0000001761114624457&qH=9ea15d2374058112"
    product_name, product_price = parse_flipkart(sample_url)
    if product_name and product_price:
        print(f"Product Name: {product_name}")
        print(f"Price: ₹{product_price}")
    else:
        print("Could not fetch product details.")
