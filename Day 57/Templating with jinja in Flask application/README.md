# Jinja in Flask
In this you will understand how to use python in html file.

1. We can add python code into html using double curly bracket{{ }} inside these brackets we can add python code.

        <h1>{{ 5*6 }}</h1>
Now this is treated as python code the result on website looks like 30.

2. We can also give keywords arguments to the template and used them in html file.
   
   For giving variables names and used them in html file. We give variable name with render_templates in our pyton file.

        @app.route("/")
        def hello():
            random_number = random.randint(1,10)
            return render_template("index.html", num=random_number)
         
       #html file
3. USe {% for %} for loop
4. end with {% endfor %}