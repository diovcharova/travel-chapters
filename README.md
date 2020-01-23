# Travel Chapters
Milestone Project Three: Data Centric Development - Code Institute

This is a website that provides a platform for a user to share their travel experiences. The website is called 'Travel Chapters' and it enables the users to manage the database by creating, reading, updating and deleting entries. Each entry is a travel chapter. The website also includes a page that summarizes the locations a user has visited. 


## Demo 
A demo of the website can  be found [here](https://travel-chapters.herokuapp.com/).

## UX
The website is targeted at people, interested in traveling and looking for a way to keep track of the places they have visited. It also serves like a diary and can be a way for the users to share their experiences with others, sharing the link to the website. 
The design on the website is very simple and stripped of complicated structures. That is because it is vital for users to be able to navigate easily and find the information they are looking for. The structure of the different pages is the same to further accommodate ease of use. The colors, typography and styles are as neutral as possible, and only complement the main content.  

### User stories
* As a user who has visited many places, I want to be able to keep track of my experiences and store them in a structured way. 
* As a user, I want to have an overview of my visited locations.
* As a user looking for an idea for my next travel destination, reading a person's experiences can inform me of what to expect.

### UX based design
Based on the user stories, I got a clearer idea of the required features on the website. As part of the design process, I developed wireframes, which can be viewed [here](https://github.com/diovcharova/travel-chapters/tree/master/static/wireframes), and mockups, which can be viewed [here](https://github.com/diovcharova/travel-chapters/tree/master/static/mockups).

## Features

### Existing Features
The header gives a general structure to the website. The navbar is a list of links, that collapses to a dropdown menu on smaller screens to save real estate. The home page displays the currently available travel chapters in the data base in the form of cards. Each chapter can be edited or deleted. In the 'New travel chapter' page, a form is provided for the user to fill in the data that is fed to the database. 'Countries' displays the list of countries in the corresponding collection, each of which can also be edited or deleted. A button to add a new country is also provided on that page. Finally, the 'Visited locations' page renders a Google maps, with markers for each visited location. 

### Features left to implement
In the future, more features can be added on the website. For instance, a section can be added where the users can create a to-do list of the places they are planning or would like to visit. Also the website can be changed such that to allow users to create accounts. Each user can then share publicly their travels or read other people's experiences. Pagination can be implemented on the homepage. Furthermore some of the input fields of the form from adding a new chapter can be better validated.


## Technologies Used
1. HTML5
2. CCS3
3. Materialize (v4.0.0) - for a more structured layout.
4. JavaScript - to consume the API.
5. jQuery - for easier manipulation of the DOM.
6. Python + Flask - to manage the database calls and render the different templates.
7. MongoDB - to store the data input from the user.
8. Google Maps JavaScript API - to render Google Maps.
9. Geocoding API - to convert locations/addreses, stored in the database, to geographic coordinates.


## Testing
The testing procedure follows three steps - planning, implementation and outcomes.

For such a small scale project, manual testing of all the features is sufficient to establish the degree to which the application works as expected. All the pages, buttons, links and forms need to be manually visited, clicked on or filled in. The calls to the database and the Google Maps API should return the expected outcomes. 

The navigation bar, appears in all of the pages and is intended to provide more structure and ease of use. When clicked, all the links lead to the expected page. Using the back command in the browser does not cause any problems. 

On the home page, the cards corresponding to the different travel chapters appear. After manually checking, the call to the database does return the expected result, namely all entries in the chapters collection. The cards work as intended, and when clicked the additional information is displayed. Each chapter can be edited and deleted via the button on the bottom right corner of the card. 'Edit' leads to the edit page where a form is displayed. The input fields are prefilled with the data from the database such that the user can only edit one or a few of the fields. The 'Edit chapter' button at the bottom of the page redirects back to the home page. The delete button deletes the entry and reloads the home page. 

The 'New travel chapter' page displays a form, requesting the user for the relevant information in order to create a new entry in the database.  Most of the fields are required and validated. The select menu displays the countries, that are already input in the database. At this version of the application, there is no validation implemented that the end date is after the start date. Inputing incorrect values from the user does not prevent a creation of a new entry. 

The 'Countries' page is rather simple, it displays a list, which is a result of a call to the database. Each item in the list can be edited or deleted via the icons on the right. The work as expected. Pressing the edit icon leads to a prefilled form and upon submition, the user is redirected back to the 'Countries' page. Deleting works in the same way as the delete of a chapter and just reloads the page, while removing the relevant entry from the database. 

The 'Visited locations' page renders a Google Maps from the Google Maps API with markers for each location present in the database. If a location is not found of Google Maps, no marker is displayed. Unfortunately, it is possible for a user to input a non-existent city or a combination of a city and country that is incorrect. This can be addressed in newer versions of the application. 

Different screen sizes have been tested to ensure responsiveness, in the developer tools and on [Responsinator](https://www.responsinator.com/). The website has also been run on various web browsers, such as Chrome, Safari, Internet Explorer and Microsoft Edge, leading to the conclusion the website is compatible with all of them. It does not perform well in most of the Firefox versions, as tested on [Browsershots](http://browsershots.org/). The HTML, CSS, JavaScript and Python codes have been validated by [HTML validator](https://validator.w3.org/), [CSS Validation service - Jigsaw](https://jigsaw.w3.org/css-validator/), [JSHint](https://jshint.com/) and [PEP8Online](http://pep8online.com/) respectively.

The outcomes of the manual testing show the the website and its features work as expected. The access to the different pages of the website is clear and straightforward as the header provides links to them. It is intuitive and makes it easy for a user to use. The different user stories achieve the intended outcome. 


## Deployment
1. A Github repository is created.
2. The site's source code is stored on the master branch (https://github.com/diovcharova/travel-chapters/).
3. After creating a new app on Heroku, the site is deployed by pushing the code from the repository by the command 'git push heroku master'. The site automatically updates whenever there is a new push to the master branch through the terminal. 

In order to deploy properly, a Procfile, specifying the dynos, and a 'requirements.txt' files are needed. The later contains the required frameworks and libraries for the application to run. Additionally, a web process needs to be started in the terminal and the variables need to be configured at Heroku. 

To run locally, the repository is cloned into the editor of choice by pasting 'git clone https://github.com/diovcharova/travel-chapters/ ' into your terminal.

## Credits

### Content
All of the content on the website is written by me. The map displayed on the 'Locations' page are a result to a call to the [Google Maps API](https://developers.google.com/maps/documentation/javascript/tutorial).
### Media
The photos used in this site were obtained from user's input. Currently, the pictures in the cards are from [Pexels](https://www.pexels.com/). 
### Acknowledgements 
The JavaScript functions, used to consume the API are inspired by Rosie's Resume project, built in the Interactive Frontend Development module of the course at Code Institute. The Python code for creating route decorators is based on the Data Centric Development mini-project. 

