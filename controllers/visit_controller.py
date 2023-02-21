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

# add a visit from the destination page
@visits_blueprint.route('/visits/new/<id>')
def add_visit_from_destination(id):
    destination = destination_repo.select(id)
    users = user_repo.select_all()
    return render_template('/visits/new2.html', destination = destination, users = users)


# CREATE ('/') POST
# add visit from visit page

@visits_blueprint.route('/visits/create', methods =['POST'])
def create_visit():
    user = user_repo.select(request.form['user']) 
    destination = destination_repo.select(request.form['destination']) 
    date = request.form['date']
    rating = request.form['rating']
    comment = request.form['comment']
    visit = Visit(user,destination,date, rating, comment)
    visit_repo.save(visit)
    return redirect('/visits')
    
# add visit from destination page
@visits_blueprint.route('/visits/<id>/create', methods =['POST'])
def create_visit_from_destination():
    user = user_repo.select(request.form['user']) 
    destination = destination_repo.select(request.form['destination']) 
    date = request.form['date']
    rating = request.form['rating']
    comment = request.form['comment']
    visit = Visit(user,destination,date, rating, comment)
    visit_repo.save(visit)
    return redirect('/destinations')
    
    
  