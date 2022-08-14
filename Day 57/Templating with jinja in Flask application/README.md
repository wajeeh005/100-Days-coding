# Jinja in Flask
In this you will understand how to use python in html file.

**1. How to use Python in HTML.**

   We can add python code into html using double curly bracket{{ }} inside these brackets we can add python code.

           <h1>{{ 5*6 }}</h1>
   Now this is treated as python code the result on website looks like 30.


**2. How to use Variables in HTML?**
     
   We can use variables with help of giving keywords arguments to the template and used them in html file.   
     
   For giving variables names and used them in html file. We give variable name via keyword with render_templates in our pyton file and use that Keyword as variable in HTML file.

           @app.route("/")
           def hello():
               random_number = random.randint(1,10)
               return render_template("index.html", num=random_number)
         
          #Access the avriable by using following code where we needed.
            {{ num }}
          
   You can get the random number by using num in html inside a double curly brackets.


**3. How to use "For" Loop in html?**
         
   For using For loop we have to give  % sign in start and end of curly bracket and also end loop via "endfor".    
         
         
         
            {% for i in range(1,10): %}      # For Starting the Loop
            <h3>{{print(i}}</h3>
            {% endfor %}                     # For Ending the loop
      

**4. How to use "IF " in html?**


            {% for i in range(1,10): %}
            {% if i == 2: %}                  # use If statement like this
            <h1>{{ print(i) }}</h1>
            {% endif %}                       # End if statment like this
            {% endfor %} 

   We can use if statement like this.
   

## Documentation And References

1. Go to Jinja Documentation via https://jinja.palletsprojects.com/en/2.11.x/templates/ .
2. Go to Rendering Templates via https://flask.palletsprojects.com/en/1.1.x/quickstart/#rendering-templates to understand how request module use how to use if else statement and many more.
