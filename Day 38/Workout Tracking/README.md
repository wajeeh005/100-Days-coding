# Workout Tracking using Google Sheet

In this application we track our workout on a Google sheet via python, and it works on NLP natural language process means we give details and it extract the meaning from detail and then calculate the calories we burnt.

  
For more details about How NLP work Click on this link [openai.com](https://openai.com/blog/openai-api/)

## Steps to Follow

1. Click [HERE](https://docs.google.com/spreadsheets/d/1DHL6Y8XAHSC_KhJsa9QMekwP8b4YheWZY_sxlH3i494/edit#gid=0) and make
   a copy of sheet to your account.
2. Go to [Nutritionix](https://www.nutritionix.com/business/api) and generate you API key.
3. After generating Store the ID and Key in these variable name, APP_ID and API_KEY.
4. Go to [NLP Exercise Demo](https://www.nutritionix.com/natural-demo/exercise?q=i%20do%206%20miles%20workout%20%20and%20%203%20km%20running) to understand how it work.
5. Go to [ Nutritionix Exercise Documentation](https://docs.google.com/document/d/1_q-K-ObMTZvO0qUEAxROrN3bwMujwAN25sLHwJzliK0/edit#heading=h.zhjgcprrgvim)
6. [Log into Sheety](https://sheety.co/) with your Google Account (the same account that owns the Google Sheet you copied).
7. Create New Project and click on the workouts API endpoint and enable GET and POST.
8. Go to [Sheety Documentation](https://sheety.co/docs/requests) to understand how to request.
9. Use the Python datetime module for current date and time.
10. For Authentication of Your Sheety API add either "Basic Authentication" or "Bearer Token" to your Sheety endpoint to secure it.
11. Also use Environment Variables for securing your keys.


### Where You do changes in code
1. You have to replace APP_ID and API_KEY with yours.
2. You have to replace sheet_endpoint with yours.

### Example 
Input:
      
      I walk for 25 minutes.  


Output

      Date	         Time	       Exercise	    Duration	   Calories
      28/07/2022	19:29:48	    Walking	      25	        110.83
         

We enter walk and 25 minutes Through NLP it get the meaning and save the data in sheet.