# Rain Alert through SMS
This is basically send a message if rain getting start to your cellphone.

# Steps to Follow
1. First you have to make an account [Open Weather map](https://home.openweathermap.org/users/sign_up). Which is used to give you weather API according to your location.
2. If you want to find your location just enter the city name your longitude and lattitude will come from this website [https://www.latlong.net/](https://www.latlong.net/).
3. Go to Api documentation [Openweathermap API Documentation](https://openweathermap.org/api/one-call-api).
4. When You all go through the steps and done as do in documentation get the json data and used [Json Viewer](http://jsonviewer.stack.hu/) for better visualized the json data received from API.
5. Narow down your data to 12h by slicing. Check this link [Python slicing](https://www.w3schools.com/python/ref_func_slice.asp).
6. Now for SMS used [Twilio](https://www.twilio.com/try-twilio) this give multiple services sign up and used Programmable SMS Python service. 
7. To automate python script used [pythonanywhere](https://www.pythonanywhere.com/). Which give us facility to automate the code according to us like schedule the code to run. We used this to remind everytime when rain comes via SMS on cellphone.
8. Used Environment Variables to hide your personal API keys. 


    env
    export variable_name=key

Instead of variable name use variable name you used in code and on key that key value. For running in pythonanywhere you have to load these environments variable there too. 


## Note:
I tried to make Twilio account but everytime they suspend my account I don't know why. So I do as shown in video.
For more APIs used [ApiList](https://apilist.fun/).