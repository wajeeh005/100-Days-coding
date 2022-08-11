# San Francisco Renting House Research
In this project we make a form which have 3 question.
1. address
2. Link to the page of that address
3. price of property

And get data from ZILLOW website and put that data into sheet using Selenium and BeautifulSoup.

# Steps to Follow
1. Go to https://docs.google.com/forms/ and create your own form.
2. Then Create 3 question as ask above and answer type should be 'Short Answer'.
3. Go to [this web address on Zillow](https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.53941573095703%2C%22east%22%3A-122.32792891455078%2C%22south%22%3A37.68487039303953%2C%22north%22%3A37.83686652896213%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D) and see how the website is structured, this is where you'll be scraping the data from.
4. Use Request to get response from it must provide http headers.
5. Then use beautiful soup to scrap and get the Address, Prices and Links of all properties.

    **Hint:** Use Select to get the data from website. 
6. Then using Selenium send all these data to your google Form.
