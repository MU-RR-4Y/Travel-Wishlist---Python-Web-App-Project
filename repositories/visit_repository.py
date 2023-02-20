from db.run_sql import run_sql
from models.visit import Visit
from models.country import Country
import repositories.destination_respository as destination_repo
import repositories.user_repository as user_repo
import repositories.country_repository as country_repo


def save(visit):
    sql = '''INSERT INTO visits (user_id, destination_id, date, rating, comment) VALUES (%s, %s,%s,%s, %s) RETURNING id'''
    values = [visit.user.id, visit.destination.id, visit.date, visit.rating, visit.comment]
    result = run_sql(sql, values)
    visit.id = result[0]['id']
    return visit

def select_all():
    visits =[]
    sql = '''SELECT * FROM visits'''
    results = run_sql(sql)
    for result in results:
        user = user_repo.select(int(result['user_id']))
        destination_id = int(result['destination_id'])
        destinations = destination_repo.select(destination_id)
        if destinations.id == destination_id:
            destination = destinations
        visit = Visit(user, destination , result['date'], result['rating'], result['comment'], result['id'])
        visits.append(visit)
    return visits 

# def select(id):
#     visit = None
#     sql = "SELECT * FROM visits WHERE id = %s"
#     values = [id]
#     result = run_sql(sql, values)[0]
#     if result is not None:
#         user = user_repo.select(int(result['user_id']))
#         destination =destination_repo.select(int(result['destination_id']))
#         visit = Visit(user, destination, result['date'], result['rating'], result['comment'], id )      
#     return visit



