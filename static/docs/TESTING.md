# Testing

## User Stories

User 1: I want an easy to use site which has a simple layout and an easy registration process
- Test - The site has proved simple to navigate on both desktop and mobile and the registration, article submission and commenting functionality is striaght forward

User 2: I want a place where i can come and view the latest Crypto news.
- Test - When I viewed the home page i am initially greeted with some feature articles and an easy to navigate Nav bar to take me to further content

User 3: I want a place where i can research specifically fundamental analysis of cryptocurrencies.
- Test - When i navigated to the Articles section of the website I can use the handy tabs to specifically see only fundamental analysis articles. The featured articles on the home page also contain a topic tag which helps pick an article from the website loading

User 4: I am interested in the crypto space and love to give feedback on information pieces
- Each article has a simple comments section where i can share my thoughts on a particular piece

User 5: I have developed a new cryptocurrency project and would like a place to post articles sharing information about my project.
- Test - The Bull Case has a dedicated New Projects topic for developers like myself to share our ideas in article form

## Navigation Link Testing
**Nav Bar**
- Checked all nav bar items direct user to correct page including logo returning to home

**Home Page**
- Checked call to action routes to register page if not signed in or to the Create Article page when logged in
- Checked Read button on feature articles correctly opens article
- Checked footer link to Crypto Penguin is working and opens in a seperate tab

**Register**
- Checked Already Registered link directs to the login page
- Checked that when registration complete, user is redirtected to their profile 

**Login**
- Checked Not Registered link directs to the registration page
- Checked that when logged in, user is redirtected to their profile 

**Articles**
- Checked that all tabs on articles page route to correct article topic group
- Checked Read button on article cards correctly redirects to the article chosen
- Checked the Post Article button directs to the correct page
- Check Register Now button that appears if user not logged in leads to register page

**Post Article**
- Checked the user is redirected to their profile after posting an article

**Profile**
- Checked Read button on article cards
- Checked that the Edit button opens the Post Article page with the article information filled in for editing
- Checked the Delete button opens a modal with the article name 
- - Checked the Yes Delete button returns to the profile
- - Checked the No Thanks button returns to the profile
- - Checked the X closes the modal and returns to the profile

## Page Functionality Testing
### Nav Bar
- Checked that Login and Register appear if no user is logged in
- Checked that Profile and Logout appear if user is signed in

### Register
- Checked flash message appears if user tries to register with an existing username
- Checked email field requires email formatting
- Checked username and password will show error is special characters used

### Login
- Checked flash messages states username/password incorrect if user fails to login

### Logout
- Checked that logout button returns to Login page with flashed message notifying user they have been logged out

### Profile
- Checked welcome flash message appears upon login
- Checked profile titled as usernames profile
- Checked Create First Article button shows if user has no articles
- - Checked this button routes to Post Article page
- Checked Edit button routes to Edit page
- Checked Delete fucntionality works and removes article from database

### Edit Article
- Checked article fields are populated and changes made are updated when update article is clicked

### Home
- Checked that the call of action is set to register if user not logged in and Post Article if user already logged in
- Checked Featured Articles display 4no. most recent articles

### Articles
- Checked the correct articles are sorting by topic on each tab

### Post Article
- Checked post article functionality is working

### Article
- Checked article displaying correctly with relevant data
- Checked comment functionality is working correctly
- - Checked only user can delete comment they made

### 404 Page
- Checked route is working as intended and 404 page is displayed if invalid link entered
- Checked Return to Home button reirects to the home page

### 500 Page
Checked route works as intended and displays if internal server error is encountered

## Code Validation
- [WC3 HTML Validator](https://validator.w3.org/) - One issue related to the Edit Article page. Reasoning explained below in [Existing Bugs](#existing-bugs)
- [WC3 CSS Validator](https://jigsaw.w3.org/css-validator/) - Passed
- [JS Hint](https://jshint.com/) - Passed
- [PEP8 online](http://pep8online.com/) - Passed

## Issues and Solutions
- For writing articles, a typical HTML textarea could not generate a complex string to recognise paragraphs etc. My solution to this was to embed the TinyMCE Text Editor
- When the article body information is sent from MongoDB to display on the article page, it contained all of the tags and was not properly structured. This is due to Jinja automatic escaping. Using the safe filter marked the variable as safe and mitigated the issue
```html
                                  <div class="row d-flex justify-content-center">
                                    <div class="col-md-10">
                                      <div class="article-body">{{ article.article_body | safe }}</div>
                                    </div>
                                  </div>
```
- Again, due to the textarea being hiden and replaced by TinyMCE I had to create a work around to ensure the article was not submitted nor submitted after editing with an empty body. The solution was to include the below snippet in both post_article and edit_article python functions
```py
                        if request.form.get("article_body") == "":
                            flash("Please fill in article body")
                        else:
                            article = {
                                "article_title": request.form.get("article_title"),
                                "article_topic": request.form.get("article_topic"),
                                "article_coin": request.form.get("article_coin"),
                                "article_body": request.form.get("article_body"),
                                "article_author": session["user"],
                                "article_published_datetime": datetime.now().strftime("%c"),
                                "article_date": datetime.now().strftime("%x")
                            }
                            mongo.db.articles.insert_one(article)
                            username = mongo.db.users.find_one(
                                {"username": session["user"]})["username"]
                            flash("Article posted")
                            return redirect(url_for("profile", username=username))
```
## Existing Bugs
- Since TinyMCE hides the textarea and replaces it with the editor, i could not populate the textarea when editing. My solution was to use JavaScript to essentially catch the article body text and insert it into the text editor. This however, isn't a best practice as a textarea should not have a value attribute. This issue renders an error on the W3 HTML Validator. As of now it is the best solution for the issue and i continue to seek a better alternative
```js
                        var body = document.getElementById("edit_article_body").getAttribute("value");
                        var stringBody = body.toString(); 
                        document.getElementById("edit_article_body").innerHTML = stringBody;
```

## Responsiveness
Responsiveness was checked using [Responsinator](https://www.responsinator.com/) while also designed with responsiveness in mind with regular testing on Dev Tools. The responsiveness has been tested across multiple devices such as iPhone 8, iPhone 8 Plus, iPhone X, Samusing Galaxy X5, iPad etc.

## Usability 
Prior to submission, I deployed the site to GitHub Pages in order to be able to share a link to the site with some friends who are also interested in Cryptocurrency. All of the feedback was very positive, each friend found it easy to use

## Performance
I tested the performance of the app with Lighthouse. Displayed below are results for both mobile and desktop of the 'Articles' page
#### Mobile Report of Articles Page
- ![Mobile](../img/lighthouse-mobile-articles.png)

#### Desktop Report of Articles Page
- ![Mobile](../img/lighthouse-desktop-articles.png)





