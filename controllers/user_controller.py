from flask import Flask, render_template, redirect, request
from flask import Blueprint
from models.user import User
import repositories.user_repository as user_repo
import repositories.country_repository as country_repo
import repositories.destination_respository as destination_repo
import repositories.visit_repository as visit_repo


users_blueprint = Blueprint('users', __name__)

# INDEX ('/') GET
@users_blueprint.route('/users')
def users():
    users = user_repo.select_all()
    user_visits = visit_repo.travel_leaderboard()
    return render_template('users/index.html', users = users, user_visits =user_visits)

# NEW ('/new') GET

# CREATE ('/') POST
@users_blueprint.route('/users/create', methods=['POST'])
def add_country():
    name = request.form['name']
    user = User(name)
    user_repo.save(user)
    return redirect('/users')

# SHOW ('/id') GET
@users_blueprint.route('/users/<id>')
def users_show(id):
    user = user_repo.select(id)
    visited = user_repo.destinations(user)
    wishlist = user_repo.wishlist(user)
    return render_template('users/show.html', user = user, visited_destinations = visited, wish_destinations = wishlist)

# EDIT ('/id/edit') GET
# UPDATE ('/id') POST
# DELETE ('/id/delete') POST



