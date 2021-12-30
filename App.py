"""
Statistics for a kids basketball team.
Goal:
1. Create a copy of constants and Clean data
    a. height converted to integer
    b. experienced -> Boolean(True or False)
    c. Guardians -> list & delete " and "
2. Create balanced teams function (3)
    a. 3 teams with equal number of experienced & inexperienced players
3. Display stats of teams
    a.display team name
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
import re

def clean_up():
    all_players = copy.copy(PLAYERS)
    for player in all_players:
        for key, value in player.items():
            # CONVERT HEIGHT from string to int
            if key == "height":
                re.sub("[^0-9]", "", value)
                print(value)

        # comma delineate guardian names

        for key, value in player.items():
            if key == "guardians":
                value.split(" and ")
                print(value)



if __name__ == "__main__":
    clean_up()
