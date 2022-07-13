"""
Import modules - including Flask class
"""
import os
# capital F indicates its a class name
from flask import Flask, render_template

# create an instance of Flask class with argument as flask module
# __name__. Flask needs this so that it knows where to look for
# templates and static files
app = Flask(__name__)


# ------------  @decorator (py-notation) as a way of wrapping functions.


@app.route("/")  # "/" navigates to the root directory
def index():
    """
    When we try to browse to the root directory, as indicated by the "/",
    then Flask triggers this index function returns "Hello, World" and/or
    the index.html file.
    """
    # return "<h1>Hello,</h1> <h2>World!</h2>"
    return render_template("index.html")  # links root directory to templates/


@app.route("/about")
def about():
    """
    Define the about.html file pathway
    """
    return render_template("about.html")


@app.route("/contact")
def contact():
    """
    Define the contact.html file pathway
    """
    return render_template("contact.html")


@app.route("/careers")
def careers():
    """
    Define the careers.html file pathway
    """
    return render_template("careers.html")


# We're using the os module from the standard library to get the 'IP'
# environment variable if it exists, but set a default value 0.0.0.0
# if it's not found. Same for port but as an integer


if __name__ == "__main__":  # __main__ is the name of the default module in Py
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True  # security flaw: never have debug=True in live versions
        )
