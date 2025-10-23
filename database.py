import sqlite3
from datetime import datetime

def create_table():
    with sqlite3.connect('prices.db') as conn:
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS products (
                url TEXT,
                name TEXT,
                price REAL,
                date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()

def get_latest_price(url):
    with sqlite3.connect('prices.db') as conn:
        c = conn.cursor()
        c.execute('''
            SELECT price FROM products WHERE url = ? ORDER BY date DESC LIMIT 1
        ''', (url,))
        row = c.fetchone()
        return row[0] if row else None

def insert_price(url, name, price):
    latest_price = get_latest_price(url)
    if latest_price != price:
        with sqlite3.connect('prices.db') as conn:
            c = conn.cursor()
            c.execute('''
                INSERT INTO products (url, name, price, date) VALUES (?, ?, ?, ?)
            ''', (url, name, price, datetime.now()))
            conn.commit()
        return True
    return False

def fetch_price_history(url):
    with sqlite3.connect('prices.db') as conn:
        c = conn.cursor()
        c.execute('''
            SELECT price, date FROM products WHERE url = ? ORDER BY date
        ''', (url,))
        return c.fetchall()
