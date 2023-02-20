from db.run_sql import run_sql
from models.user import User
from models.country import Country
import repositories.destination_respository as destination_repo


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



# def destinations(user):
#     countries =[]
#     destinations = []
#     sql = ''' SELECT countries.* FROM countries
#         INNER JOIN visits
#         ON visits.country_id = countries.id   
#         WHERE visits.user_id = %s'''    
#     values =[user.id]
#     results = run_sql(sql,values)
#     for result in results:
#         country = Country(result['name'],result['id'])
#         countries.append(country)
       
#     destinations_list = destination_repo.select_all()
#     for destination in destinations_list:
#             for country in countries:
#                 if destination.country.id == country.id:
#                     destinations.append(destination)

#     for destination in destinations:
#         if 

#     return destinations

def visited_on_destinations(country):
    users =[]
    sql = ''' SELECT users.* FROM users
        INNER JOIN visits
        ON visits.user_id = users.id   
        WHERE visits.country_id = %s'''    
    values =[country.id]
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
