from flask import Flask, render_template, redirect, request
from flask import Blueprint
from models.wishlists import Wishlist
import repositories.user_repository as user_repo
import repositories.destination_respository as destination_repo
import repositories.wishlist_repo as wishlist_repo

wishlists_blueprint =Blueprint('wishlists', __name__)

# NEW ('/new') GET
@wishlists_blueprint.route('/wishlists/new')
def add_wishlist():
    destinations = destination_repo.select_all()
    users = user_repo.select_all()
    return render_template('/wishlists/new.html', destinations = destinations, users = users)

# add a visit from the destination page
@wishlists_blueprint.route('/wishlists/new/<id>')
def add_wishlist_from_destination(id):
    destination = destination_repo.select(id)
    users = user_repo.select_all()
    return render_template('/wishlists/new.html', destination = destination, users = users)


# # CREATE ('/') POST
# # add visit from visit page

@wishlists_blueprint.route('/wishlists/create', methods =['POST'])
def create_wishlist():
    user = user_repo.select(request.form['user']) 
    destination = destination_repo.select(request.form['destination']) 
    wishlist = Wishlist(user,destination)
    wishlist_repo.save(wishlist)
    return redirect('/users')
    
# # add visit from destination page
# @wishlists_blueprint.route('/wishlists/<id>/create', methods =['POST'])
# def create_wishlist_from_destination():
#     user = user_repo.select(request.form['user']) 
#     destination = destination_repo.select(request.form['destination']) 
#     date = request.form['date']
#     rating = request.form['rating']
#     comment = request.form['comment']
#     visit = Visit(user,destination,date, rating, comment)
#     visit_repo.save(visit)
#     return redirect('/destinations')