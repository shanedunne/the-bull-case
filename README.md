# The Bull Case
![Project Across Devices](#)

The Bull Case aims to provide a place for blockchain enthusiasts to research, keep up to date and share their own thoughts on everything Crypto!

## Table of Contents:

- [UX](#ux)
  - [User Stories](#user-stories)
  - [Strategy](#1-strategy)
  - [Scope](#2-scope)
  - [Structure](#3-structure)
  - [Skeleton](#4-skeleton)
  - [Surface](#5-surface)
- [Features](#features)
  - [Existing Features](#existing-features)
  - [Features to consider implementing in the future](#features-to-consider-implementing-in-the-future)
- [Technologies Used](#technologies-used)
  - [Languages](#1-languages)
  - [Integrations](#2-integrations)
  - [Workspace, Version Control, and Repository Storage](#3-workspace-version-control-and-repository-storage)
- [Resources](#resources)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)
  - [Media](#media)
  - [Code](#code)
- [Acknowledgments](#acknowledgments)

## UX

### User Stories

- User 1: I want a place where i can come and view the latest Crypto news.
- User 2: I want a place where i can research specifically fundamental analysis of cryptocurrencies.
- User 3: I am interested in the development side of Crypto and need a source where i can filter for development articles.
- User 4: I have developed a new cryptocurrency project and would like a place to post articles sharing information about my project.
- User 5: I am a technical analyst and i would like a platform where i can post my research. I do not want to manage my own blog or join social media.

### Strategy
- Provide a platform where users can educate themselves on all aspects of the Crypto space
- Provide a route away from the conventions of social media where people can share their ideas and thoughts in article form

### Scope 
- An easy to navigate site with simple register, login and logout functions
- Articles can be filetered by topic using tabs
- Allows users to create, read, update and delete their submitted articles

### Structure
I wanted to create a simple and distraction free platform where the user experience and attention is always kept and directed towards the content of the site. 
For this reason the functionality is limited to not take away from the sole purpose of the site: a simple knowledge resource.
The structure and layout of pages is very similar across the board and allows for easy navigation without distraction

### Skeleton
- [Wireframes](static/docs/wireframes.pdf) - The final commit has not differed much from the initial intentions highlighted in the wireframes
- Navigation Bar
- - Home - Homepage containing call to action, blurb on purpose of site and a few featured articles
- - Articles - Call to action to post article with articles below catagorised by topic on different tabs
- - Post Article - Form to contribute an article including TinyMCE textarea
- - Article - Article page displaying topic, image, author, date published and the article body with a comments section at the bottom
- - Login - Simple login form requesting username and password. Link at bottom of form to register if not already
- - Register - Simple register form requesting full name, email address, username and password. Link at bottom of form to login if already registered
- - Profile - Contains all articles contributed by user with buttons to read, edit and delete articles. Delete articles propmts a modal to make sure the user wants to delete
- - Edit - Allows user to edit article with pre-populated fields containing original article
-
- Database Diagram
![Project Across Devices](static/docs/dbd)

### Surface

