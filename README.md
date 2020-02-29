[![Build Status](https://travis-ci.org/ivarsaris/dutchtreats.svg?branch=master)](https://travis-ci.org/ivarsaris/dutchtreats)

# Dutchtreats

**E-commerce App - Fourth milestone project; Full stack frameworks with Django - Code Institute**

Dutchtreats is a web application where users can buy typical Dutch foods online and have it delivered
at home. Users can create and update a profile, find information about the products, write reviews, 
add items to a cart, and pay for these items using [Stripe](https://stripe.com/en-nl). Users can also
learn about the company on the about page and get in contact with Dutchtreats using a contact form. 

As a Dutchman who travels a lot, sometimes I miss Dutch foods. I love to try new foods and enjoy local cuisine.
However, sometimes I wish I could get my hands on some Dutch foods wherever I am. This inspired me to build this 
web application.

The web application was made for educational purposes only, it's not a real webshop.

## Demo

[Live website](https://dutchtreats.herokuapp.com/). The apllication is hosted on [Heroku](www.heroku.com) and uses a 
Heroku Postgress database.

![Responsive page](https://dutchtreats.s3.eu-west-3.amazonaws.com/media/images/dutchtreats-responsive.png)

## UX

### Users

Users of Dutchtreats are people who don't have access to Dutch foods where they live. The Netherlands has several delicasies
that are delicious and (almost) only available in The Netherlands. Dutch expats working in other countries, or others
who have stayed in The Netherlands and are back home can now order these foods online and have them delivered to their home.

#### User stories

I started by creating [user stories](userstories.md) to help determine what features to add to the website.

### Mockup

I created a [mockup](https://ivarsaris.wixsite.com/dutchtreats) using Wix. I did this in order to determine how to style the website and play around with
the layout.

### Design

In terms of the color scheme, the Dutch colors were choosen. Orange is the national color, and the Dutch flag is 
red, white, and blue. These colors come back all throughout the application. The search function has a yellow and
a red button. As you know, red and yellow together form orange. The products and meet the team colums have an orange background color. 
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

## Tecnhnologies used

The web application has been made using the following technologies:

* **Gitpod** - Online development environment for GitHub
* **HTML5** - Coding language used for creating the content and structure of the website
* **CSS** - Coding language used for styling the content
* **Python3** - Dynamic, object oriented programming language
* **Django** - Open source Python framework used for building web applications
* **JavaScript** - Used for creating functions which add interactivity to the apllication
* **MongoDB** - Online open source document oriented database
* **Google Chrome** - Used as browser and for developer tools
* [**Materialize**](https://materializecss.com/) - Framework library used for display, styling and icons
* **Git** - Used for version control
* [**Github**](https://github.com/) - Used to host the repository for the application
* [**Heroku**](https://www.heroku.com/) - Used to deploy the application
* **Heroku Postgress** - SQL database from Heroku

## Development process

I made the backend functionalities before I created the styling. When I added the styling and the content, I ran into some bugs in the
backend. I fixed these along the way.

I started with the [Code Institute template](https://github.com/Code-Institute-Org/gitpod-full-template) for working in Gitpod. I created a 
repository in Github and linked this to the template. When I created most functionalities, I deployed the application to Heroku and deployed
Travis continuous integration. I had debug=True throughout working on the project. I switched this to debug=False upon final deployment in order to 
make sure no sensitive data can be retreived. Throughout the development process, I had the neccessary environment variables set in the env.py file.
I added this file to the .gitignore file so the sensitive variables wouldn't be uploaded the GitHub. I added the same environment variables to 
Heroku.

## Testing

### Automated Testing

Automated testing was done using Travis continuous integration. Automated testing is done for the apps, views, models, and forms.

### Manual testing

I manually tested all functions in all apps. I did this to ensure all functions were working properly. For a while, the functionality stored
admin as the user who wrote any review, no matter who is logged in. The problem here was an error in the 



