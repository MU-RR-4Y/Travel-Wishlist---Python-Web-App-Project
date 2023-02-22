from db.run_sql import run_sql
from models.destination import Destination
import repositories.country_repository as country_repo
import repositories.wishlist_repo as wishlist_repo

def save(destination):
    sql = '''INSERT INTO destinations (name, country_id, information)
          VALUES (%s, %s, %s)
          RETURNING id'''
    values = [destination.name,destination.country.id, destination.information]
    result = run_sql(sql, values)
    destination.id = result[0]['id']
    return destination


def delete_all():
    sql = 'DELETE FROM destinations'
    run_sql(sql)

def select_all():
    destinations = []
    sql = '''SELECT * FROM destinations'''
    results = run_sql(sql)
    for result in results:
        country_id = int(result['country_id'])
        countries = country_repo.select(country_id)
        if countries.id == country_id:
            country = countries
        destination = Destination(result['name'],country,result['information'], result['id'] )
        destinations.append(destination)
    return destinations
    

def select(id):
    destination = None
    sql ='''SELECT * FROM destinations WHERE id = %s'''
    values = [id]
    results = run_sql(sql, values)
    if results is not None:
        result = results[0]
        country_id = int(result['country_id'])
        countries = country_repo.select(country_id)
        if countries.id == country_id:
            country = countries
        destination = Destination(result['name'], country, result['information'],id)
        return destination

def delete(id):
    sql ='''DELETE FROM destinations WHERE id = %s'''
    values = [id]
    run_sql(sql, values)


def get_country(id):
    country_list = country_repo.select_all()
    for country in country_list:
        if country.id == int(id):
            return country




