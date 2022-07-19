# Flash Card App

### This application is basically help you to learn new words in diffrent language according to you.

1.  Its like flash card appears randomly from the list.

2.  It do like flassh card, on one side French word is written and on the other side its in English.

3.  If you guess the word correctly then tick and it 
will not apear again.

4. If you don't know the word in English you just      cross it ,it will come randomly.

You can get more words from [Wiktionary:Frequency_lists](https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists) and also from [FrequencyWords](https://github.com/hermitdave/FrequencyWords/tree/master/content/2018)


You can save word in Excel sheet in any language and then translate it via following formula
    =GOOGLETRANSLATE(text, [source_language, target_language])


### How it works

1.  Randomly generated words shown if you know Press tick button, that word will not appear again.

2. If you don't remember the word simply press Cross button, it will appear randomly next time.

3.  Everything store in a new file, so to help you to show the words next time which are unknown to you or you doesn't remmember.

## Steps must used in very project of Tkinter

1.  First create window
        window=Tk()

2.  Give title of window
        windo.title("Write Here a Title you want to give")

3.  Configure the window ,add padding or background
    colour etc
        window.config(padx=50,pady=50)

4.  Must End with following line
        window.mainloop()


### Following things we add after 3rd step

1.  Canvas , we can used this to add, draw diffrent things which we want to display. The width and height should be same as size of image we want to add.
        Canvas(width=800,height=524)

2.  PhotoImage(file="location of image") used to save the image in a variable

3.  creat_image used to display image on a canvas
    canvas.create_image(x_axis_value,y_axis_value,image=variable_name(used in step 2))



