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

    return render_template('/destinations/index.html', destinations = destinations, countries = countries )

# NEW ('/new') GET
@destinations_blueprint.route('/destinations/new/<id>')
def add_destintion_to_country(id):
    country = country_repo.select((int(id)+1))
    return render_template('/destinations/new2.html', country = country)
    


# CREATE ('/') POST
# @destinations_blueprint.route('/destinations/create', method =['POST'])
# def create_destination_country_page():




#     return render_template

# SHOW ('/id') GET
# EDIT ('/id/edit') GET
# UPDATE ('/id') POST
# DELETE ('/id/delete') POST
