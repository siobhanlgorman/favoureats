# Agile
The Agile methodology was used to plan the project. Github was used as the tool to demonstrate this. However Github is not the ideal tool to adequately link Iterations - Epics - User Stories. Although I linked User Stories (Issues) to Epics (Milestones) and placed these in Iterations (Milestones), Epics did not automatically show the % progress to completion once user stories were moved in the kanban board. It also proved difficult with this developer's level of competence and the short time frame allowed, to accurately itemise all tasks in a user story in advance of implementation. As a result some user stories were updated during the course of implementation.

# UX
## Strategy
### Project Goal

The goal of the project is to create a recipe website with tried and tested recipes for both family meals and dinner parties. Inspiration for the site came from a book club group who requested a place to store the recipes for the lovely dinners provided at their regular meetings. This idea was expanded to appeal more broadly to general users looking for good recipes and a means to store, edit and delete their own favourite recipes.
### Epics and User Stories
#### Epic: Set up admin page for admin to manage recipe posts, reviews and site users
  * As a site admin I can CRUD draft recipe posts so that I can complete the recipes later (must-have / complete)
  * As a Site Admin I can CRUD posts so that I can manage my site content (must-have / complete)
  * As a site admin I can approve reviews so that I can filter out inappropriate content (must-have / complete)
  * As an admin I can view the number of likes on a recipe post so that I can know which are the most popular
  * As an admin I can view reviews of a recipe post so that I can read the commentary on a recipe
  * As an admin I can create reviews of recipe posts so that I can generate discussion on recipe posts

#### Epic: Enable users to register on the site to access full features
  * As a user I can register an account so that I can access the full range of features on the site (must-have / complete)
#### Epic: Enable users to login/logout on the site to access full features
  * As a registered user I can login and logout of the site so that I can access my content (must-have / complete)
#### Epic: Enable registered users to review recipe posts
  * As a registered user I can click on a post in the recipe list so that I open the full recipe post (must-have / complete)
#### Epic: Create landing page to attract users to the site
  * As a user I can view a snapshot of the site on the landing page so that know what the site's purpose is
#### Epic: Enable registered users to read full recipe posts and reviews
  * As a registered user I can click on a post in the recipe list so that I open the full recipe post
#### Epic: Enable registered users to CRUD their own recipes
  * As a registered user I can CRUD my own recipes so that I can manage my own content (should-have / complete)
#### Epic: Create recipe list page to showcase content to users
  * As a user I can view a paginated list of recipes so that I can see what I would like to select if registered (must-have / complete)
#### Epic: Enable registered users to search through their own recipes to enhance UX
  * As a user I can search my own recipe posts by title so that easily find a recipe (should-have / complete)
  * As a user I can search recipes by ingredient so that I can easily find a recipe that I want to use (could-have / future features)
#### Epic: Enable registered users to interact with recipe posts to enhance UX
  * As a registered user I can favorite/unfavorite recipes so that I can interact with the site content (must-have / complete)
  * As a logged-in user I can review a recipe so that I can interact with the site (must-have / complete)
#### Epic: Enable users to filter recipe posts to enhance UX
  * As a user I can search recipes by ingredient so that I can easily find a recipe that I want to use (could-have / future feature)
  * As a registered user I can filter favourite recipes to a list so that I can find all my favourites easily (should-have / future feature)
#### Epic: Enable users to sign-in/register with Google/Facebook account
  * As a user I can register an account with social networks so that I can streamline my accounts (could-have / future feature)
#### Epic: Enable users to CRUD own reviews
  * As a registered user I can create/read/update/delete my own review posts so that I can manage my own content (should-have / complete)
## Scope
## Structure
## Skeleton
### Wireframes
## Surface
# Features
## Existing Features

### All Pages
  * Navbar
  * Footer
  * Social media icons
### Home Page
  * Hero Image with overlay text highlighting the purpose of the site
  * Register link button on hero image to encourage users to register. Button becomes invisible if user is signed in
  * Snapshot images of three most recent recipe posts
  * View recipes link button at bottom of page to direct users easily to view the full recipe list
### About Page
### Recipes Page
### My Recipes Page


