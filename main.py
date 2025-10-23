import pandas as pd
from database import create_table, insert_price
from notifier import send_alert
from parsers.amazon import parse_amazon
from parsers.flipkart import parse_flipkart

create_table()
df = pd.read_csv('urls.csv')

def scrape_site(url):
    if "amazon" in url:
        return parse_amazon(url)
    elif "flipkart" in url:
        return parse_flipkart(url)
    else:
        return None, None

for _, row in df.iterrows():
    url = row['url']
    alert_price = row['alert_price']
    name, price = scrape_site(url)
    if not name or not price:
        continue
    insert_price(url, name, price)
    print(f"{name} => ₹{price}")
    if price <= alert_price:
        send_alert(name, price, url)
