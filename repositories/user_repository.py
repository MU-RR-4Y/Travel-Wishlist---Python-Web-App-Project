from db.run_sql import run_sql
from models.user import User
from models.country import Country
from models.destination import Destination
import repositories.country_repository as country_repo


def save(user):
    sql = '''INSERT INTO users (name) VALUES (%s) RETURNING id'''
    values = [user.name]
    result = run_sql(sql, values)
    user.id = result[0]['id']
    return user



def select_all():
    users = []
    sql = '''SELECT * FROM users'''
    results = run_sql(sql)
    for result in results:
        user = User(result['name'], result['id'])
        users.append(user)
    return users 

def select(id):
    user = None
    sql = "SELECT * FROM users WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        user = User(result['name'], result['id'] )
    return user



def delete_all():
    sql ='DELETE FROM users'
    run_sql(sql)



def destinations(user):
    destinations = []
    sql = ''' SELECT destinations.* FROM destinations
        INNER JOIN visits
        ON visits.destination_id = destinations.id   
        WHERE visits.user_id = %s'''    
    values =[user.id]
    results = run_sql(sql,values)
    for result in results:
        country = country_repo.select(int(result['country_id']))
        destination = Destination(result['name'],result['information'], country, result['id'])
        destinations.append(destination)
    return destinations




def visited_on_destinations(destination):
    users =[]
    sql = ''' SELECT users.* FROM users
        INNER JOIN visits
        ON visits.user_id = users.id   
        WHERE visits.destination_id = %s'''    
    values =[destination.id]
    results = run_sql(sql,values)
    for result in results:
        user = User(result['name'],result['id'])
        users.append(user)
    return users


# def wiishlist(user):
#     destinations =[]
#     sql =''' SELECT destinations.* FROM destinations
#         INNER JOIN visits
#         ON visits.destination_id = destinations.id   
#         WHERE visits.user_id = %s'''      
#     values =[user.id]
#     results = run_sql(sql,values)
#     for result in results:
#         destination = destination(result['name'], result['infromation'], result,result['id'])
#         destinations.append(destination)
#     return destinations
