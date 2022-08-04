import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

website_url = "https://www.amazon.com/dp/B09WVZBWWK/ref=sbl_dpx_kitchen-electric-cookware_B08GC6PL3D_0"

headers = { 'Accept-Language' : "en-US,en;q=0.9",
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
        }

response = requests.get(url=website_url, headers=headers)
web_html = response.content

soup = BeautifulSoup(web_html, "lxml")
title = soup.find(id="productTitle").get_text().strip()
print(title)
price_with_dollar_sign = soup.find("span", class_="a-offscreen").get_text()
price_without_dollar_sign = price_with_dollar_sign.split("$")[1]
float_price = float(price_without_dollar_sign)
print(float_price)

BUY_PRICE= 100
if float_price < BUY_PRICE:
    message = f"{title} is now in just {float_price}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login("Your email address","YOur password")
        connection.sendmail(to_addrs="to address",
                            from_addr="from address",
                            msg=f"subject:Amazon Price Alert!\n\n{message}\n{website_url}")


