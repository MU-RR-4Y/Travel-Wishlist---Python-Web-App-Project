from flask import Flask, render_template, redirect, request
from flask import Blueprint
from models.wishlists import Wishlist
import repositories.user_repository as user_repo
import repositories.destination_respository as destination_repo
import repositories.wishlist_repo as wishlist_repo

wishlists_blueprint =Blueprint('wishlists', __name__)

# NEW ('/new') GET
# add a wishlist item from the destination page
@wishlists_blueprint.route('/wishlists/new/<id>')
def add_wishlist_from_destination(id):
    destination = destination_repo.select(id)
    users = user_repo.select_all()
    return render_template('/wishlists/new.html', destination = destination, users = users)

# add a wishlist item from the user page
@wishlists_blueprint.route('/wishlists/new/<id>/user')
def add_wishlist_from_user(id):
    destinations = destination_repo.select_all()
    user = user_repo.select(id)
    return render_template('/wishlists/new2.html', destinations = destinations, user = user)

# # CREATE ('/') POST
# add wishlist

@wishlists_blueprint.route('/wishlists/create', methods =['POST'])
def create_wishlist():
    user = user_repo.select(request.form['user']) 
    destination = destination_repo.select(request.form['destination']) 
    wishlist = Wishlist(user,destination)
    wishlist_repo.save(wishlist)
    return redirect('/users')
    
