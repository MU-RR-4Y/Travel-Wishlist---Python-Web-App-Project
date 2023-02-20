from flask import Flask, render_template, redirect, request
from flask import Blueprint
from models.country import Country
import repositories.country_repository as country_repo
import repositories.destination_respository as destination_repo

destinations_blueprint = Blueprint('destinations', __name__)

# INDEX ('/') GET
@destinations_blueprint.route('/destinations')
def destinations():
    destinations = destination_repo.select_all()
    countries = country_repo.select_all() 

    return render_template('destinations/index.html', destinations = destinations, countries = countries )

# NEW ('/new') GET
# CREATE ('/') POST
# SHOW ('/id') GET
# EDIT ('/id/edit') GET
# UPDATE ('/id') POST
# DELETE ('/id/delete') POST
