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
## Bugs
### Resolved Bugs
1. Image uploads from front end to home page and recipes page but is not visible in recipe detail page. Solved by changing src from `recipe_image` to `recipe.recipe_image.url`
2. When I added success messages to the create, edit and delete recipe functions the delete message would not appear. To fix this I had to override the delete method in the DeleteView with a delete function. I found the solution in [here](https://stackoverflow.com/questions/47636968/django-messages-for-a-successfully-delete-add-or-edit-item)

### Unresolved Bugs
1. Min and Max validators imported and set for cook_time but not working.
2. User created posts are added to public recipe list inside of only their own created recipes list
3. Number of comments does not appear on recipes page but number of favourites does 
4. User generated ingredients and steps do not appear as lists
## Gitpod Forking and Cloning
# Deployment
## Heroku
# Credits

[Dennis Ivy 'Django To Do List App With User Registration & Login'](https://www.youtube.com/watch?v=llbtoQTt4qw&t=68s) was useful for full CRUD functionality application
This tutorial was used to auto generate slugs from the fron-end: [Kodnito](https://kodnito.com/posts/slugify-urls-django/)
[Stack Overflow](https://stackoverflow.com/) was used for general queries
## Images
Dinner Party Image by <a href="https://pixabay.com/users/pexels-2286921/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1852926">Pexels</a> from <a href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1852926">Pixabay</a>