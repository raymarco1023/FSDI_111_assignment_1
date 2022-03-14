# from the flask "module" import the Flask "class"
from flask import Flask

# Initialize or instantiate the Flask class into the app variable.
app = Flask(__name__)
# app is an object (an instance of the FLask class)
# The relationship between objects and classes is like the relationship between houses and their blueprints.
#
#


@app.route("/")  # Flask decortor that maps a route to a "view function"
def about_me():  # view function
    me = {                          # a dictionary type variable called "me"
        "first_name": "Ray",  # <- Key/value pairs for our dictionary
        "last_name": "Garcia",
        "hobbies": "Outdoor",
        "active": True
    }
    return me                       # our return statement
    # By default, flask will convert python dictionaries to JSON


@app.route("/greet/<name>/")
def greet_user(name):
    return "<h1>Hello, %s</h1>" % name  # %s mapping a string


@app.route("/sqaure/<int:num>")
def square_num(num):
    return "<h1>%s squared is: %s</h1>" % (num, num*num)
