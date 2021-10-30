# Automated Testing
## Set-up for testing in local environment
## Unittest
Unittest was used to test the correct template was rendered
# Manual Testing
## Testing User Stories
#### Epic: Set up admin page for admin to manage recipe posts, reviews and site users
#### User Stories:
  * As a site admin I can create draft recipe posts so that I can complete the recipes later (must-have / complete)(#8)

  Description: The site administrator is able to create draft recipes.

  Testing Steps:
  1. Navigate to the website of [favoureats](https://favoureats.herokuapp.com/)
  2. Click on the 'Sign In' tab on the navigation menu bar
  3. Sign in with admin's name and password
  4. Navigate to [admin page](https://favoureats.herokuapp.com/admin/)
  5. In the admin panel menu beside recipes click the add button
  6. In the recipe form enter content in the fields
  7. Click save to save the created recipe
 

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
  1. Navigate to the website of [favoureats](https://favoureats.herokuapp.com/)
  2. Click on the 'Sign In' tab on the navigation menu bar
  3. Sign in with admin's name and password
  4. Navigate to [admin page](https://favoureats.herokuapp.com/admin/)
  5. In the admin panel menu beside recipes click the add button
  6. In the recipe form enter content in the fields
  7. Change the status to published from the status dropdown menu
  8. Click save to save the created recipe

Expected result: The recipe is saved as 'published' to the list of recipes in the admin panel. The recipe is viewable on the website
Actual result: The recipe is saved as 'published' to the list of recipes in the admin panel. The recipe is viewable on the website
Pass/Fail: Pass

To read/update a recipe:

1. Navigate to the website of [favoureats](https://favoureats.herokuapp.com/)
2. Click on the 'Sign In' tab on the navigation menu bar
3. Sign in with admin's name and password
4. In the admin panel on[admin page](https://favoureats.herokuapp.com/admin/) select recipes to view a list of draft and published recipes
5. In the list select a recipe title to read the full recipe
6. To update the recipe update the necessary fields and click save

Expected result: The viewed/updated recipe is saved to the list of recipes
Actual result: The viewed/updated recipe is saved to the list of recipes
Pass/Fail: Pass

To delete a recipe:
1. Navigate to the website of [favoureats](https://favoureats.herokuapp.com/)
2. Click on the 'Sign In' tab on the navigation menu bar
3. Sign in with admin's name and password
4. In the admin panel on [admin page](https://favoureats.herokuapp.com/admin/) select recipes to view a list of draft and published recipes
5. From the list select the recipe to be deleted in the checkbox beside the title
6. In the action dropdown menu above the list select 'delete' and 'go' to delete the recipe

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
1. Navigate to the website of [favoureats](https://favoureats.herokuapp.com/)
2. Click on the 'Sign In' tab on the navigation menu bar
3. Sign in with admin's name and password
4. In the admin panel on [admin page](https://favoureats.herokuapp.com/admin/) select reviews to view a list of draft and published reviews
5. In the list select a review in the checkbox
6. In the action dropdown menu above the list select 'approve selected review' or 'delete selected review' and then 'go'

Expected result: The approved review is published on the website
Expected result: The deleted review is removed from the list of reviews
Actual result: The approved review is published on the website
Actual result: The deleted review is removed from the list of reviews
Pass/Fail: Pass

* As an admin I can view the number of favourites on a recipe post so that I can know which are the most popular(#28)
* As an admin I can view reviews of a recipe post so that I can read the commentary on a recipe(#29)
* As an admin I can create reviews of recipe posts so that I can generate discussion on recipe posts(#31)
## Testing Features
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