## Future Features
### User sign-in with Google/Facebooks
### Search/Filter on Recipes page
### Search/Filter by ingredient
### Filter by favourites
### Apply full CRUD functionality to user's own reviews



## Design
### Colours
### Typography
### Images

# Database
# Technologies
# Testing
## Browser compatibility
## Responsiveness
## Code Validation
## User Story Testing
## Manual Testing
## Automated Testing
  * test files in testing md?

## Bugs
### Resolved Bugs
1. Image uploads from front end to home page and recipes page but is not visible in recipe detail page. Solved by changing src from `recipe_image` to `recipe.recipe_image.url`
2. When I added success messages to the create, edit and delete recipe functions the delete message would not appear. To fix this I had to override the delete method in the DeleteView with a delete function. I found the solution in [here](https://stackoverflow.com/questions/47636968/django-messages-for-a-successfully-delete-add-or-edit-item)
3. User generated ingredients and steps do not appear as lists. Fixed by adding `|linebreaks` to the steps and ingredients sections of the recipe detail template

### Unresolved Bugs
1. Min and Max validators imported and set for cook_time but although error is raised if value outside these is entered the dropdown indicated all integer values.
2. Number of comments does not appear on recipes page but number of favourites does 
## Gitpod Forking and Cloning
# Deployment
## Local Deployment: Forking and Cloning
## Heroku
1. First follow these steps to create your app:
* Install Django and gunicorn: `pip3 install django gunicorn`
* Install supporting database libraries dj_database_url and psycopg2 liibrary: `pip3 install dj_database_url psycopg2`
* Install Cloudinary libraries to manage photos: in the terminal window type `pip3 install dj-3-cloudinary-storage`
* Create file for requirements: in the terminal window type `pip freeze --local > requirements.txt`
* Create project: in the terminal window type `django-admiin startproject project_name .`
* Create app: in the terminal window type `python3 manage.py startapp app_name`
* Add app to list of `installed apps` in settings.py file: `'app_name'`
* Migrate changes: in the terminal window type `python3 manage.py migrate`
* Run the server to test if the app is installed: in the terminal window type `python3 manage.py runserver`
* If the app has been installed correctly the window will display `The install worked successfully! Congratulations!`

2. Create your Heroku app
* Navigate to the Heroku website
* In the Heroku browser window, create an account by entering your email address and a password
* Activate the account through the authentication email sent to your email account
* Click the new button and select create a new app from the dropdown menu
* Enter a name for the application which must be unique, in this case the app name is 'favoureats'
* Select a region, in this case Europe
* Click create app

3. Connect the Database in Heroku to Gitpod
* In the Heroku dashboard click on the Resources tab
* Scroll down to Add-Ons, search for and select 'Heroku Postgres'
* In the Settings tab, scroll down to 'Reveal Config Vars' and copy the text in the box beside DATABASE_URL.

4. Set up Environment Variables (Database url and Secret Key)
* In Gitpod create a new env.py file in the top level directory
* Add env.py to the .gitignore file
* In env.py import the os library
* In env.py add `os.environ["DATABASE_URL"] = "Paste in the text link copied above from Heroku DATABASE_URL"`
TIM DO I PASTE IN MY DB URL HERE?
* In env.py add `os.environ["SECRET_KEY"] = "Make up your own random secret key"`
* In Heroku Settings tab Config Vars enter the same secret key created in env.py by entering 'SECRET_KEY' in the box for 'KEY' and your randomly created secret key in the 'value' box.

5. Prepare the environment and settings.py file
* In Gitpod in the 'settings.py' file type:

 ```
 from pathlib import Path
 import os
 import dj_database_url

 if os.path.isfile("env.py"):
  import env
 ```
* Remove the default insecure secret key in settings.py and replace with the link to the secret key variable i Heroku by typing: `SECRET_KEY = os.environ.get(SECRET_KEY)`
* Comment out the `DATABASES` section in settings.py and replace with:
```
DATABASES = {
  'default': 
  dj_database_url.parse(os.environ.get("DATABASE_URL"))
  }`
```
6. Make migrations for the database
* In the terminal type:
```
python3 manage.py makemigrations`
python3 manage.py migrate`
```
7. Store the static and media files on Cloudinary
* Create a Cloudinary account and from the 'Dashboard' in Cloudinary copy your url into the envy.py file by typing: `os.environ["CLOUDINARY_URL"] = "your link goes here but you must remove the start so it begins with 'cloudinary://"`
* Add Cloudinary url to 'settings' 'config vars' in Heroku: type CLOUDINARY_URL: your url here e.g. cloudinary://
* Add DISABLE_COLLECTSTATIC to Heroku 'config vars': type DISABLE_COLLECTSTATIC in the box for 'key' and '1' in the value box (note: this must be removed for final deployment)
* Add Cloudinary libraries to installed apps section of `settings.py` in this order: 
 ```
 'cloudinary_storage'
 'django.contrib.staticfiles''
 'cloudinary'
 ```
* Tell Django to use Cloudinary to store media and static files. Type this in Static Files section of `settings.py`:
```
STATIC_URL = '/static'
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'STATIC')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE =
'cloudinary_storage.storage.MediaCloudinaryStorage'
* Link file to the templates directory in Heroku 
* Place under the BASE_DIR: TEMPLATES_DIR = os.path.join(BASE_DIR,
'templates')
```
* Change the templates directory to TEMPLATES_DIR. Place within the TEMPLATES array: `'DIRS': [TEMPLATES_DIR]`
* Add Heroku Hostname to ALLOWED_HOSTS: ```ALLOWED_HOSTS =
['favoureats.herokuapp.com', 'localhost']```

9. Create `media`, `static` and `templates` folders in top level directory in Gitpod
10. Create Procfile in top level directory: `workspace/favoureats/Procfile`
* In Procfile add: `web: gunicorn favoureats .wsgi
11. In Gitpod terminal add commit and push: 
```
git add .
git commit -m “Deployment Commit”
git push
```
12. Heroku Deployment: 
* In the top menu bar select 'Deploy'.
* In the 'Deployment method' section select 'Github' and click the connect to Github button to confirm.
* In the 'search' box enter the Github repository name for the project: favoureats: https://github.com/siobhanlgorman/favoureats
Click search and then click connect to link the heroku app with the Github repository. The box will confirm that heroku is connected to the repository.

