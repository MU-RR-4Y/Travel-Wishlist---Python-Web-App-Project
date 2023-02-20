from flask import Flask, render_template, redirect, request
from flask import Blueprint
from models.user import User
import repositories.user_repository as user_repo
import repositories.country_repository as country_repo
import repositories.destination_respository as destination_repo

users_blueprint = Blueprint('users', __name__)

# INDEX ('/') GET
@users_blueprint.route('/users')
def users():
    users = user_repo.select_all()
    return render_template('users/index.html', users = users)

# NEW ('/new') GET

# CREATE ('/') POST
# SHOW ('/id') GET
# EDIT ('/id/edit') GET
# UPDATE ('/id') POST
# DELETE ('/id/delete') POST



