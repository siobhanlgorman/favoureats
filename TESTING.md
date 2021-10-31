# Automated Testing
## Set-up for testing in local environment
## Unittest
Unittest was used to test the correct template was rendered
# Manual Testing
## Testing User Stories
#### Epic: Set up admin page for admin to manage recipe posts, reviews and site users
To test the admin user stories begin with the following steps:
1. Navigate to the website of [favoureats](https://favoureats.herokuapp.com/)
2. Click on the 'Sign In' tab on the navigation menu bar
3. Sign in with admin's name and password
4. Navigate to [admin page](https://favoureats.herokuapp.com/admin/)

#### User Stories:
  * As a site admin I can create draft recipe posts so that I can complete the recipes later (must-have / complete)(#8)

  Description: The site administrator is able to create draft recipes.

  Testing Steps:
  
1. In the admin panel menu beside recipes click the add button
2. In the recipe form enter content in the fields
3. Click save to save the created recipe
 

  ![###](documentation/screenshots/admin_create.png)
  ![###](documentation/screenshots/admin_draft2.png)
  ![###](documentation/screenshots/admin_draft3png)

  ![###](documentation/screenshots/???png)

  Expected result: A draft recipe is saved by default to the list of recipes in the admin panel
  Actual result: A draft recipe is saved to the list of recipes in the admin panel
  Pass/Fail: Pass

  * As a Site Admin I can CRUD recipes so that I can manage my site content (must-have / complete)(#9)
  Description: The site administrator is able to create, read, update and delete recipes.

  Testing Steps:
  To create a recipe:
  
  1. In the admin panel menu beside recipes click the add button
  2. In the recipe form enter content in the fields
  3. Change the status to published from the status dropdown menu
  4. Click save to save the created recipe

Expected result: The recipe is saved as 'published' to the list of recipes in the admin panel. The recipe is viewable on the website
Actual result: The recipe is saved as 'published' to the list of recipes in the admin panel. The recipe is viewable on the website
Pass/Fail: Pass

To read/update a recipe:

1. In the admin panel list select a recipe title to read the full recipe
2. To update the recipe update the necessary fields and click save

Expected result: The viewed/updated recipe is saved to the list of recipes
Actual result: The viewed/updated recipe is saved to the list of recipes
Pass/Fail: Pass

To delete a recipe:
1. From the list of recipes in the admin panel select the recipe to be deleted in the checkbox beside the title
2. In the action dropdown menu above the list select 'delete' and 'go' to delete the recipe

Expected result: The viewed/updated recipe is deleted from the list of recipes and is not visible on the website
Actual result: The viewed/updated recipe is deleted from the list of recipes and is not visible on the website
Pass/Fail: Pass
  
  ![###](documentation/screenshots/admin_create.png)
   ![###](documentation/screenshots/default_draft.png)
  ![###](documentation/screenshots/admin_draft2.png)
    ![###](documentation/screenshots/admin_draft3png)
  ![###](documentation/screenshots/???png)

* As a site admin I can approve reviews so that I can filter out inappropriate content (must-have / complete)(#10)

Testing Steps:

1. In the admin panel select reviews to view a list of draft and published reviews
2. In the list select a review in the checkbox
3. In the action dropdown menu above the list select 'approve selected review' or 'delete selected review' and then 'go'

Expected result 1: The approved review is published on the website
Expected result 2: The deleted review is removed from the list of reviews
Actual result 1: The approved review is published on the website
Actual result 1: The deleted review is removed from the list of reviews
Pass/Fail: Pass

* As an admin I can view the number of favourites on a recipe post so that I can know which are the most popular(#28)

1. In the admin panel select a recipe
2. Scroll down to the favourites field to view highlighted names of users who have favourited the recipe
3. On the website navigate to the recipe list page where the number of favourites is shown under the recipeawarded to a recipe 
4. On the website click on a recipe to open the full detail to see the number of favourites beside the recipe

Expected result 1: The names of users who have favourited a recipe are highlighted in the admin panel recipe view
Expected result 2: The number of favourites appears beside the star on the recipes page
Expected result 3: The number of favourites appears beside the star on the recipe detail page


Actual result 1: The names of users who have favourited a recipe are highlighted in the admin panel recipe view
Actual result 2: The number of favourites appears beside the star on the recipes page
Actual result 3: The number of favourites appears beside the star on the recipe detail page

Pass/Fail: Pass

* As an admin I can view reviews of a recipe post so that I can read the commentary on a recipe(#29)
This is tested in #10 above with a PASS result.

* As an admin I can create reviews of recipe posts so that I can generate discussion on recipe posts(#31)

1. In the admin panel select the 'add' button beside 'Reviews'
2. In the content form select a recipe from the dropdown menu.
3. Complete the content fields and the checkbox 'approved' to publish or leave blank to create a draft
4. Click save

Expected result 1: The review appears in the list of reviews in the admin panel
Expected result 2: The approved review is published on the website

Actual result 1: The review appears in the list of reviews in the admin panel
Actual result 2: The approved review is published on the website
Pass/Fail: Pass

#### Epic: Enable users to register on the site to access full features
#### User Stories:
  * As a user I can register an account so that I can access the full range of features on the site (must-have / complete)(#18)

Testing Steps:
1. Navigate to the website of [favoureats](https://favoureats.herokuapp.com/)
2. Click on the 'Register' tab on the navigation menu bar
3. Create an account with username, email and password

Expected result 1: Message displays 'You have successfully signed in'
Expected result 2: Sign In link in navigation changes to Sign Out

Actual result 1: Message displays 'You have successfully signed in'
Actual result 2: Sign In link in navigation changes to Sign Out

Pass/Fail: Pass

  * As a registered user I can login and logout of the site so that I can access my content (must-have / complete)(#19)

Testing Steps:
1. Navigate to the website of [favoureats](https://favoureats.herokuapp.com/)
2. Click on the 'Sign In' link in the navigation menu and sign in with username and password
3. Click on the 'Sign Out' link to sign out.


Expected result 1: Message displays 'You have successfully signed in'
Expected result 2: Message displays 'You have successfully signed out'
Expected result 3: Sign In link in navigation changes to Sign Out and vice versa

Actual result 1: Message displays 'You have successfully signed in'
Actual result 2: Message displays 'You have successfully signed out'
Actual result 3: Sign In link in navigation changes to Sign Out and vice versa

Pass/Fail: Pass


#### Epic: Create landing page to attract users to the site
#### User Stories:
  * As a user I can view a snapshot of the site on the landing page so that know what the site's purpose is (must-have/complete)(#24)

Testing Steps:
1. Navigate to the website of [favoureats](https://favoureats.herokuapp.com/)
2. Scroll down the page to view the text in the hero image
3. Scroll down to view most recent recipes posted
4. Scroll down to see button to 'view recipes'

Expected result 1: Text visible on hero image explaining site
Expected result 2: Call to action 'Register' button on hero image
Expected result 3: Text indicating users must sign in to view full recipes and create recipes
Expected result 4: Three most recent images displaying
Expected result 5: Call to action 'View recipes' button on below three latest images directing users to recipes list page


Actual result 1: Text visible on hero image explaining site
Actual result 2: Call to action 'Register' button on hero image
Actual result 3: Text indicating users must sign in to view full recipes and create recipes
Actual result 4: Three most recent images displaying
Actual result 5: Call to action 'View recipes' button on below three latest images directing users to recipes list page

Pass/Fail: Pass

#### Epic: Enable registered users to CRUD their own recipes
#### User Stories:
  * As a registered user I can CRUD my own recipes so that I can manage my own content (should-have / complete)(#12)

Testing Steps:
1. Navigate to the website of [favoureats](https://favoureats.herokuapp.com/)
2. Click on the 'Sign In' link in the navigation menu and sign in with username and password
3. Navigate to the page of [favoureats](https://favoureats.herokuapp.com/myrecipes) to view a list of the logged in users recipes
4. Click on view beside a recipe in the list to view the full recipe detail page
5. Click on edit beside a recipe in the list to view the recipe form, edit the content and click on 'Submit Recipe' to save changes
6. Click on delete beside a recipe in the list to delete a recipe. 

Expected result 1: Full recipe detail page opens when view is clicked
Expected result 2: Recipe is updated on website when edits are submitted.
Expected result 3: Success message displays when updated recipe is submitted.
Expected result 4: Confirm delete page displays when user clicks on delete
Expected result 5: Success message displays when user successfully deletes recipe.

Actual result 1: Full recipe detail page opens when view is clicked
Actual result 2: Recipe is updated on website when edits are submitted.
Actual result 3: Success message displays when updated recipe is submitted.
Actual result 4: Confirm delete page displays when user clicks on delete
Actual result 5: Success message displays when user successfully deletes recipe.

Pass/Fail: Pass

#### Epic: Create recipe list page to showcase content to users
#### User Stories:
  * As a user I can view a list of recipes so that I can see what I would like to select if registered (must-have / complete)(#15)

Testing Steps:
1. Navigate to the website of [favoureats](https://favoureats.herokuapp.com/)
2. Click on the 'recipes' link in the navigation menu or the 'view recipes' button at the bottom of the page
3. Scroll down to view a summary list of recipes posted

Expected result 1: User is redirected to Recipes page

Actual result 1: User is redirected to Recipes page

Pass/Fail: Pass

#### Epic: Enable registered users to search through the recipes to enhance UX
#### User Stories:
  * As a user I can search my own recipe posts by title and ingredient so that easily find a recipe (should-have / complete)(#23)

Testing Steps:
1. Navigate to the website of [favoureats](https://favoureats.herokuapp.com/)
2. Login to the website
3. Click on the 'myrecipes' link in the navigation menu
4. Enter text in the search box and click the search icon
5. Click the 'x' to clear the search and return to full list of recipes

Expected result: List of recipes corresponding to search query is displayed or 'no recipes found' if there is no match

Actual result: List of recipes corresponding to search query is displayed or 'no recipes found' if there is no match

Pass/Fail: Pass

  * As a user I can search through the recipe list page by title and ingredient so that I can easily find a recipe (should-have / complete) (25)

Testing Steps:
1. Navigate to the website of [favoureats](https://favoureats.herokuapp.com/)
2. Click on the 'recipes' link in the navigation menu
3. Enter text in the search box and click the search icon
4. Click the 'x' to clear the search and return to full list of recipes

Expected result: List of recipes corresponding to search query is displayed or 'no recipes found' if there is no match

Actual result: List of recipes corresponding to search query is displayed or 'no recipes found' if there is no match

Pass/Fail: Pass

#### Epic: Enable registered users to interact with recipe posts to enhance UX
#### User Stories:
  * As a registered user I can click on a post in the recipe list so that I open the full recipe post (must-have / complete)(#20)

Testing Steps:
1. Navigate to the website of [favoureats](https://favoureats.herokuapp.com/)
2. Login to the website
3. Click on the 'recipes' link in the navigation menu
4. Click on the title of a recipe
5. Repeat test for user not logged in

Expected result: User is redirected to full recipe detail page. User not logged in is directed to 'sign in' page.

Actual result: User is redirected to full recipe detail page. User not logged in is directed to 'sign in' page.

Pass/Fail: Pass

* As a registered user I can favorite/unfavorite recipes so that I can interact with the site content (must-have / complete)(#11)

Testing Steps:
1. Navigate to the website of [favoureats](https://favoureats.herokuapp.com/)
2. Login to the website
3. Click on the 'recipes' link in the navigation menu
4. Click on the title of a recipe
5. Click on the star icon to toggle 'favourite' on and off

Expected result 1: When user clicks on star, star becomes full colour to favourite and outline only if not favourite.
Expected result 2: Number beside favourites star is updated

Actual result 1: When user clicks on star, star becomes full colour to favourite and outline only if not favourite.
Actual result 2: Number beside favourites star is updated

Pass/Fail: Pass

  * As a logged-in user I can review a recipe so that I can interact with the site (must-have / complete)(#32)

Testing Steps:
1. Navigate to the website of [favoureats](https://favoureats.herokuapp.com/)
2. Login to the website
3. Click on the 'recipes' link in the navigation menu
4. Click on the title of a recipe to open the full recipe detail page with review form
5. Enter content in the review box and click 'submit'

Expected result: Thankyou message displays thanking user for submitting a review. 'Your review is pending approval'. Review appears as draft in admin panel list of reviews.

Actual result: Thankyou message displays thanking user for submitting a review. 'Your review is pending approval'. Review appears as draft in admin panel list of reviews.

Pass/Fail: Pass

## Testing Features

### Navigation
- check that all navigation links work as expected

Testing Steps:
1. Navigate to [favoureats](https://favoureats.herokuapp.com/)
2. Without logging in click on the links in the navbar
3. Login and click the links in the navbar
4. Scroll down the page

Expected Results
1. Not logged in user can view links to Home, About, Recipes, Register and Sign In
2. Each of these links opens the expected page
3. Logged in user can view links to Home, About, Recipes, My Recipes and Sign Out
4. Each of these links opens the expected page
5. Active page is highlighted in each case
6. Navbar remains in view when scrolling

Actual Result
1. Not logged in user can view links to Home, About, Recipes, Register and Sign In
2. Each of these links opens the expected page
3. Logged in user can view links to Home, About, Recipes, My Recipes and Sign Out
4. Each of these links opens the expected page
5. Active page is highlighted in each case
6. Navbar remains in view when scrolling

![](documentation/screenshots/nav1.png)

  ![](documentation/screenshots/nav2.png)

![](documentation/screenshots/nav3.png)

![](documentation/screenshots/sticky_nav.png)

Pass/Fail: Pass

### Logo

- check that logo links back to the home page:

Testing Steps:
1. Open each page and click on logo

Expected Result
- logo links back to home page from each page

Actual result
- logo links back to home page from each page

Pass/Fail: Pass

![Logo](documentation/screenshots/logo_screenshot.png)


### Footer
- check that social media links direct the user to the correct website of Facebook, Instagram and Twitter pages

Testing Steps

1. Click on each icon


Expected result
1. Each icon opens on a separate tab to its corresponding social media website

Actual Result
1. Each icon opens on a separate tab to its corresponding social media website

Pass/Fail: Pass

### Home Page
### Register Button

* Check that hero register button on hero image is not visible when user is signed in and that the register link navigates to the sign up page

Testing Steps
1. Navigate to [favoureats](https://favoureats.herokuapp.com/)
2. Without logging in look at the hero image
3. Click on the register button
4. Login and view the hero image

Expected Results
1. Register button is visible to not logged in users
2. Register button is not visible when user is loged in
3. Register button links to sign up page

Actual Results
1. Register button is visible to not logged in users
2. Register button is not visible when user is loged in
3. Register button links to sign up page

Pass/Fail: Pass

![](documentation/screenshots/navbar_no_log.png)
*View to not signed in user*

![](documentation/screenshots/navbar_log.png)
*View to signed in user*

### Recipes/My Recipes text links
* Check that links in Latest Recipes text direct users to correct page. Recipes page link goes to Recipes page and My Recipes link takes not logged in users to Sign In page and logged in users to My Recipes page

Testing Steps
1. Click on links without logging in
2. Click on links after logging in

Expected results
1. Both users ar directed to Recipes Page
2. Only logged in user can open My Recipes page while not logged in user is directed to Sign In page

Acctual results
1. Both users ar directed to Recipes Page
2. Only logged in user can open My Recipes page while not logged in user is directed to Sign In page

Pass/Fail: Pass

![](documentation/screenshots/latest.png)
*Latest recipe information*


### Snapshot images
- check that images are of three most recent recipe posts with title, date added and author. 

Testing Steps
1. Log in to admin panel
2. Check list of recipes
3. Check that the three images correspond to the most recent recipe additions

Expected Result:
1. The three recipes are the most recent additions and the most recent is first

Actual Result:
1. The three recipes are the most recent additions and the most recent is first

Pass/Fail: Pass

![](documentation/screenshots/snapshot.png)
*Three latest recipes*


### View the Recipes button
* Check that the 'View the Recipes' button links to Recipes page

Testing Steps
1. Click on the View the Recipes button

Expected Result
1. When button is clicked the user is redirected to the Recipes page

Pass/Fail: Pass

![](documentation/screenshots/view_btn.png)
*View the Recipes button*






















- The navbar collapses for mobile and portrait tablets:

![](documentation/screenshots/nav_coll.png)
*Navbar collapsed*



## Code Validation
## HTML Validation
HTML was validated by [The WEC Markup Validation Service](https://validator.w3.org/)
No errors or warnings were found:

[Home Page](https://validator.w3.org/nu/?doc=https://favoureats.herokuapp.com/)

[About Page](https://validator.w3.org/nu/?doc=https://favoureats.herokuapp.com/about/)

[Recipes Page](https://validator.w3.org/nu/?doc=https://favoureats.herokuapp.com/recipes/)

[My Recipes Page](https://validator.w3.org/nu/?doc=https://favoureats.herokuapp.com/myrecipes/)

[Register Page]()
https://validator.w3.org/nu/?doc=https://favoureats.herokuapp.com/accounts/signup/

[Login Page](https://validator.w3.org/nu/?doc=https://favoureats.herokuapp.com/accounts/login/)


[Logout Page](https://validator.w3.org/nu/?doc=https://favoureats.herokuapp.com/accounts/logout/)




## CSS Validation

## Browser compatibility
## Responsiveness

## Bugs here ????