from db.run_sql import run_sql
from models.wishlists import Wishlist
from models.destination import Destination
import repositories.destination_respository as destination_repo
import repositories.user_repository as user_repo
import repositories.wishlist_repo as wishlist_repo

def save(wishlist_item):
    sql = '''INSERT INTO wishlists (user_id, destination_id) VALUES (%s, %s) RETURNING id'''
    values = [wishlist_item.user.id, wishlist_item.destination.id]
    result = run_sql(sql, values)
    wishlist_item.id = result[0]['id']
    return wishlist_item

def select_all():
    wishlists =[]
    sql ='''SELECT * FROM wishlists'''
    results = run_sql(sql)
    for result in results:
        user = user_repo.select(int(result['user_id']))
        destination = destination_repo.select(int(result['destination_id']))
        id = int(result['id'])
        wishlist_item = Wishlist(user,destination,id)
        wishlists.append(wishlist_item)
    return wishlists




def most_common(list):
    most_common_item = None
    counter = 0
    for item in list:
        if list.count(item)>counter:
            counter= list.count(item)
        most_common_item = item
    return most_common_item

def most_wishlisted_destintion():
    wishlists = wishlist_repo.select_all()
    destination_list =[]
    for item in wishlists:
        destination_name = item.destination.name
        destination_list.append(destination_name)
    destination = wishlist_repo.most_common(destination_list)
    return destination

    


    
   
