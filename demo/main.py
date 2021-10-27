import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText

URL = "https://www.amazon.in/Lenovo-ThinkPad-15-6-inch-Microsoft-20RDS18B00/dp/B08HLKC8ZL/ref=sr_1_1?dchild=1&keywords=thinkpad&qid=1613056917&s=electronics&sr=1-1"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.4 Safari/605.1.15"}
PRICE_VALUE = 60000  # the comparing pirce


def trackPrices():
    price = float(getPrice())
    if price > PRICE_VALUE:
        diff = int(price - PRICE_VALUE)
        print(f"Still ₹{diff} too expensive")
    else:
        print("Cheaper! Notifying...")
        send(email)
    pass


def getPrice():
    page = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id='productTitle').get_text().strip()
    print(title)
    price = soup.find(id='priceblock_ourprice').get_text().replace("₹", "").replace(" ", "").replace(",", "").strip()
    print(title)
    print(price)
    return price


def send(email):
    subject = "Amazon Price Dropped!"
    mailtext = 'Subject:' + subject + '\n\n' + URL + "<br><br>" + "<storng>price dropped hurry up</strong><br>message from tarun"
    from_email = "kushvithchinna900@gmail.com"  # your email address
    from_password = "kushvithKushvitH"  # your email password
    to_email = email  # senders email address
    msg = MIMEText(mailtext, "html")
    msg["subject"] = subject
    msg['to'] = to_email
    msg['from'] = from_email

    yahoo = smtplib.SMTP("smtp.gmail.com", 587)
    yahoo.ehlo()
    yahoo.starttls()

    yahoo.login(from_email, from_password)
    yahoo.send_message(msg)
    yahoo.quit()
    print("email sent done!")
    pass


if __name__ == "__main__":
    trackPrices()
