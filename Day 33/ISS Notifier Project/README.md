# ISS Notifier Project

#### What is ISS?

The International Space Station (ISS) is the largest modular space station currently in low Earth orbit. It is a multinational collaborative project involving five participating space agencies: NASA (United States), Roscosmos (Russia), JAXA (Japan), ESA (Europe), and CSA (Canada).

For further Details click [HERE](https://en.wikipedia.org/wiki/International_Space_Station).

## What is this Project?
   In this project we use Api of ISS for getting its location and then notify if satelite is moving above you or present on your location.
The notification is via mail by using SMTP.



### What is API?
API is Application Programming Interfaces basically its a barrier between your program and External system. Its is a set of rules if you meets the requirments of external system then you request to it and it responce back to you.

"An application programming interface (API) is a way for two or more computer programs to communicate with each other. It is a type of software interface, offering a service to other pieces of software."

For more details click [HERE](https://en.wikipedia.org/wiki/API).


## Steps to Follow
1. You have to make 2 testing emails one should be gmail an other should be on yahoo totally depends on you.


2. Then import "smtplib" to make a connection.


3. Your connection depends on account you used. 

   1. For Gmail 

          smtplib.SMTP("smtp.gmail.com")
   2. For Yahoo
           
          smtplib.SMTP("smtp.mail.yahoo.com")
   
4. You should first go to your account setting then in security and make your account less secure by turning on "less secure feature" this feature.



#### NOTE:
This is not working because GOOGLE turn off the less secure app feature. And I am not abl to turn it On. ASAP i got the right solution then i update this.