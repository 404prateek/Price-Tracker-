import requests
from bs4 import BeautifulSoup

def parse_amazon(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to retrieve page, status code: {response.status_code}")
        return None, None

    soup = BeautifulSoup(response.content, 'html.parser')

    title_tag = soup.find('span', {'id': 'productTitle'})
    title = title_tag.get_text(strip=True) if title_tag else "Title not found"

    price_tag = soup.select_one('.a-price .a-offscreen')
    if not price_tag:
        price_tag = soup.find('span', {'id': 'priceblock_ourprice'}) or \
                    soup.find('span', {'id': 'priceblock_dealprice'})

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
    sample_url = "https://www.amazon.in/iPhone-17-Pro-Promotion-Breakthrough/dp/B0FQFBHQMJ/ref=sr_1_1?sr=8-1"  # replace with actual product URL
    product_name, product_price = parse_amazon(sample_url)
    if product_name and product_price:
        print(f"Product Name: {product_name}")
        print(f"Price: ₹{product_price}")
    else:
        print("Could not fetch product details.")
