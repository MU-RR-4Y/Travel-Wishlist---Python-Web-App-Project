leaders= ['Dave', 'Dave', 'Dave', 'Jack', 'Jack', 'Simon', 'John', 'Steve']

def leader(list):
    leaderboard=[]
    for name in list:
        if leaderboard.count(name)==0:
            leaderboard.append(name)
        else:
            pass
    return leaderboard

print(leader(leaders))