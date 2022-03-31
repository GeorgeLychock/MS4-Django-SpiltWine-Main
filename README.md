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
Spilt Wine is an ecommerce website that sells wines, wine accessories, and culinary items. The user has access to a shopping cart which keeps track of their cart items and displays their current purchase costs as they view products and navigate the site. The user can purchase the items with a credit card and will receive an email verification of their purchase. The site will display a detailed view of each product where the user can add the item to their cart, or if logged in and if the item is a wine, can add the wine item to their virtual wine cellar (Cellar). The Cellar is a custom application that keeps the user's information on the wines they add to their Cellar which can be viewed by logging in when the user returns to the site. The Cellar gives the user the ability to update the quantity of the item or remove the item from their Cellar. The Cellar displays useful statistics on the items they have added, including: Total value,total number of items, # of varietals, a list of varietals, a progress bar showing the number of varietals (out of a total of 180) contained in their Cellar, etc. All content and functionality are available on any size device.

> ### Important Notes
>
>-  The primary focus of this project is to display Django, Python, and database skills learned in the Full Stack Frameworks with Django module of the Salem State University / Code Institute Full Stack Software Developer Certificate Program.
>-  The cart, profile, and checkout apps' code is almost entirely from Code Institute's module "Full Stack Frameworks with Django". The largest change I made to these apps was to delete much of the product sizes code since my product array does not require it. I also made updates such as styling, changing the HTML amd CSS to Bootstrap 5.1 framework, and removing the reverse() methods from views rendering.
>-  Because I'm working on a local dev machine, and not GitPod, I could not finish the webhooks developement and testing until I had the project deployed. (Although I figured out afterwards that I had to install and use the Stripe CLI to perform webhook testing on my local env anyway)
>-  The custom app Cellar is the primary focus on my project although the base website is a fully functioning ecommerce site based on the curricullum mini project.
>-  


<a name="US"></a>

## User Stories

>-  I used the User Story list shown in the CI curriculum as a template:
>-  User Story List  - [View](_documentation/product_specs/MS4 User Stories - v1.pdf)

-   ### Anonymous AND Logged In User Experience
    -   #### **Story 1** As a Site Visitor, I want to be able to search recipes by using a quick search method.
        -  #### *Acceptance Criteria* -- Duplicated in Testing Section
            1.  A search form is presented without leaving the home page
            2.  A minimal number of search criteria is presented to choose from
            3.  When the form is submitted, user is redirected to the advanced search page and presented the results list/table

<a name="REQS"></a>
## Requirements
(Alignments to User Stories are in paratheses)
-   Application must be responsive and fully functional to use on any device
-   Allow users to search products
-   Allow users to log in and log out of the app
-   Logging in provides user with feature to rate a product
-   Logging in provides a site admin with feature to build a product
-   Allow users to view details about the product including an image

<a name="BACKLOG"></a>
## Future Requirements
(Alignments to User Stories are in paratheses, if available)
-   Include a weather indicator on the home page
-   Allow users to view top 5 rated products
-   Allow Users to choose an avatar from a pallet of avatars for their profile

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