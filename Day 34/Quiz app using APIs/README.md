# Quiz App using APIs
This is basically a quiz app with graphical interface using tkinter.
We get questions API from [Open Trivia DB](https://opentdb.com/api_config.php). This is online database which give us facility to chose or make quiz question and having different multiple options too.

## Steps
1. First we get the question from Api through following line of code.
   

        requests.get("https://opentdb.com/api.php", params=parameters)

2. Load these question's json file
3. Then by using Tkinter make a Gui and display questions there.

4. For gui make a class of quiz interface then load this in main file.
5. Also get different things from other files and used in ui.py file.

### Extra Hint
###  How to convert Text into correct format using HTML library.
For online converty you can go to [freeformatter.com](https://www.freeformatter.com/html-escape.html#before-output)
You must check this [ link](https://www.w3schools.com/html/html_entities.asp) too for better understanding of html.

For unscaping following line of code is used.
        
    html.unescape("Write text here")

### Example 
##### Without correct format
    Q.9: The Norse god Odin has two pet crows named &quot;Huginn&quot; and &quot;Muninn&quot;.  What do their names mean? (True/False):

##### With correct format
    Q.9: The Norse god Odin has two pet crows named "Huginn" and "Muninn".  What do their names mean? (True/False):

