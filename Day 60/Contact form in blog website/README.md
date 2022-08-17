# Website for Blog
In this website the data fetch from Api and then post on website using jinja.

# Steps to Follow

1. Go to https://startbootstrap.com/previews/clean-blog/ to download free template of blog website.
    You can also visit for getting template of your choice.
   1. https://bootstrapmade.com/  
   2. https://www.creative-tim.com/bootstrap-themes/free
2. Create templates and static folder, templates folder contain only .html files while rest of file should be in static folder.
3. Create header.html and footer.html and get code from index.html and put it in respected file.
4. Using Jinja Include fo Render Templates by doing this you don't need to add everytime header or footer in website pages. You can access it by using only single file and from following code you can use it in any website page. 

    
    #For header
    {% include "header.html" %}
    #For footer
    {% include "footer.html" %}
5. Create your own JSON bin with https://www.npoint.io/ or you can use mine https://api.npoint.io/c67d1455fa94791892d6
6. In main.py get hold of the JSON data at the above API endpoint.
7. Then give the whole list of data into index.html
8. By using loop post the data like title and subtitle on home page in index.html.

9. You can use following links for understanding how template use variables and for loop.
   1. https://jinja.palletsprojects.com/en/2.11.x/templates/#for
   2. https://jinja.palletsprojects.com/en/2.11.x/templates/#variables


## Modification in this application

1. Add a form page for contact details.
2. Handle POST Request with Flask server
   1. Visit this website https://www.w3schools.com/tags/att_form_action.asp
   2. For sendind data from html to python script visit https://stackoverflow.com/questions/11556958/sending-data-from-html-form-to-a-python-script-in-flask
3. First visit [Flask Documentation](https://flask.palletsprojects.com/en/1.1.x/quickstart/#the-request-object) where you understand how POST and GET requests work.
4. We set action attribute to form tag to get access of form.
5. 