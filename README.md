# Price Tracker

An automated Python tool that tracks product prices on popular e-commerce websites like Amazon and Flipkart. It stores price history in an SQLite database and sends real-time email alerts when prices drop below defined thresholds.

## Features

- Scrapes product prices and details from multiple online stores.
- Stores price history with timestamps in a SQLite database.
- Sends automated email alerts when prices drop to target values.
- Easy configuration using a CSV file for product URLs and alert prices.
- Modular design for adding new websites or notification methods.

## Quickstart

1. Clone this repository:
git clone https://github.com/404prateek/Price-Tracker-.git
cd Price-Tracker-

text

2. Activate your existing virtual environment:
source .venv/Scripts/activate # Windows PowerShell
source .venv/bin/activate # Linux/macOS

text

3. Install dependencies (if not already done):
pip install -r requirements.txt

text

4. Prepare the `urls.csv` file with columns:
- `url`: Product URL
- `alert_price`: Price to trigger email alert

5. Initialize the database (run once):
from database import create_table
create_table()

text

6. Run the price tracker script:
python main.py

text

7. Receive email notifications when prices drop.

## Configuration

- Store your email credentials securely using environment variables.
- Extend parsers or notifications as needed.

## Contributing

Feel free to report issues or suggest features via GitHub issues or pull requests.

## License

MIT License