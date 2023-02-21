from flask import Flask, render_template, redirect, request
from flask import Blueprint
from models.visit import Visit
import repositories.user_repository as user_repo
import repositories.destination_respository as destination_repo
import repositories.visit_repository as visit_repo

visits_blueprint =Blueprint('visits', __name__)


#INDEX ('/') GET
@visits_blueprint.route('/visits')
def visit():
    visits = visit_repo.select_all()
    users = user_repo.select_all()
    destinations =destination_repo.select_all()
    return render_template('visits/index.html', visits = visits, destinations = destinations, users = users)



# @visits_blueprint.route('/visits/<index>')
# def show_visit(index):
#     visit = visit_repo.select(int(index))
#     return render_template('/visits/show.html', visit =visit)


# NEW ('/new') GET
@visits_blueprint.route('/visits/new')
def add_visit():
    destinations = destination_repo.select_all()
    users = user_repo.select_all()
    return render_template('/visits/new.html', destinations = destinations, users = users)
