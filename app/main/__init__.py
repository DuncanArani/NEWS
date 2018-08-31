# We import the Blueprint class from flask. We then initialize the Blueprint class by creating a variable main. The Blueprint class takes in 2 arguments. The name of the blueprint and the __name__ variable to find the location of the blueprint.

from flask import Blueprint
main = Blueprint('main',__name__)
from . import views,error
