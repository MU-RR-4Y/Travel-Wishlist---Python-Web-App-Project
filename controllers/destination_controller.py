from flask import Flask, render_template, redirect, request
from flask import Blueprint
from models.country import Country
from models.destination import Destination
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
# request form to add destination from destination page - new.html
@destinations_blueprint.route('/destinations/new')
def add_destintion():
    countries =country_repo.select_all()
    return render_template('/destinations/new.html', countries = countries)


# request form to add destination from a country page - new2.html
@destinations_blueprint.route('/destinations/new/<id>')
def add_destintion_to_country(id):
    country = country_repo.select((int(id)))
    return render_template('/destinations/new2.html', country = country)
    


# CREATE ('/') POST
# Add a adestination from the destination page
@destinations_blueprint.route('/destinations/create', methods =['POST'])
def create_destination():
    name = request.form['name']
    information =request.form['info']
    country_form = request.form['country']
    countries = country_repo.select_all()
    for country_item in countries:
        if country_form == country_item.name:
            country = country_item

    destination = Destination(name,country,information)
    destination_repo.save(destination)
    return redirect('/destinations')
    

# Add a destination from a country page
@destinations_blueprint.route('/destinations/create/<id>', methods =['POST'])
def create_destination_country_page(id):
    name = request.form['name']
    information =request.form['info']
    country = country_repo.select(int(id))
    destination = Destination(name,country,information)
    destination_repo.save(destination)
    return redirect('/countries')

# SHOW ('/id') GET
# EDIT ('/id/edit') GET
# UPDATE ('/id') POST

# DELETE ('/id/delete') POST
#Delete from destination page
@destinations_blueprint.route('/destination/<id>/delete', methods=['POST'])
def delete_destination(id):
    destination_repo.delete(id)
    return redirect ('/destinations')

#delete from country page
@destinations_blueprint.route('/destination/<id>/delete/country', methods=['POST'])
def delete_destination_from_country(id):
    destination_repo.delete(id)
    return redirect('/countries')