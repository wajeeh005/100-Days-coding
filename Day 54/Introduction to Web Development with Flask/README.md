# Introduction to Web Development with Flask
First you need to understand what is Backend and Fronted. A Full Stack Developer is someone who works with the Back End — or server side — of the application as well as the Front End, or client side.

### What is Web Development?
Web development is the coding or programming that enables website functionality.  

The web development hierarchy is as follows:

1. Front End (Client-side coding)
2. Back End (Server-side coding)
3. Database

For more Details Click [HERE](https://www.techopedia.com/definition/23889/web-development).
### What is Flask?
Flask is a Web Application Framework represents a collection of libraries and modules that enables a web application developer to write applications without having to bother about low-level details such as protocols, thread management etc.

[Click Here](https://flask.palletsprojects.com/en/1.1.x/quickstart/) To learn how to do hello world project via flask.


## Steps to Follow
1. Create a hello.py file and put the following code in it.


    from flask import Flask
    app = Flask(__name__)
    
    @app.route('/')
    def hello_world():
        return 'Hello, World!'


To run the application you can either use the flask command or python’s -m switch with Flask. Before you can do that you need to tell your terminal the application to work with by exporting the FLASK_APP environment variable:


    $ export FLASK_APP=hello.py
    $ flask run
        Running on http://127.0.0.1:5000/
If you are on Windows, the environment variable syntax depends on command line interpreter. On Command Prompt:
  

    C:\path\to\app>set FLASK_APP=hello.py

#### Helpful Links
1. Go to [Windows Command Cheat Sheet](http://www.cs.columbia.edu/~sedwards/classes/2015/1102-fall/Command%20Prompt%20Cheatsheet.pdf) and see simple useful command.
2. [Python Visualization](https://pythontutor.com/visualize.html#mode=edit) go to this website and understand how code will work step by step.
3. 