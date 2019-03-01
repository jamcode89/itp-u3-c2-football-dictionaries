from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_position(squads_list):
    nation = {}
    players = players_as_dictionaries(squads_list)
    for player in players:
        position = player['position']
        nation.setdefault(position, [])
        nation[position].append(player)
    return nation
    