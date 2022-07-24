# Stock Trading News Alert Project

This application send news alert on cell phone via SMS when The stock value diffrence from last day greater then specific number then this news alert activate and send message to user.

## Steps to Follow
So, we are doing this for TESLA stock.
1. You can go to [TESLE](https://www.tradingview.com/symbols/NASDAQ-TSLA/) for viewing the overwiew of Tesla stocks.
2. For getting Stock API you have to go on [alphavantage](https://www.alphavantage.co/) and generate and API 
3. Then go to [Documentation](https://www.alphavantage.co/documentation/) to understand what parameters and how to used Api.
4. We also need a NEWS API for getting news related to our Stock name for this I used [newsapi](https://newsapi.org/).
5. And in the End used [Twilio](https://www.twilio.com/)

### The code for this break down into 9 steps.
1. Get yesterday's closing stock price.  

    **Hint:** You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
  

2. Get the day before yesterday's closing stock price.  


3. Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.  
**Hint:** https://www.w3schools.com/python/ref_func_abs.asp  


4. Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.  


7. If difference percentage is greater than 5 use the News API to get articles related to the COMPANY_NAME.
  

8. Use Python slice operator to create a list that contains the first 3 articles.  
**Hint:** https://stackoverflow.com/questions/509211/understanding-slice-notation.
  

9. Create a new list of the first 3 article's headline and description using list comprehension.
  

10. Send each article as a separate message via Twilio.
  

11. Format the message like this:

        
        
        TSLA: 🔺2%
        Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
        Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
        or
        TSLA: 🔻5%
        Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
        Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.



### Note:
All the steps are working perfectly but the step 10 in which we have to acces Twilio for SMS services is not work here due to i have no access to this account if you have then you just put you credential in code and it will work.