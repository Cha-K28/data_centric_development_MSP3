# README.md
# ServiceHistory

## About

If you are buying a car wouldnt you like to know that it was well looked after. 

Thats where a service history comes in. By documenting all the work that has been done on your car it makes it alot easier to sell, and alot easier to trade in. 

The more detailed the service history the better. 

From oil changes to. new wipers and even a bulb, everything should be documented. 

Its best to keep all this in one place. However alot of people may not know that their service history is usually in the vehicle glove box. Aswell as this people can forget to fill it in. 

Thats when this website comes into play. As an online service history its very simple to fill in when you are on a computer, tablet or smart phone. 

It was key to have a website that was easy to use for any vehicle user. Many people are not familiar with car terminology such as timing belts, clutches, turbos or Automatic transmission oils, 
The beauty of the site is that you can fill in what you want and what you understand. 

As well as car owners it could also be used for businessess with a fleet of cars that want to keep all service histories in one place. 
It can even be used by cyclists who want to keep thier bycycle service history up to date. 

The website could also be edited slightly and used for many different reasons, such as shopping lists, a spending tracker or a exorsise tacker. 

### Features left to implement

One feature in particular id would like to add to the website in the future is the and extra table so that a user can have different cars based on the reg number. At present if a user has more
than one vehicle, the service histories will be mixed. 

This would open up the site to even more potential users such as garages and dealerships that want to keep track on the vehicle they have worked on. 

Id also like to add some content to the carousel on the home page.

The other feature id like to add is an email subscription as part of the registration and and "forgot password" function if a user forget their password. 

## Wireframes


## UX
This website can be used by any vehicle owner. It has one main funtion.

The function of the website is an online service history for your car. You Register, with a username and password, and following that simple step you can begin adding your service history details. 
Too often peolple remove the service book from their cars or dont even know where it is so an online service history that is simple to use is a perfect solution. 

Once the user registers they can then add a service, they can edit it and if delete it id nessessary. 


The entire website is laid out in an easy to use way so that anybody can navigate it.
The buttons are large and its very clear what each button does. Register, Add, View, Edit/update and Delete.

The Data to be entered in the table is very clear so there is no confusion for the user. 

## Features

The website has only a few features as it has one main function. 

It has an Register Form, Log in Form and Service info Table. 

Another nice feature on the homepage is the Carousel. In the future id like to popuplate the carousel with info displaying just how important a proper service history is, instead of having it in a
paragraph. Some nicer pictures with nicer text would be very appealing to a user. 

Another feature i used that was new to me was the Modal. The modal again was got from Materialize and used to ensure the user wanted to delete a serive. 




## Technologies Used

Materialize: "https://materializecss.com/getting-started.html"
Materialize was used throughout the website. I uses Materialize for the Carousel on the home page, the Login and Register Forms and the Service History Table. 
It was also used to generate both the header and the footer. 


Font Awesome: "https://fontawesome.com/"
Font awsome was used for the icons on the website.

W3schools: "https://www.w3schools.com/css/default.asp"
I used W3 schools at various stages of the project to help me understand some of Javascript, Python, CSS and HTML.

Jquery: "https://jquery.com/"
I used Jquery for the js parts of the project. As alot of it linked to my materialize features it was very handy to take them from there and they worked seamlessly.

MongoDB: "https://www.mongodb.com/"
I used Mongo DB for the Database




## Testing

The site was thoroughly tested on various different devices and browsers. Chrome, Safari, Firefox on Mac and PC. Also worked on both Iphone and Android.

The site works fine on both mobile and laptops.

Phone Screen sizes varied from Iphone 5/SE to Iphone 11.

Laptop screen sizes included 13" and 15.6". It was also tested on a larger 22" monitor. 

IT was tested using both chrome dev tools and actual devices.

I also sent it to friends and family for user testing.

## Issues

The main issue i had and still have with the site is that the service info table does not display correctly on smaller screens. I asked the tutors about this and It seems to be
a common issue with small screens. 

another issue i had was getting the service data to update. Initially i tried to do edit and update with in the one app route. 
I solved it by creating a seperate app route for the update function. 

The other issue was when i loged in with any user the service info was displayed. It should of been specific to each user. Thankfully, i got this sorted by adding a "created by" field 
and filtering on this when the user logs in. Now the service histories are specific to the loged in user. 

Another was one that the user stayed logged in all the time. I added a session lifetime of 30 mins to fix this. 

I had other small styling issues 


## Deployment

The Deployment for this site was slightly different to. previous Projects as this time i used Heroku. 

It was alos very simple

1. Add Requirements.txt an procfile
2. push code to github
3. log into heroku
4. configure VARs settings
5. after pushing to git enable auto updates on heroku
6. Enable auto deployment 
7. Click Deply branch (this may take a minute)
8. click View to see Deployed branch


## Content:
All Content about service histories was written by myself.

## Media:
All pictures used came from google searches.

## Acknowledgements
The code institute tutor team and in particular Igor who helped me at many stages throughout this project particularly when i had difficulties understanding wiring up the app routes.  
The idea came from my work, as part of my work i often have to deal with service historys so this give me the idea for the website
The IT team at work who took time out of their busy days to give me advice anytime I asked.
To Gerry, my mentor, for his wonderful guidance and advice throughout the project.