13. Final Deployment
In Gitpod: 
* When development is complete in `settings.py` change the debug setting to: `DEBUG = False`
* In settings.py add: `X_FRAME_OPTIONS = 'SAMEORIGIN'`
* In Heroku settings config vars change the DISABLE_COLLECTSTATIC value to 0 or delete if no more development will be undertaken??????????
* Because DEBUG must be switched to True for development and False for production it is recommended that only manual deployment is used in Heroku. 
* To manually deploy click the button 'Deploy Branch'. The default 'main' option in the dropdown menu should be selected in both cases. When the app is deployed a message 'Your app was successfully deployed' will be shown. Click 'view' to see the deployed app in the browser. The live deployment of the project can be seen [here](https://favoureats.herokuapp.com/myrecipes/)

The app starts automatically and can be restarted by pressing the 'Run Program' button.
Forking the Repository
If you wish to fork the repository to make changes without affecting the original you can fork the repository

Navigate to the Favoureats GitHub repository
Click the 'Fork' button at the top right of the page.
A forked copy of the repository will appear in your Repositories page.
Cloning the Repository
On Github navigate to the main page of the After the Party.
Above the list of files click the dropdown code menu.
Select the https option and copy the link.
Open the terminal.
Change the current working directory to the desired destination location.
Type the git clone command with the copied URL: git clone https://github.com/siobhanlgorman/favoureats.git.
Press enter to create the local clone.

# Credits

[Dennis Ivy 'Django To Do List App With User Registration & Login'](https://www.youtube.com/watch?v=llbtoQTt4qw&t=68s) was useful for full CRUD functionality application.

This tutorial was used to auto generate slugs from the front-end: [Kodnito](https://kodnito.com/posts/slugify-urls-django/)

[Stack Overflow](https://stackoverflow.com/) was used for general queries

## Images
Dinner Party Image by <a href="https://pixabay.com/users/pexels-2286921/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1852926">Pexels</a> from <a href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1852926">Pixabay</a>