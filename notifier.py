import smtplib
from email.mime.text import MIMEText

def send_alert(name, price, url):
    body = f"Price Drop Alert!\n\n{name} is now ₹{price}\nCheck it here: {url}"
    msg = MIMEText(body)
    msg['Subject'] = "Price Tracker Alert"
    msg['From'] = "prateekprogrammer.2004@gmail.com"
    msg['To'] = "receiver_email@example.com"

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login("prateekprogrammer.2004@gmail.com", "abc_1234")
            server.send_message(msg)
        print("Email alert sent!")
    except Exception as e:
        print(f"Error sending email: {e}")
