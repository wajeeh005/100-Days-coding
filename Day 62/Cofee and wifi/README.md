# Coffee & Wi-Fi
This is website contain the all the details like opening ,closing time, wifi availability, socket avalibiity and also google map location of nearby cafes which have both coffee services and wifi too. 


1. Use Custom Css File

    You can add custom Css File:
    
        {% block styles %}
        {{super()}}
        <link rel="stylesheet"
              href="{{url_for('.static', filename='mystyle.css')}}">
        {% endblock %}

    For more Examples :
        https://pythonhosted.org/Flask-Bootstrap/basic-usage.html#examples


2.  Use Bootstrap Tables 

    Go to this website https://getbootstrap.com/docs/4.5/content/tables/ and you will understand how to generate a table.


3. Use quick_form 

    First make a class and use Wtform different field like StringField, SubmitField, URLField, TimeField, SelectField, etc.
    Also use a validator to check that the URL field has a URL entered , Required Field, etc.

    [Wtform Documentation](https://pythonhosted.org/Flask-Bootstrap/forms.html)