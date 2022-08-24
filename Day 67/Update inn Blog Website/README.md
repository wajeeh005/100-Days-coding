# Updating Blogs Website by adding following Functionality

1. Get all post from Database.
2. Post a new Blog Post.
3. Edit the existing Blog.
4. Also Delete the Blog Post.


## Steps to follow:
### 1. We have to get all the post from the posts.db SQLite databse.  
for this we use following query.

    BlogPost.query.all()
Which fetch all the data from the database column BlogPost.

### 2. For posting new blog first we need to figure out how to use Flask CKEditor package.
It used to make Blog content(body) input in the WTForm into a full CKEditor.

Check out following links for more details.
1. https://flask-ckeditor.readthedocs.io/en/latest/basic.html
2. https://pythonhosted.org/Flask-Bootstrap/forms.html
3. https://flask-wtf.readthedocs.io/en/stable/

2.2.    The data from CKEditor must be save in html format for that we use [Jinja safe() filter](https://jinja.palletsprojects.com/en/2.11.x/templates/#safe)

### 3. Edit a Post
For this first we need get the post id. And then it should auto-populate the field in the WTForm with blog's data. You change the properties via create blog and then all chagnes should be update in database.
so for that we have to replace the data wit HTML form data.

### 4. Delete a post from database.
We use following code 

    post_to_delete = BlogPost.query.get(post_id)
    db.session.delete(post_to_delete)
    db.session.commit()

first get post via post id then delete and save final changes in db.