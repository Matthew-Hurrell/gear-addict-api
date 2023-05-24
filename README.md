# **Gear Addict - API**

Gear Addict is an online application that allows users to add and categorise their music gear and also share details about their live rigs with the community. Users can interact with other users by becoming a fan, as well as liking, commenting and saving rigs.

This project was built as the final portfolio submission for the [Code Institute](https://codeinstitute.net/) National Diploma in Full Stack Software Development. 

The project has been split into two parts - the front end built with [React](https://react.dev/), and the back end powered by the [Django REST Framework](https://www.django-rest-framework.org/). 

More information on the front end of the site can be found on the front end [README](https://github.com/Matthew-Hurrell/gear-addict/blob/main/README.md).

Link to the live site - [Gear Addict Live Site](https://gear-addict-react.herokuapp.com/)

Link to the live API - [Gear Addict Live API](https://gear-addict.herokuapp.com/)

Link to the front end repository - [Gear Addict Front End Repo](https://github.com/Matthew-Hurrell/gear-addict)

![Gear Addict Responsive](static/readme-images/gear-addict-responsive.png)

# Contents

* [**User Stories**](<#user-stories>)
* [**Database Schemas**](<#database-schemas>)
* [**Testing**](<#testing>)
    * [**Validator Tests**](<#validator-tests>)
    * [**Manual Tests**](<#manual-tests>)
    * [**Automated Tests**](<#automated-tests>)
    * [**Bugs**](<#bugs>)
* [**Technologies Used**](<#technologies-used>)
    * [Languages](<#languages>)
    * [Frameworks](<#frameworks>)
    * [Software](<#software>)
    * [Libraries](<#libraries>)
* [**Deployment**](<#deployment>)
* [**Credits**](<#credits>)
    * [**Content**](<#content>)
    * [**Media**](<#media>)
    * [**Code**](<#code>)
*  [**Acknowledgements**](<#acknowledgements>)


# User Stories

![Gear Addict User Story Example](static/readme-images/gear-addict-user-stories.png)

In terms of project management, user stories are an integral part of the software development creative process. There is a total of sixty user stories for the Gear Addict project. Before development began, all user stories began as epics. They were then refined down into user stories, which were then again split into acceptance criteria and tasks. Each user story was then assigned a story points number in relation to its difficulty in comparison to the other user stories. Finally, each user story was given a label to display its priority. User stories were then sorted into weekly iterations and added to the Gear Addict Project Board to aid with organisation. As development progressed, user stories were closed and moved into the done column on the Gear Addict project board. Each iteration was carefully planned to not have more than 60% must-have user stories. 

A full list of user stories can be found in a separate file here - [Gear Addict User Stories](https://github.com/Matthew-Hurrell/gear-addict/blob/main/readme/userstories.md)

The closed Gear Addict GitHub issues can be found here - [Gear Addict GitHub Issues](https://github.com/Matthew-Hurrell/gear-addict/issues?q=is%3Aissue+is%3Aclosed)

The Gear Addict Project Board can be found here - [Gear Addict Project Board](https://github.com/users/Matthew-Hurrell/projects/3)

[Back to top](<#contents>)

# Database Schemas

![Gear Addict Database Schema](static/readme-images/gear-addict-database-schema.png)

The Gear Addict database was created using seven custom models. There are two different post types - Gear and Rigs. Users can also interact with the community using the Star, Like, Comment and Fan models. The enhanced profile model allows for further profile customisation to add to the user experience. 

[Back to top](<#contents>)

# Testing

The Gear Addict application has been tested rigourously throughout the development process. This section will provide details on the tests carried out specifically on the back end API.

[Back to top](<#contents>)

## Validator Tests

![Gear Addict Python Lint Tests](static/readme-images/gear-addict-python-lint-test.png)

All Python code within the Gear Addict application has been run through the [Code Institute PEP8 Online Python Linter](https://pep8ci.herokuapp.com/). Minor indentation and whitespace errors were corrected. No known errors are now present.

[Back to top](<#contents>)

## Manual Tests

Here you will find a comprehensive list of all the manual tests that were carried out on the Gear Addict API.

| Status | **Rigs**
|:-------:|:--------|
| &check; | Correct list URL path
| &check; | Correct rig URL path
| &check; | Add rig functionality
| &check; | Edit rig functionality
| &check; | Delete rig functionality
| &check; | Correct rig fields
| &check; | Non authenticated users cannot create rigs
| &check; | Only authenticated owners can update or delete their own rig
| &check; | Search functionality
| &check; | Filter functionality
| &check; | Ordering functionality
| &check; | Default image URLs correct
| &check; | Pagination functioning
| &check; | Count fields functionality working correctly

| Status | **Gear**
|:-------:|:--------|
| &check; | Correct list URL path
| &check; | Correct gear URL path
| &check; | Add gear functionality
| &check; | Edit gear functionality
| &check; | Delete gear functionality
| &check; | Correct gear fields
| &check; | Non authenticated users cannot create gear
| &check; | Only authenticated owners can update or delete their own gear
| &check; | Search functionality
| &check; | Filter functionality
| &check; | Default image URL correct
| &check; | Pagination functioning

| Status | **Profiles**
|:-------:|:--------|
| &check; | User profile automatically created on sign up
| &check; | Correct list URL path
| &check; | Correct profile URL path
| &check; | Edit profile functionality
| &check; | Correct profile fields
| &check; | Only authenticated owners can update their own profile
| &check; | Filter functionality
| &check; | Ordering functionality
| &check; | Default image URLs correct
| &check; | Pagination functioning
| &check; | Count fields functionality working correctly

| Status | **Comments**
|:-------:|:--------|
| &check; | Correct list URL path
| &check; | Correct comment URL path
| &check; | Add comment functionality
| &check; | Edit comment functionality
| &check; | Delete comment functionality
| &check; | Correct comment fields
| &check; | Non authenticated users cannot create comments
| &check; | Only authenticated owners can update their own comment
| &check; | Filter functionality
| &check; | Pagination functioning
| &check; | Correct rig id 

| Status | **Fans**
|:-------:|:--------|
| &check; | Correct list URL path
| &check; | Correct fan URL path
| &check; | Add fan functionality
| &check; | Delete fan functionality
| &check; | Correct fan fields
| &check; | Non authenticated users cannot create a fan
| &check; | Only authenticated owners can delete their own fan
| &check; | Pagination functioning
| &check; | Correct fan name
| &check; | Correct idol id 

| Status | **Likes**
|:-------:|:--------|
| &check; | Correct list URL path
| &check; | Correct like URL path
| &check; | Add like functionality
| &check; | Delete like functionality
| &check; | Correct like fields
| &check; | Non authenticated users cannot add a like
| &check; | Only authenticated owners can delete their own like
| &check; | Pagination functioning
| &check; | Correct rig id 
| &check; | Correct owner 

| Status | **Stars**
|:-------:|:--------|
| &check; | Correct list URL path
| &check; | Correct star URL path
| &check; | Add star functionality
| &check; | Delete star functionality
| &check; | Correct star fields
| &check; | Non authenticated users cannot add a star
| &check; | Only authenticated owners can delete their own star
| &check; | Pagination functioning
| &check; | Correct rig id 
| &check; | Correct owner 

[Back to top](<#contents>)

## Automated Tests

[Back to top](<#contents>)

## Bugs

[Back to top](<#contents>)

# Technologies Used

[Back to top](<#contents>)

## Languages

[Back to top](<#contents>)

## Frameworks

[Back to top](<#contents>)

## Software 

[Back to top](<#contents>)

## Libraries

[Back to top](<#contents>)

# Deployment

[Back to top](<#contents>)

# Credits

[Back to top](<#contents>)

## Content

[Back to top](<#contents>)

## Media

[Back to top](<#contents>)

## Code

[Back to top](<#contents>)

# Acknowledgements

[Back to top](<#contents>)