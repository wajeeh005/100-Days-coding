# Flask WTF
Its a simple integration of Flask and WTForms.  
It also include CSRF,file upload, and also reCAPTCHA.


## Features or benefits over simple HTML form
1. It does Integration with WTForms. 
2. It does easy form validation.
3. It helps to Secure Form with CSRF (Cross Site Scripting Forgery) token. 

For WTForms Documentation [CLICK HERE](https://wtforms.readthedocs.io/en/2.3.x/).  
For Flask WTF Documentation [CLICK HERE](https://flask-wtf.readthedocs.io/en/1.0.x/).


WTForms basic fields https://wtforms.readthedocs.io/en/2.3.x/fields/#basic-fields


It has built-in validation. Instead of writing own validation code we can use build-in function DataRequired(). Which chechk automatically that
we have "@" in email, minimum password length and so on.
https://wtforms.readthedocs.io/en/2.3.x/crash_course/#validators

Validators paameters accept List of validators object. The DataRequired make field required, user must type in something otherwise it generates an error.

In order to make sure all required field for chrome we have to switch off the browser validation. we use attribute of form "novalidate"
  
        <form method="POST" action="{{ url_for('login') }} " novalidate>


