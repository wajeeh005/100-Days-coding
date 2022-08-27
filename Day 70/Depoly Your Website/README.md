# Deploy Your Website

## Steps to Follow
1. First upload your code on [github](https://github.com/).
2. Go to [gitignore.io](https://www.toptal.com/developers/gitignore/) and search for a Flask gitignore template. Copy all the text in the resulting page and create a new file at the top level of your project with the name .gitignore. Paste everything from the gitignore page to this file.
3. Add your GitHub details to PyCharm by going to the Version Control settings.

    Windows: File -> Settings -> Version Control -> GitHub  

    Then click on the "+" button and select Login via GitHub:
4. Next, create a new GitHub repo by going to   
    VCS -> Import into Version Control -> Share Project on GitHub

    Now, PyCharm will create a new remote repository on GitHub in your account and push all the local commits to the remote.

### Use gunicorn and Heroku to host your website

1. Sign up for a free account on [www.heroku.com](www.heroku.com).

2. Create a new application on Heroku.

3. Connect Heroku to your GitHub project. Under the Deploy tab, select Connect to GitHub

4. Search for the name of your blog project repository name (if in doubt check GitHub) and connect it to Heroku.

5. Scrolling further down the page on the deploy pane, click on Enable Automatic Deploys. This means that whenever you push a new commit to your remote GitHub repository, it will automatically re-deploy your server with the changes.

6. Finally, in Manual deploys, click on Deploy Branch to deploy for the first time.

7. Once it's done, click View to see your web app

