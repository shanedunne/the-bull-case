import os
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# Render home page
@app.route("/")
@app.route("/home")
def home():
    topics = mongo.db.topics.find()
    articles = list(mongo.db.articles.find().sort('article_date', -1).limit(4))
    return render_template("home.html", topics=topics, articles=articles)


# Render register page
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        # check if email already exists in db
        existing_email = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})

        if existing_email:
            flash("Email address already in use")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "fullname": request.form.get("fullname").lower(),
            "email": request.form.get("email").lower()
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


# Render login page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                                    existing_user["password"],
                                    request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get(
                        "username")), 'flash')
                return redirect(url_for("profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# Render profile page
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    articles = list(mongo.db.articles.find(
        {"article_author": username}))

    if session["user"]:
        return render_template(
            "profile.html", username=username, articles=articles)

    return redirect(url_for("login"))


# Logout function
@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# Render articles page
@app.route("/get_articles")
def get_articles():
    articles = list(mongo.db.articles.find())
    return render_template("articles.html", articles=articles)


# Render article template
@app.route("/view_article/<article_id>")
def view_article(article_id):
    article = mongo.db.articles.find_one({"_id": ObjectId(article_id)})
    comments = list(mongo.db.comments.find({"article_id": article_id}))
    return render_template("article.html", article=article, comments=comments)


# Create new article
@app.route("/post_article", methods=["GET", "POST"])
def post_article():
    if request.method == "POST":
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

    topics = mongo.db.topics.find().sort("topic_name", 1)
    return render_template("post-article.html", topics=topics)


# Edit Task
@app.route("/edit_article/<article_id>", methods=["GET", "POST"])
def edit_article(article_id):
    if request.method == "POST":
        if request.form.get("edit_article_body") == "":
            flash("Please fill in article body")
        else:
            updated = {
                "article_title": request.form.get("article_title"),
                "article_topic": request.form.get("article_topic"),
                "article_coin": request.form.get("article_coin"),
                "article_body": request.form.get("edit_article_body"),
                "article_author": session["user"],
                "article_published_datetime": datetime.now().strftime("%c"),
                "article_date": datetime.now().strftime("%x")
            }
            mongo.db.articles.update({"_id": ObjectId(article_id)}, updated)
            username = mongo.db.users.find_one(
                {"username": session["user"]})["username"]
            flash("Article Updated")
            return redirect(url_for("profile", username=username))

    article = mongo.db.articles.find_one({"_id": ObjectId(article_id)})
    topics = mongo.db.topics.find().sort("topic_name", 1)
    return render_template("edit-article.html", article=article, topics=topics)


# Render article delete modal
@app.route("/delete_modal/<article_id>")
def delete_modal(article_id):
    article = mongo.db.articles.find_one({"_id": ObjectId(article_id)})
    return render_template("profile.html", article=article)


# Delete article
@app.route("/delete_article/<article_id>")
def delete_article(article_id):
    mongo.db.articles.remove({"_id": ObjectId(article_id)})
    username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
    flash("Article Deleted")
    return redirect(url_for("profile", username=username))


# Post Comment
@app.route("/post_comment/<article_id>", methods=["GET", "POST"])
def post_comment(article_id):
    if request.method == "POST":
        comment = {
            "comment_author": session["user"],
            "article_id": article_id,
            "comment_body": request.form.get("comment_body"),
            "comment_published_datetime": datetime.now().strftime("%c")
        }
        mongo.db.comments.insert_one(comment)
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        article = mongo.db.articles.find_one({
            "_id": ObjectId(article_id)})
        flash("Comment Posted")
        return redirect(url_for('view_article', article_id=article["_id"],
                                article=article, username=username))

    return render_template("articles.html")


# Delete comment
@app.route("/delete_comment/<comment_id>/<article_id>")
def delete_comment(comment_id, article_id):
    mongo.db.comments.remove({"_id": ObjectId(comment_id)})
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    article = mongo.db.articles.find_one({
        "_id": ObjectId(article_id)})
    flash("Comment Deleted")
    return redirect(url_for('view_article', article_id=article["_id"],
                            article=article, username=username))


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', error=error), 404


@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html', error=error), 500

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
