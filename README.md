[![Build Status](https://travis-ci.org/ivarsaris/dutchtreats.svg?branch=master)](https://travis-ci.org/ivarsaris/dutchtreats)

# Dutchtreats

**E-commerce App - Fourth milestone project; Full stack frameworks with Django - Code Institute**

Dutchtreats is a web application where users can buy typical Dutch foods online and have it delivered
at home. Users can create and update a profile, find information about the products, write reviews, 
add items to a cart, and pay for these items using [Stripe](https://stripe.com/). Users can also
learn about the company on the about page and get in contact with Dutchtreats using a contact form. 

As a Dutchman who travels a lot, sometimes I miss Dutch foods. I love to try new foods and enjoy local cuisine.
However, sometimes I wish I could get my hands on some Dutch foods wherever I am. This inspired me to build this 
web application.

The web application was made for educational purposes only, it's not a real web shop.

## Demo

[Live website](https://dutchtreats.herokuapp.com/). The application is hosted on [Heroku](https://www.heroku.com/home) and uses a 
Heroku Postgress database.

![Responsive page](https://dutchtreats.s3.eu-west-3.amazonaws.com/media/images/dutchtreats-responsive.png)

## UX

#### User stories

I started by creating [user stories](userstories.md) to help determine what features to add to the website.

1. Strategy

Dutchtreats was created for people who don't have access to Dutch foods where they live. The Netherlands has several delicacies
that are delicious and (almost) only available in The Netherlands. Dutch expats working in other countries, or others
who have stayed in The Netherlands and are back home can now order these foods online and have them delivered to their home.

2. Scope

The user can use the Dutchtreats website to order Dutch foods. The following pages and functions are part of the application.

##### Home
Gives an introduction to the website and calls for action from the user to order products.

##### Registration
User can create an account with their Email address. This page is only accessible if no user is logged in.

##### Login 
User can log in to their account. This page is only accessible if no user is logged in.

##### Profile
User can see an overview of their personal information. The user can change their username, profile picture or Email address. 
This page is only accessible if a user is logged in.

##### Products
This page has an overview of all products. The user can search for a specific product with a search form. The user can add products
straight to their cart from the products page. This is only possible if a user is logged in. The user can also click on a product and
open this product's page.

##### Single product
This page gives a more extensive overview of the product. This includes the name, price, a picture, a description, and reviews other users
have written about this product. The user can add products to their cart from the product page. The user can also write a review about the product.
Writing a review and adding a product to cart is only possible if a user is logged in.

##### Cart
The cart page gives an overview of all the products the user has added to their cart. It gives the picture, name, price, amount added to cart,
and total price. The user can change the amount of any product they added to their cart. 
The page also gives the total price of all products and a checkout button that links to the checkout page.

##### Checkout
The checkout page gives a small overview of the products the user will buy. The user can checkout using the checkout form. 
Here, the user needs to input their personal information and Credit Card information. Stripe Credit Card payment processing is used
for the payments.

##### Contact
The user can use the contact page to get in touch with Dutchtreats. the user can fill out a form to send a message to Dutchtreats with 
any questions, suggestions or feedback.

The structure, skeleton and surface is too much to discuss here. All elements were thought through with the user experience in mind.

### Mockup

I created a [mockup](https://ivarsaris.wixsite.com/dutchtreats) using Wix. I did this in order to determine how to style the website and play around with
the layout. I designed the mockup both for desktop and mobile. For some reason, the mockup is only responsive to mobile on an actual mobile device,
not on a mobile screen in Chrome devtools. I don't know why.

### Design

In terms of the color scheme, the Dutch colors were chosen. Orange is the national color, and the Dutch flag is 
red, white, and blue. These colors come back all throughout the application. The search function has a yellow and
a red button. As you know, red and yellow together form orange. The products and meet the team columns have an orange background color. 
I choose to add this because I felt the application was a little too white.

I choose "Allan" as font for the title. This because I think it's beautiful and attracts attention. I choose "Cabin" as font for the rest 
of the web application. This because it's easy to read and looks modern but classy.

I started with a [bootstrap snippet](https://getbootstrap.com/docs/4.0/components/navbar/) for a navbar with collapsible nav-items. The web application has many pages. 
In order to keep the navbar uncluttered, I choose to hide the login and registration page
when the user is logged in. And the profile and cart link are hidden when there's no user logged in. The navbar collapses the products,
about, and contact pages on screens smaller than large. The other links are displayed, because they're short and consist mostly of icons.
These don't take up a lot of space, so they can be displayed on smaller screens.

The footer is simple and clean. On smaller screens, the font size of the text is smaller so the footer doesn't take up too much
of a smaller screen's space.

I choose to place all forms(login, registration, review, and contact) in the center of the screen. This because these forms are the most
important parts of their respective pages. Putting them in the center makes sure the attention goes straight to the form.

I made sure users could easily navigate back and forth between pages that make sense. For example, clicking on product in the product page 
opens the single product page. On this single product page, there's a button right underneath the heading that redirects back to the products
page. The same goes for the cart and checkout pages. Under the order in the cart there's a button that navigates to the checkout page, and underneath
the header in the checkout page, there's a button that redirects back to the cart page. This goes for the registration and login page as well. The
user doesn't have to go to the navbar to navigate between these pages.

Whenever there's a message to be displayed for the user, it is displayed on top of the page right underneath the navbar. The text is orange and is shown 
in a black strip. I choose this because it attracts attention and the user sees the message immediately.

## Technologies used

The web application has been made using the following technologies:

* **Gitpod** - Online development environment for GitHub
* **HTML5** - Coding language used for creating the content and structure of the website
* **CSS** - Coding language used for styling the content
* **Python3** - Dynamic, object oriented programming language
* **Django** - Open source Python framework used for building web applications
* **JavaScript** - Used for creating functions which add interactivity to the application
* **MongoDB** - Online open source document oriented database
* **Google Chrome** - Used as browser and for developer tools
* [**Materialize**](https://materializecss.com/) - Framework library used for display, styling and icons
* **Git** - Used for version control
* [**GitHub**](https://github.com/) - Used to host the repository for the application
* [**Heroku**](https://www.heroku.com/) - Used to deploy the application
* **Heroku Postgress** - SQL database from Heroku

## Development process

I made the backend functionalities before I created the styling. When I added the styling and the content, I ran into some bugs in the
backend. I fixed these along the way.

I started with the [Code Institute template](https://github.com/Code-Institute-Org/gitpod-full-template) for working in Gitpod. I created a 
repository in GitHub and linked this to the template. When I created most functionalities, I deployed the application to Heroku and deployed
Travis continuous integration. I had debug=True throughout working on the project. I switched this to debug=False upon final deployment in order to 
make sure no sensitive data can be retrieved. Throughout the development process, I had the necessary environment variables set in the env.py file.
I added this file to the .gitignore file so the sensitive variables wouldn't be uploaded the GitHub. I added the same environment variables to 
Heroku.

I made this application in two time phases. There was significant time between the two phases. I had forgotten quite a bit about how Django works
and I spent some time figuring it out again. In this time, I stupidly added several secret keys to my settings file and committed them to GitHub. 
Thankfully I realized my mistake and changed all keys and disabled the ones I committed to GitHub. Now, no keys that can be found in any commit 
are useable.

## Testing

I manually tested all functions in all apps. I did this to ensure all functions were working properly. For a while, the functionality stored
admin as the user who wrote any review, no matter who is logged in. The problem here was an error in the template language. Another issue that 
came up was because I created the profile functionality after I created the superuser(Admin). So Admin didn't have a profile, and when I tried to
render the profile page when logged in as Admin, it returned an error. I simply created a new superuser to fix this issue.

To test the Stripe payment method, you can use the Stripe test card information. Use credit card number 4242424242424242 with any CVC code and an expiry
month in the future and the(fictional) payment should go through. I tested it several times myself and the payments all went through and show up on the Stripe dashboard:

![Stripe dashboard](https://dutchtreats.s3.eu-west-3.amazonaws.com/media/images/stripe-payments.png)

when entering wrong credit card information, the application should return a message to the user indicating what went wrong. However, this doesn't happen. I wrote 
the functionality for this but it's not coming through. I'm not sure why or how to fix this.

### Responsiveness

I tested the application on several devices. I tested on an HP laptop, a MacBook, a Microsoft Surface laptop, an iPad an iPhone 6, 7, and 10, an Honor 10 and a Samsung
Galaxy s9. The application was responsive and worked well on all devices. I also ran the application through https://responsivedesignchecker.com/ and checked many different devices. 
This to make sure the application looks good on all of them. I ensured the application looks good on all devices from 320px width(smallest mobile device) and up. 

### Browser compatibility

I tried the application on several browsers. The application worked well on Google Chrome, Safari and Mozilla Firefox.
However, there was one issue in Internet Explorer and Microsoft Edge. The soft orange background color I uses for the product and meet the team columns doesn't come through. I'm not sure
how to fix this.

### Code validation

I ran the code through several validators to make sure there are no mistakes. The HTML validators don't take Django template language into account, so several errors were returned. 
I checked them and these were not mistakes.

**HTML5**

https://validator.w3.org/

https://html5.validator.nu/

**CSS**

https://codebeautify.org/cssvalidate

https://jigsaw.w3.org/css-validator/

**Python**

https://extendsclass.com/python-tester.html

http://pep8online.com/

## Features

The application has several features, not all are accessible to everyone. The following features are accessible to the following users:

**Anyone** 
- See the webpage
- find products
- Read reviews 
- Fill out the contact form. 

**Logged in user**
- Add products to their cart
- Buy the products through the checkout page
- Write a product review
- Delete a review they wrote
- Visit their profile page
- Make changes to their profile

**Admin**
- Access the admin panel
- Make changes to and delete products
- Make changes to user profiles
- Make changes to and delete reviews
- Access the overview of all orders placed

### Features left to implement

The first feature I would like to implement is some kind of functionality to keep track of stock. If a delivery comes in, Admin can add these to the stock
and when a customer buys a product, it gets taken out. So Admin always has an overview of the amount of all products in stock. Also, when a product is sold out, 
it doesn't show in the products page any more. So a user isn't disappointed when they buy something but it can't be delivered. 

Another feature I would like to implement is a star rating system for the products. A user can give a rating to a product, and the average rating of a product is
calculated and displayed. So users can see if others like a product or not. 

Also I would like to add some kind of pagination to the products and the reviews. When the inventory grows and more products are added, they will all displayed
in one page as it stands now. This could cause a very long products page. Adding pagination would make it look neater. The same goes for reviews. A user would
see the last 10 reviews. If they want to load more, that's possible. But by default, only the last 10 are shown.

I would also like to make a more elaborate profile page. Currently, the user can only add their username, e-mail and upload a picture. I would like to add
their address and credit card information as well. So when a user goes to their cart, this information is already filled out. The user doesn't need to fill
out the checkout form every time.

## Installation

The application is deployed in Heroku. To get the app running locally, follow these steps:

1. Set up a workspace in your development environment
2. Clone the app from my GitHub repository with the following command: git clone https://github.com/ivarsaris/dutchtreats
3. Change the directory with the following command: cd dutchtreats
4. Install the required installations with the following command: sudo pip3 install -r requirements.txt
5. Obtain your own secret keys for AWS S3, Stripe, and Heroku Postgress. Put them in a file call env.py in the root directory. 
Put "import env" on line 2 of your settings file. 
6. Set DEBUG = True in line 16 of your settings file. 
7. Save the file, and run it in the terminal with the following command: python3 manage.py
Now your app is running locally

## Credits

### Content 

All content was written by me.

### Media 

I got the images from google. I choose images with no brand or company information. I don't own the copyright to any of the images.
The application was made for educational purposes only. No copyright infringement was intended. 

### Acknowledgements

I took a navbar snippet from Bootstrap and adapted it to fit the application.

I followed the [Django tutorial from Corey Schafer](https://www.youtube.com/watch?v=FdVuKt_iuSI&t=504s) on YouTube for the create profile functionality. I adapted the code and styling to fit the
application.

I want to thank my mentor, Seun Owonikoko, for her support and feedback. I also want to thank the tutors from Code Institute for helping me solve
several issues that came up along the way.
