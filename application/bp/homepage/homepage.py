"""Homepage blueprint with home and about routes."""

from flask import Blueprint, render_template

homepage = Blueprint("homepage", __name__, template_folder="templates")


@homepage.route("/")
def home():
    """Render the home page."""
    return render_template("homepage.html")


@homepage.route("/about")
def about():
    """Render the about page."""
    return render_template("about.html")

