"""
Import modules - including Flask class
"""
import os
import json
# capital F indicates its a class name
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
    import env

# create an instance of Flask class with argument as flask module
# __name__. Flask needs this so that it knows where to look for
# templates and static files
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")


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
    Defines the about.html file pathway
    Change the <h2> element where called on the about.html
    Iterates through the list of numbers and creates a paragraph at each
    """
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template(
        "about.html",
        page_title="About",
        # list_of_numbers=[1, 2, 3]
        company=data
        )


@app.route("/about/<member_name>")
def about_member(member_name):
    """
    Defines the about/<member_name> file pathway
    Opens the JSON data as read-only and 
    iterates through each index providing a url link
    """
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    # return "<h1>" + member["name"] + "</h1>"
    return render_template("member.html", member=member)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    """
    Define the contact.html file pathway
    Displays a change of state when the form is submitted
    """
    if request.method == "POST":
        print(request.form.get("name")) # displays none
        print(request.form["email"]) # throws an exception
        print(request.form["phone"]) # throws an exception
        print(request.form["message"]) # throws an exception
        flash("Thanks {}, we have received your message!".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    """
    Define the careers.html file pathway
    """
    return render_template(
        "careers.html", page_title="Come Work With Us!"
        )


# We're using the os module from the standard library to get the 'IP'
# environment variable if it exists, but set a default value 0.0.0.0
# if it's not found. Same for port but as an integer


if __name__ == "__main__":  # "__main__" is the name of the default module in Py
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True  # security flaw: never have debug=True in live versions
        )
