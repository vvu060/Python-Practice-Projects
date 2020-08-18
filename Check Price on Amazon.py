import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.com/dp/B07RKPP1YL/ref=sr_1_2?crid=2T5VGC65G66Y5&dchild=1&keywords=dji+mavic+mini&qid=1593875037&sprefix=dji%2Caps%2C279&sr=8-2'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    print(soup.prettify())

    title = soup.find(id="productTitle")
    price = soup.find(id="priceblock_ourprice").getText()
    converted_price = float(price[0:5])

    if(converted_price < 450):
        send_mail()
#    print(converted_price)
#   print(title)

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('vvu060@gmail.com', 'asa')

    subject = 'Price Fell Down!'
    body = 'https://www.amazon.com/dp/B07RKPP1YL/ref=sr_1_2?crid=2T5VGC65G66Y5&dchild=1&keywords=dji+mavic+mini&qid=1593875037&sprefix=dji%2Caps%2C279&sr=8-2'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'vvu060@gmail.com',
        'vishal.urankar@skema.edu',
        msg
    )
    print("EMAIL SENT")

    server.quit()

while(True):
    check_price()
    time.sleep(60*60)