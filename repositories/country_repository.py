from db.run_sql import run_sql
from models.country import Country

def save(country):
    sql = '''INSERT INTO countries (name)
            VALUES (%s)
            RETURNING id'''
    values = [country.name]
    result = run_sql(sql, values)
    country.id = result[0]['id']
    return country


def select_all():
    countries = []
    sql = 'SELECT * FROM countries'
    results = run_sql(sql)
    for result in results:
        country = Country(result['name'], result['id'])
        countries.append(country)
    return countries

def select(id):
    country = None
    sql = 'SELECT * FROM countries WHERE id = %s'
    values =[id]
    results = run_sql(sql, values)
    if results is not None:
        result = results[0]
        country = Country(result['name'], id)
    return country


def delete_all():
    sql ='DELETE FROM countries'
    run_sql(sql)

def delete(id):
    sql ='''DELETE FROM countries WHERE id = %s'''
    values = [id]
    run_sql(sql, values)