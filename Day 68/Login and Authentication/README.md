# Login Authentication and Secret Password generation To store in Database

In this project we figure out how to encrypt our passeord and then store in database. So no hacker can easily hack our passwords.

# Steps to Follow:
1. Encryption
   1. So encryption is hiding the information via some secret key so outsider can understand what its real meaning.
      1. In this we convert simple text to ciphertext to encrypt and reverse it to decrypt.
   
          Example:
   
              1. Plaintext:    The quick brown fox jumps over the lazy dog.
              2. ciphertext:   xasvj vvvgs jjtdp bknlj ruzgg guiol xkivf.


2. Hashing Passwords using Werkzeug 
   1. Go to [Documentation](https://werkzeug.palletsprojects.com/en/1.0.x/utils/#module-werkzeug.security) and see how we use it.

3. Securing Routes 
   1. For this Go to [Configure application](https://flask-login.readthedocs.io/en/latest/#configuring-your-application).
   2. We do this to secure our routes, for example if user is authenticated then he have access to special routes.
   3. We can import [LoginManager](https://flask-login.readthedocs.io/en/latest/#flask_login.LoginManager) class from Flask-login. This LoginManager helps to run application and Flask-Login at a same time. Like use_loader get user id and check is_authenticate,is_loggged type function. In simple it make work easy to identify is user is authenticated.
   4. Go to [Documentaion](https://flask-login.readthedocs.io/en/latest/#your-user-class) for more understanding.
4. Used Flask card to show some mesasges on screen.
   1. If user type wrong eamil messeage shows thet its wrong email try again.
   2. If password is wrong then messeage shown related to password.
   3. Go to https://flask.palletsprojects.com/en/1.1.x/patterns/flashing/ forunderstanding how we use it.