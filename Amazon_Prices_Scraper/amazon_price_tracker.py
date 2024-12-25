import smtplib

import requests
from bs4 import BeautifulSoup

# The below link in the URL is of MacBook 16 inch. But you can add the link of the product you want to track.
URL = "https://www.amazon.com/dp/B0DLHBYRPS/ref=fs_a_mbt2_us1"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
}


def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    title = soup.find(id="productTitle").get_text()
    print(title)
    
    text = soup.find(class_="a-size-medium a-color-success").get_text()
    print(text)
    


def send_mail():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("***@gmail.com", "password***")

    subject = "PRICE FELL DOWN OF MACBOOK"
    body = "Check the AMAZON link - https://www.amazon.in/Apple-MacBook-16-inch-Storage-2-3GHz/dp/B081JWZSSX/ref=sr_1_3?keywords=macbook+pro&qid=1580832880&sr=8-3 "
    #server.sendmail("***@gmail.com", "********@gmail.com", msg)

    print("Email has been sent !!!!!")
    server.quit()


print(check_price())
