# Automated Amazon Price Tracker

## Steps to follow
1. First open the product in which you are interested.
2. Use the requests library to request the HTML page of the Amazon product using the URL.
3. You have to pass some headers "User-Agent" and "Accept-Language" values in the request header. Use this link to find these values  
http://myhttpheader.com/
4. If you get an error that says **"bs4.FeatureNotFound: Couldn't find a tree builder with the features you requested: html-parser."**  
Then use **"lxml"** parser instead of the **"html.parser"**.
5. Use BeautifulSoup to Scrape the Product Price.
6. Convert the price into Float.
7. Use SMTP to send emails if price down enough to your price in which you want to purchase.




##### Note
My SMTP protocol is not working because google turn off  "allow less secure apps to access your account".

### Resources
1. https://www.amazon.com/dp/B09WVZBWWK/ref=sbl_dpx_kitchen-electric-cookware_B08GC6PL3D_0
2. https://docs.python.org/3/library/smtplib.html
3. http://myhttpheader.com/
4. 

