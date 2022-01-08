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
    a. display team name *
    b. Total players on that team as an integer *
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
from time import sleep


Panthers = []
Bandits = []
Warriors = []
team_names_str = ["Panthers", "Bandits", "Warriors"]
all_teams = [Panthers, Bandits, Warriors]

# Copy PLAYERS to a new list to be mutated
all_players = copy.deepcopy(PLAYERS)


def clean_up():

    # Data cleaning (height, experience, guardians)
    # sort players in all_players by experience
    from operator import itemgetter
    asp = sorted(all_players, key=(itemgetter("experience")))
    for i in range(len(all_players)):
        height_in = all_players[i]["height"][0:2]
        int(height_in)
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
    teams_len = len(all_teams)
    for player in range(len(all_players)):
        all_teams[player % teams_len].append(all_players[player])
    # print("Panthers: \n", Panthers, "\n\n", "Bandits: \n", Bandits, "\n\n", Warriors)
    return Panthers, Bandits, Warriors


def team_stats(team_name, selection):
    # give name of team
    print(f"\nTeam Name: {team_names_str[selection]}")
    # number of members on the team
    number_of_players = len(all_teams[selection])
    print(f"Number of Players: {number_of_players}")
    # The player names as strings separated by commas
    team_members = []
    for count, i in enumerate(team_name):
        team_members.append(team_name[count]["name"])
    team_members_string = ", ".join(team_members)
    print(f"Players: {team_members_string}")

    # number of inexperienced players on that team
    ip = 0
    ep = 0
    for i in team_name:
        if i["experience"] is False:
            ip += 1
        elif i["experience"] is True:
            ep += 1
    print(f"Inexperienced Players: {ip}")
    # number of experienced players on that team
    print(f"Experienced Players: {ep}")
    # the average height of the team
    sum_heights = 0
    for i in team_name:
        sum_heights = sum_heights + i["height"]
    avg_height = sum_heights / len(team_name)
    print(f"Average player height: {avg_height} inches")
    # the guardians of all the players on that team (as a comma-separated string)

    # The formatting you use to display is up to you.

# User interface
def statistics_finder():
    print("***BASKETBALL STATS***")
    try:
        start_select = str(input("Select Option \n    a) View teams \n    b) Quit \n"))
        if start_select.lower() == "a":
            print("\n\nSELECT A TEAM TO VIEW")
            print("    a) Panthers \n    b) Bandits \n    c) Warriors")
            try:
                mm_select = input("Choose one team")
                mm_select.lower()
                if mm_select == "a":
                    print("Accessing Panthers team view...")
                    sleep(.25)
                    """
                    loading = "##########"
                    for letter in loading:
                        print(letter)
                        sleep(.1) """
                    team_stats(Panthers, 0)
                elif mm_select == "b":
                    print("Bandits team viewer")
                elif mm_select == "c":
                    print("Warriors team viewer")
                else:
                    raise ValueError
            except ValueError:
                print("Please provide a valid response")
            # Bring to main menu
        elif start_select.lower() == "b":
            print("Goodbye")
        else:
            raise ValueError
    except ValueError:
        print("Please provide a valid response")

# if __name__ == "__main__":


clean_up()

draft_players()

# statistics_finder()

