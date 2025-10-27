from flask import Blueprint, render_template

# Declare Blueprint object named `homepage`
homepage = Blueprint("homepage", __name__, template_folder="templates")

# default route: renders homepage.html
@homepage.route("/")
def home():
    return render_template("homepage.html")

# about route: renders about.html
@homepage.route("/about")
def about():
    return render_template("about.html")
