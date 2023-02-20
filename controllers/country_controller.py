from flask import Flask, render_template, redirect, request
from flask import Blueprint
from models.country import Country
import repositories.country_repository as country_repo
import repositories.destination_respository as destination_repo

countries_blueprint = Blueprint('countries', __name__)

# INDEX ('/') GET
@countries_blueprint.route('/countries')
def countries():
    destinations = destination_repo.select_all()
    countries = country_repo.select_all()
    return render_template('countries/index.html', countries = countries, destinations =destinations)


# NEW ('/new') GET


# CREATE ('/') POST
# SHOW ('/id') GET
# EDIT ('/id/edit') GET
# UPDATE ('/id') POST
# DELETE ('/id/delete') POST
