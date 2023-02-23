from db.run_sql import run_sql
from models.visit import Visit
import repositories.destination_respository as destination_repo
import repositories.user_repository as user_repo
import repositories.wishlist_repo as wishlist_repo
import repositories.visit_repository as visit_repo


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


def most_most_visited_destination():
    visits = visit_repo.select_all()
    destination_list = []
    for item in visits:
        destination_name =item.destination.name
        destination_list.append(destination_name)
    destination = wishlist_repo.most_common(destination_list)
    return destination

def most_travelled_user():
    visits = visit_repo.select_all()
    user_list = []
    for item in visits:
        user_name = item.user.name
        user_list.append(user_name)
    user = wishlist_repo.most_common(user_list)
    return user

def leader(list):  #tested on tests/leaderboard.py
    leaderboard=[]
    for name in list:
        if leaderboard.count(name)==0:
            leaderboard.append(name)
        else:
            pass
    return leaderboard



def travel_leaderboard():
    visits = visit_repo.select_all()
    user_list = []
    for item in visits:
        user_name = item.user.name
        user_list.append(user_name)
    leaderboard = wishlist_repo.leaderboard(user_list)
    final_leaderboard = leader(leaderboard)
    return final_leaderboard