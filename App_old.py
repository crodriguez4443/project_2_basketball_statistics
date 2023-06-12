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
    a. display team name *****
    b. Total players on that team as an integer *****
    c. The player names as strings separated by commas *****
    d. number of inexperienced players on that team *****
    e. number of experienced players on that team *****
    f. the average height of the team *****
    g. the guardians of all the players on that team (as a comma-separated string)  ????????????
    h. The formatting you use to display is up to you. *****
Extra credit
4. Team balanced # of experienced & inexperienced players ??????????
5. Main menu Quit option
6. team stats gives players heights in asc order
7. save team analysis
"""

from constants import TEAMS
from constants import PLAYERS
import copy
from time import sleep
from operator import itemgetter
from sys import exit

Panthers = []
Bandits = []
Warriors = []
panthers_sorted = []
bandits_sorted = []
warriors_sorted = []
panthers_stats = []
bandits_stats = []
warriors_stats = []
team_names_str = ["Panthers", "Bandits", "Warriors"]
all_teams = [Panthers, Bandits, Warriors]

# Copy PLAYERS to a new list to be mutated
players_unsorted = copy.deepcopy(PLAYERS)
# sort players in all_players by experience
all_players = sorted(players_unsorted, key=(itemgetter("experience")))


def clean_up():
    # Data cleaning (height, experience, guardians)

    for i in range(len(all_players)):
        height_in = all_players[i]["height"][0:2]
        all_players[i]["height"] = int(height_in)

        if all_players[i]["experience"] == "YES":
            all_players[i]["experience"] = True
        elif all_players[i]["experience"] == "NO":
            all_players[i]["experience"] = False
        # print(all_players[i]["experience"])
        # print(type(all_players[i]["experience"]))

        guardian_names = all_players[i]["guardians"].split(" and ")
        all_players[i]["guardians"] = guardian_names
        # print(all_players[i]["guardians"])

    # all fields are good
    return all_players


def draft_players():
    # copy code over and figure out how to make it work
    # print(all_players)
    teams_len = len(all_teams)
    for player in range(len(all_players)):
        all_teams[player % teams_len].append(all_players[player])
    # print("Panthers: \n", Panthers, "\n\n", "Bandits: \n", Bandits, "\n\n", Warriors)
    global warriors_sorted
    global panthers_sorted
    global bandits_sorted
    panthers_sorted = sorted(Panthers, key=(itemgetter("height")))
    bandits_sorted = sorted(Bandits, key=(itemgetter("height")))
    warriors_sorted = sorted(Warriors, key=(itemgetter("height")))


def team_stats(team_name, selection, stats_recorded):
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
    stats_recorded.append({"inexp": ip})
    stats_recorded.append({"exp": ep})
    sum_heights = 0
    for i in team_name:
        sum_heights = sum_heights + i["height"]
    avg_height = round(int(sum_heights) / int(len(team_name)), 2)
    print(f"Average player height: {avg_height} in")
    stats_recorded.append({"avg_height": avg_height})
    # the guardians of all the players on that team (as a comma-separated string).
    all_team_guardians = []

    for player in team_name:
        g = ", ".join(player['guardians'])
        all_team_guardians.append(g)
    team_guardians_string = ", ".join(all_team_guardians)
    print(f"Team guardians: {team_guardians_string}")

# Main Menu
def main_menu():
    print("*** BASKETBALL STATS***")
    while True:
        try:
            start_select = str(input("Select Option \n    a) View teams \n    b) Quit \n"))
            if start_select.lower() == "a":
                statistics_finder()
            elif start_select.lower() == "b":
                print("Program ending")
                exit()
            else:
                raise ValueError
        except ValueError:
            print("enter a valid response")


# User interface
def statistics_finder():
    while True:
        print("\n\nSELECT A TEAM TO VIEW")
        print("    a) Panthers \n    b) Bandits \n    c) Warriors \n    d) Main Menu")
        try:
            mm_select = input("Choose one team ")
            mm_select.lower()
            if mm_select == "a":
                print("Accessing Panthers team view...")
                sleep(.25)
                """
                loading = "##########"
                for letter in loading:
                    print(letter)
                    sleep(.1) """
                team_stats(panthers_sorted, 0, panthers_stats)
            elif mm_select == "b":
                print("Accessing Bandits team view...")
                sleep(.25)
                """
                loading = "##########"
                for letter in loading:
                    print(letter)
                    sleep(.1) """
                team_stats(bandits_sorted, 1, bandits_stats)
            elif mm_select == "c":
                print("Accessing Pirates team view...")
                sleep(.25)
                """
                loading = "##########"
                for letter in loading:
                    print(letter)
                    sleep(.1) """
                team_stats(warriors_sorted, 2, warriors_stats)
            elif mm_select == "d":
                print("\n\nTaking you to Main Menu")
                main_menu()
            else:
                raise ValueError
        except ValueError:
            print("Please provide a valid response")

if __name__ == "__main__":
    clean_up()
    draft_players()
    main_menu()
    statistics_finder()

