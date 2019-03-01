from football_dictionaries.assignment_1   import players_as_dictionaries


def players_by_country_and_position(squads_list):
    nation = {}
    players = players_as_dictionaries(squads_list)
    for player in players:
        position = player['position']
        country = player['country']
        nation.setdefault(country,{})
        nation[country].setdefault(position, [])
        nation[country][position].append(player)
    return nation
    
