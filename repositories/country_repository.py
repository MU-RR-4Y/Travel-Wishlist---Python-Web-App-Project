from db.run_sql import run_sql
from models.country import Country
import repositories.country_repository as country_repo

def save(country):
    sql = '''INSERT INTO countries (name, climate, currency)
            VALUES (%s, %s, %s)
            RETURNING id'''
    values = [country.name, country.climate, country.currency]
    result = run_sql(sql, values)
    country.id = result[0]['id']
    return country


def select_all():
    countries = []
    sql = 'SELECT * FROM countries'
    results = run_sql(sql)
    for result in results:
        country = Country(result['name'], result['climate'], result['currency'], result['id'])
        countries.append(country)
    return countries

def select(id):
    country = None
    sql = 'SELECT * FROM countries WHERE id = %s'
    values =[id]
    results = run_sql(sql, values)
    if results is not None:
        result = results[0]
        country = Country(result['name'],result['climate'], result['currency'], id)
    return country


def delete_all():
    sql ='DELETE FROM countries'
    run_sql(sql)

def delete(id):
    sql ='''DELETE FROM countries WHERE id = %s'''
    values = [id]
    run_sql(sql, values)

def update_country(country):
    sql = '''UPDATE countries SET (climate, currency) = ( %s, %s) WHERE id = %s'''
    values = [country.climate, country.currency, country.id]
    run_sql(sql,values)
    