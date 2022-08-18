# Flask WTF
Its a simple integration of Flask and WTForms.  
It also include CSRF,file upload, and also reCAPTCHA.


## Features or benefits over simple HTML form
1. It does Integration with WTForms. 
2. It does easy form validation.
3. It helps to Secure Form with CSRF (Cross Site Scripting Forgery) token. 

For WTForms Documentation [CLICK HERE](https://wtforms.readthedocs.io/en/2.3.x/).  
For Flask WTF Documentation [CLICK HERE](https://flask-wtf.readthedocs.io/en/1.0.x/).

### WTForms basic fields [Documentation](https://wtforms.readthedocs.io/en/2.3.x/fields/#basic-fields)
We can use built-in fields without going into details or a lot of coding. Just use like StringField,PasswordField, etc.

### Validators [Documentation](https://wtforms.readthedocs.io/en/2.3.x/crash_course/#validators)
It has built-in validation. Instead of writing own validation code we can use build-in function DataRequired(). Which chechk automatically that
we have "@" in email, minimum password length and so on.

Validators parameters accept List of validators object. The DataRequired make field required, user must type in something otherwise it generates an error.

In order to make sure all required field for chrome we have to switch off the browser validation. we use attribute of form "novalidate"
  
        <form method="POST" action="{{ url_for('login') }} " novalidate>


### Receiving Form Data with WTForms [Documentation](https://wtforms.readthedocs.io/en/2.3.x/crash_course/#how-forms-get-data)
it's even easier to get hold of the form data. All you have to do is to tap into the

    <form_object>.<form_field>.data

For checking form is submitted we simply use  

    validate_on_submit()

**Try**:
email: admin@email.com

password: 12345678

then show them the success.html page.
Otherwise show them the denied.html page


### Inheriting Templates Using Jinja2
As we use html template which remain same for more templates than we make a single file and used them in other files via including.
 
    {% include "header.html" %}

Same is the case we can use inheritence template. If the section remain same for more then one file and used same in different file then we simply inherit it using following code.
If title remain same.

    {% extends "base.html" %} means get template from base.html file
    {% block title %}{% endblock %}

If content of body remain same.

    {% block content %}{% endblock %}

#### Flask-Bootstrap 
We can use Flask-Bootstrap python extention to improve appearance of website.

    #In terminal
    pip install Flask-Bootstrap