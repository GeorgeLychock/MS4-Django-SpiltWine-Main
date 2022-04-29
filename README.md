# George Lychock - MS4 Project: Spilt Wine
### Salem State University Fullstack Software Developer Certificate
#### MS4 Django Spilt Wine
-   [View Live Dev Site](https://ms4-spiltwine.herokuapp.com/)

<hr>

<h1 align="center"><img src="_documentation/montage.png" /></h1>

## Table of Contents

- [Use Case](#UC)
    - [User Stories](#US)
    - [Requirements](#REQS)
    - [Backlog (Future Requirements)](#BACKLOG)
- [UI/UX](#UXUI)
    - [UI](#UI)
        -   [Wireframes](#UIWF)
    - [UX - Design](#DES)
        -   [Wireframes](#UXWF)
- [Technical Background](#TECH)
- [Testing](TESTRM.md)
- [Known/Resolved Issues](#ISSUES)
- [Product/Project Management](#PROJ)
- [Deployment](#DPLY)
- [Credits](#CREDS)

<a name="UC"></a>
# Use Case
Spilt Wine is an ecommerce website that sells wines, wine accessories, and culinary items. The user has access to a shopping cart which keeps track of their cart items and displays their current purchase costs as they view products and navigate the site. The user can purchase the items with a credit card and will receive an email verification of their purchase. The site will display a detailed view of each product where the user can add the item to their cart, or if logged in and if the item is a wine, can add the wine item to their virtual wine cellar (Cellar). The Cellar is a custom application that keeps the user's information on the wines they add to their Cellar which can be viewed by logging in when the user returns to the site. The Cellar gives the user the ability to update the quantity of the item or remove the item from their Cellar. The Cellar displays useful statistics on the items they have added, including: Total value ,total number of items, # of varietals, a list of varietals, a progress bar showing the number of varietals (out of a total of 180) contained in their Cellar, etc. All content and functionality are available on any size device.

> ### Important Notes
>
>-  The primary focus of this project is to display Django, Python, and database skills learned in the Full Stack Frameworks with Django module of the Salem State University / Code Institute Full Stack Software Developer Certificate Program.
>-  The cart, profile, and checkout apps' code is almost entirely from Code Institute's module "Full Stack Frameworks with Django". The largest change I made to these apps was to delete much of the product sizes code since my product array does not require it. I also made updates such as styling, changing the HTML amd CSS to Bootstrap 5.1 framework, and removing the reverse() methods from views rendering.
>-  Because I'm working on a local dev machine, and not GitPod, I could not finish the webhooks developement and testing until I had the project deployed. (Although I figured out afterwards that I had to install and use the Stripe CLI to perform webhook testing on my local env anyway)
>-  The custom app Cellar is the primary focus on my project although the base website is a fully functioning ecommerce site based on the curricullum mini project.
>-  All user directed messages are displayed in a custom format, as opposed to Toasts, to have more control on position and to understand messages in Django and Python
>-  Wine Accessories and Culinary products currently exist as placeholders, no product editing or sorting can be performed on products in those categories at present. All CRUD actions can be performed on wine products.


<a name="US"></a>

## User Stories

>-  I used the User Story list shown in the CI curriculum as a template:
>-  User Story List  - [View PDF](_documentation/product_specs/MS4_User_Stories_v1.pdf)
>-  Full User Story detail is provided below but only for truly custom apps and any app I customized heavily.
>-  The lists above contain all user stories that were used to test the deployed project.
>-  I decided to track most of the user stories as a spreasheet given the number of stories and ease of import into a work tracking app (such as Jira) in the future if I so chose.

All Acceptance Criteria Results can be found in [TESTRM.md](TESTRM.md)

-   ### Visitor/Shopper
    -   #### **Story V-1** As a Visitor/Shopper I want to be able to view a list of products so that I can select a product to purchase.
        -  #### *Acceptance Criteria*
            1.  A list of product categories is presented
            2.  Category links present user with category product listings
            3.  Product listings and featured sidebars should display as product cards displaying: product name, varietal (for wines), product image, price, a truncated description, origin of wine (for wines)
            4.  Product image and name should link to product detail page (described below)

    -   #### **Story V-2** As a Visitor/Shopper I want to be able to view individual product details so that I can determine a product description, image, and product info.
        -  #### *Acceptance Criteria*
            1.  Product details view should be accessible from all product listings, featured sidebars, product summaries (eg in the Cart or Cellar summaries), and search results summaries
            2.  The wine detail view should present all of the following information: vintage, product name, brand, varietal, product image, price, a full description, origin of wine, size, units for size, wine type, body, ABV, style
            3.  Present an Add to Cart option, for all users
            4.  Present an Add to Cellar option, for authenticated users
            5.  Present an Edit and Delete option, for admin authenticated users

    -   #### **Story V-3** As a Visitor/Shopper I want to be able to view any featured items so that I can view product(s) the company feels are of particular interest of me.
        -  #### *Acceptance Criteria*
            1.  A Featured Items panel/section is presented on any product category view
            2.  Featured items should present a product's name, image, varietal (for wine products), price, and origin (for wine products)
            3.  The featured product image and title should be linked to the product's detail page

    -   #### **Story S-1** As a Visitor/Shopper I want to be able to sort a list of products by price, name, country/state, or varietal so that I can view products more similar to what I'm looking for.
        -  #### *Acceptance Criteria*
            1.  A dropdown is presented in the main menu for the user to sort products by name (all products in alpha order), price, country/state, and varietal (for wine products)
            2.  A dropdown is presented in the product category listings for the user to sort products by name (all products in alpha order), price, country/state, and varietal (for wine products)

-   ### Authenticated User
    -   #### **Story C-1** As a/an Logged In User I want to be able to add, update, or delete wines from a personal library so that I can see a listing of all the wine I have in my wine collection.
        -  #### *Acceptance Criteria*
            1.  An Add to Cellar option is presented to authenticated users on the wine details view and redirects user to the add to cellar view, or, if the item is already in the cellar redirects to the update cellar view
            2.  The option adds/updates the wine to the user's cellar, confirms an item has been added/updated, then redirects to the user's cellar
            3.  A Cellar icon is presented to all users in a menu panel on all main views which directs the user to their cellar view
            4.  Clicking Cellar icon: Authenticated users are directed to their personal cellar view
            5.  Clicking Cellar icon: Unauthenticated users are directed to the login page
            6.  The Cellar view displays a message if the cellar is empty
            7.  A list of saved cellar items is presented if items have been added to the user's cellar. The list displays the product image, name, vintage, SKU, price, quantity on-hand in cellar, and subtotal value of each cellar item
            8.  The quantity on-hand field displays the current quantity of the item in the user's cellar and is editable; quantity can be updated
            9.  Update is confirmed
            10.  The item can be removed from the Cellar

    -   #### **Story C-2** As a/an Logged In User I want to be able to view metrics of my wine library so that I can understand the make up of my wine collection.
        -  #### *Acceptance Criteria*
            1.  A cellar statistics panel is displayed to the user displaying the following information based on the wines in the user's cellar:
            >- Cellar Value
            >- Number of items in the cellar
            >- Number of varietals in the cellar
            >- A list of the different varietals represented in the cellar

-   ### Administrator
    -   #### **Story A-1** As an Administrator I want to be able to add and delete wine products in the wine product database so that I can provide access to their information throughout the website.
        -  #### *Acceptance Criteria*
            1.  A link to a wine product management option should be presented on the user menu dropdown for all users with editing rights or admin privileges.
            2.  The option should present the user with a method to add a new product
            3.  The method should present a form that allows the user to input all required and optional data for the product
                -   Included fields for wine products (*required fields): *product name, vintage, brand, SKU, featured option, product image, product image url, has sizes option, *size, measure, price, *a full description, *country or state origin, region origin, appellation origin, *wine type, *varietal, *body, *style, ABV, taste field
            4.  Upon clicking, an Add Product submit button should inform the user the product data has been saved and redirect the user to the new product's detail view
            5.  Product information is added correctly
            6.  A link to delete a wine product should be presented on the wine product details view for all users with editing rights or admin privileges
            7.  A confirmation method should be presented to the admin to confirm product deletion
            8.  User is returned to the product category view when user confirms deletion
            9.  Message is displayed indicating the product was deleted successfully

    -   #### **Story A-2** As an Administrator I want to be able to update wine products in the wine product database so that I can provide access to their information throughout the website.
        -  #### *Acceptance Criteria*
            1.  A link to a Product Update view should be presented on the wine product details view for all users with editing rights or admin privileges.
            2.  Once at Product Update, a message indicating what product is being edited should be present
            3.  The Product Update view should contain all the following fields (read only fields are indicated, otherwise all fields can be edited): product name, vintage, brand, SKU, featured option, product image, product image url, has sizes option, size, measure, price, a full description, country or state origin, region origin, appellation origin, wine type, varietal, body, style, ABV, taste field
            4.  Product information is updated correctly when I submit changes
            5.  User is returned to the product detail page when changes are submitted
            6.  Message is displayed indicating save was completed successfully



    -   #### **Story Template** As an Administrator I want to be able to add, update, and delete products in the product database so that I am able to access their information through the website.
        -  #### *Acceptance Criteria*
            1.  How do I get there?
            2.  What messaging does the user get when they arrive?
            3.  What's it do when I get there?
            4.  What messaging does the user get when they are there?
            5.  How do I get out of there?
            6.  What messaging does the user get when they leave?
            


<a name="REQS"></a>
## Requirements
(Alignments to User Stories are in paratheses)
-   Application must be responsive and fully functional to use on any device
-   Allow users to search products
-   Allow users to log in and log out of the app
-   Logging in provides a site admin with feature to build a product
-   Allow users to view details about the product including an image
-   Provide a logged in user or anonymous user with feature to buy a product

<a name="BACKLOG"></a>
## Future Requirements
(Alignments to User Stories are in paratheses, if available)
-   Include a weather indicator on the home page
-   Allow users to view top 5 rated products
-   Allow Users to choose an avatar from a pallet of avatars for their profile
-   Create a product management view giving the admin options for creating/editing/deleting products
-   Currently, when an admin deletes a wine from the database the JS redirects to the generic all wines listing. This should be changed when a product management view is available. That view should be sent a flag that then creates a confirm message that the wine has been successfully deleted from the db.

# UX/UI
-   ## UI
    <a name="UI"></a>
    -   ### Wireframes
        <a name="UIWF"></a>
        -   UI Map (Site Map aligned to data structures and functions) - [View](https://github.com/GeorgeLychock/MS3-Project-Python-uSpice/blob/master/_documentation/ui/Site-UI-Map-.jpg)
    -   ### Sprints
        -   UI Sprint Map - [View](https://github.com/GeorgeLychock/MS3-Project-Python-uSpice/blob/master/_documentation/ui/Site-UI-Sprints-.jpg)


-   ## UX - Design
    <a name="DES"></a>
    -   ### Wireframes
        <a name="UXWF"></a>
        -   Home Page - Desktop and Tablet Wireframe - [View](_documentation/wireframes/spiltwine-wireframe-desktop-home.jpg)
        -   Home Page - Mobile Wireframe - [View](_documentation/wireframes/spiltwine-wireframe-mobile-home.jpg)


<a name="TECH"></a>
# Technical Background
## Features and Logic
-   The app uses custom Javascript and localStorage for the add ingredient functionality on the Build Recipe and Edit Recipe pages
-   The app uses custom Javascript and localStorage for the nav click path arrows functionality
## Sitemap, UI, and Data Structures
-   UI Sitemap  - [View](https://github.com/GeorgeLychock/MS3-Project-Python-uSpice/blob/master/_documentation/ui/Site-UI-Map-.jpg)
-   Sprints  - [View](https://github.com/GeorgeLychock/MS3-Project-Python-uSpice/blob/master/_documentation/ui/Site-UI-Sprints-.jpg)
-   Data Structures  - [View](https://github.com/GeorgeLychock/MS3-Project-Python-uSpice/blob/master/_documentation/ui/uspice-data-structures.jpg)

## Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JavaScript](https://www.javascript.com/)
-   [Python3](https://www.python.org/)

## Frameworks, Libraries, & Programs Used
1. [Bootstrap 5.1:](https://getbootstrap.com/docs/5.1/getting-started/introduction/)
    - Bootstrap was used to assist with the responsiveness and styling of the website.
2. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the 'Montserrat' and 'Raleway' fonts into the style.css file which is used on all pages throughout the project.
3. [Bootstrap Icons:](https://icons.getbootstrap.com/)
    - Bootstrap Icons was used for all app icons
4. [jQuery:](https://jquery.com/)
    - jQuery came with Bootstrap and is used in custom JS.
5. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing Visual Studio on my Linux laptop to commit to Git and Push to GitHub.
6. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
7. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used for a few of the icons where I did not like the Bootstrap versions or BS did not have a suitable icon.
9.  [draw.io](https://app.diagrams.net/)
    - Wireframing tool
10. [Inkscape](https://inkscape.org/)
    - Drawing app used for logo design
11. [Flaticons](https://www.flaticon.com/authors/flat-icons)
    - Avatar images

### Resources Used
-   [MDN General Web Docs: ](https://developer.mozilla.org/) For semantic structure reference, arrays, localStorage, fetch.
-   [W3Schools.com](https://www.w3schools.com/), For Color Picker, html/css/js general refernece, semantic structure reference, arrays, localStorage.
https://www.djangoproject.com/
-   [For Loop Examples from pythonguides.com:](pythonguides.com/python-for-loop-index/)
-   [Changing the port setting for Django](https://pythonistaplanet.com/how-to-change-the-default-runserver-port-in-django/) I needed to change the port since I'm running my own dev environment and not GitPod
-   [Field data types for Django Models](https://www.geeksforgeeks.org/django-model-data-types-and-fields-list/#:~:text=Basic%20model%20data%20types%20and%20fields%20list%20,raw%20binary%20data.%20%2021%20more%20rows%20)
-   [Migrating Data using fixtures Django](https://www.bing.com/videos/search?q=creating+django+fixtures+from+csv&view=detail&mid=21A1F428ED88293C96F021A1F428ED88293C96F0&FORM=VIRE) Instructions on how to convert csv to fixture JSON and migrate to Django

Django Tutorial https://www.geeksforgeeks.org/django-tutorial/?ref=gcse

Django Project
-   [DjangoProject Queries Documentation](https://docs.djangoproject.com/en/4.0/topics/db/queries/)
-   https://docs.djangoproject.com/en/4.0/topics/db/models/#model-inheritance

Primary Key Best Practices https://stackoverflow.com/questions/337503/whats-the-best-practice-for-primary-keys-in-tables#:~:text=Primary%20keys%20should%20be%20as%20small%20as%20necessary

JSON Convertor https://www.convertcsv.com/csv-to-json.htm

django-countries https://pypi.org/project/django-countries/#show-certain-countries-first

https://medium.com/swlh/how-to-style-your-django-forms-7e8463aae4fa

#   Testing
<a name="TESTING"></a>
-   [See Test ReadMe File](TESTRM.md)

#   Known/Resolved Issues
<a name="ISSUES"></a>
-   [See Test ReadMe File](TESTRM.md)

<a name="CREDS"></a>
# Credits
## Code Credits
-   Model class methods are borrowed from Code Institute code provided in the Bontique Ado Project for the Full Stack Software Developer curriculum.
-   html/css: Recreated the Home page using the Code Institute code provided in the Bontique Ado Project for the Full Stack Software Developer curriculum as a template. I changed the markup and styles for Bootstrap 5.1 and consolidated a number of the core BS styles into custom style groups. https://codeinstitute.net/global/
-   <!-- Cart Form from Code Institute, Django Module https://codeinstitute.net/global/ -->
-   RegEx input patterns from W3Schools - https://www.w3schools.com/tags/att_input_pattern.asp
-   Avatar Icons made by [Flaticon](https://www.flaticon.com/)
-   The localStorage check code in script.js is from [MDN - Using_the_Web_Storage_API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API/Using_the_Web_Storage_API). This code checks to make sure that the browser can support localStorage and has it turned on. Find code use indicated by "CODE REUSE - localStorage Check "