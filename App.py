"""
Statistics for a kids basketball team.
Goal:
1. Create a copy of constants and Clean data
    a. height converted to integer ********************
    b. experienced -> Boolean(True or False)  ********************
    c. Guardians -> list & delete " and "  ********************
2. Create balanced teams function (3)
    a. 3 teams with equal number of experienced & inexperienced players (6 players on each team) ********************
3. Display stats of teams
    a. display team name
    b. Total players on that team as an integer
    c. The player names as strings separated by commas
    d. number of inexperienced players on that team
    e. number of experienced players on that team
    f. the average height of the team
    g. the guardians of all the players on that team (as a comma-separated string)
    h. The formatting you use to display is up to you.
Extra credit
4. Team balanced # of experienced & inexperienced players
5. Main menu Quit option
6. team stats gives players heights in asc order
7. save team analysis
"""

from constants import TEAMS
from constants import PLAYERS
import copy

Panthers = []
Bandits = []
Warriors = []

# Copy PLAYERS to a new list to be mutated
all_players = copy.deepcopy(PLAYERS)


def clean_up():

    # Data cleaning (height, experience, guardians)
    # sort players in all_players by experience
    from operator import itemgetter
    sorted(all_players, key=(itemgetter("experience")))
    for i in range(len(all_players)):
        height_in = all_players[i]["height"][0:2]
        all_players[i]["height"] = height_in
        # print(all_players[i]["height"])

        if all_players[i]["experience"] == "YES":
            all_players[i]["experience"] = bool("TRUE")
        else:
            all_players[i]["experience"] = bool("FALSE")
        # print(all_players[i]["experience"])
        # print(type(all_players[i]["experience"]))

        guardian_names = all_players[i]["guardians"].split(" and ")
        all_players[i]["guardians"] = guardian_names
        # print(all_players[i]["guardians"])
    return all_players


def draft_players():
    # copy code over and figure out how to make it work
    # print(all_players)
    all_teams = [Panthers, Bandits, Warriors]
    teams_len = len(all_teams)
    print(teams_len)
    for player in range(len(all_players)):
        all_teams[player % teams_len].append(all_players[player])
    print("Panthers: \n", Panthers, "\n\n", "Bandits: \n", Bandits, "\n\n", Warriors)
    return Panthers, Bandits, Warriors


""" 
    print(all_players)
    experienced_players = set()
    un_experienced_players = set()
    while len(experienced_players) != 3:
        for i in all_players:
            if i["experience"] == "TRUE":
                experienced_players.add(i)
                team_name.extend(experienced_players)
                print(experienced_players)
                return experienced_players

        print(experienced_players)
    while len(un_experienced_players) != 3:
        for i in all_players:
            if i["experience"] == "FALSE":
                un_experienced_players.add(i)
                team_name.append(un_experienced_players)
                return un_experienced_players

    return team_name
"""

if __name__ == "__main__":
    clean_up()

draft_players()