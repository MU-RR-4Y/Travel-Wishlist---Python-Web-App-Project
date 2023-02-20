from db.run_sql import run_sql
from models.wishlists import Wishlist
import repositories.destination_respository as destination_repo
import repositories.user_repository as user_repo

def save(wishlist_item):
    sql = '''INSERT INTO wishlists (user_id, destination_id) VALUES (%s, %s) RETURNING id'''
    values = [wishlist_item.user.id, wishlist_item.destination.id]
    result = run_sql(sql, values)
    wishlist_item.id = result[0]['id']
    return wishlist_item