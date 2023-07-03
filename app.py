'''

# TODO: Display the following... (below)

# Team: panthers stats
______
total players
total experienced
total inexperienced
average height

players on team
....
guardians of players
... 

Press ENTER to continue

'''
from constants import TEAMS
from constants import PLAYERS
from operator import itemgetter
import copy

deepcopyteams = copy.deepcopy(TEAMS)
deepcopyplayers = copy.deepcopy(PLAYERS)
sorted_players = sorted(deepcopyplayers, key=itemgetter('experience'))

newpanthers = []
newbandits = []
newwarriors = []

def clean_data(): 
    no_exp = False
    exp = True
    for player in sorted_players:
        if player["experience"] == 'NO':
            player["experience"] = bool(no_exp)
            #turns experience into a boolean value
        elif player["experience"] == 'YES':
            player["experience"] = bool(exp)
        player["height"] = int(player['height'][0:2]) #converts height to an integer value
        player["guardians"] = (player["guardians"]).split(" and ") 
        #removes " and " and creates a list of guardians"
    balance_teams(sorted_players)

def balance_teams(thesorted):
    #takes sorted_players (with cleaned data) and ads them to their new teams
    #3 experienced players & 3 inexperienced players per team
    for i in range(0, len(thesorted),3):
        #loop 3 players at a time and make into a "group"
        group = thesorted[i:i+3]
        newpanthers.append(group[0])
        newbandits.append(group[1])
        newwarriors.append(group[2])
    return(newpanthers,newbandits,newwarriors)

def menu():
    #initial game menu.
    print("### WELCOME TO TEAM STATS! ####\n")
    print("Here are your choices:\n\n")
    while True:
        try:             
            display = input('A) Display team stats"\nB) Quit\n\nEnter an option: ')
            if display.upper() == "A":
                teamselector()
                break
            elif display.upper() == "B":
                print("Thank you for playing")
                break
            else:
                raise ValueError
        except ValueError as e:
            display = input('sorry, press any key to try again ')
                
def teamselector():
    while True:
        try:
            #prompts user to choose one of the 3 teams in the consistant list TEAMS
            #returns the appropriate team for their selection in the display_stats function (below)
            team_select = input(f"Select team to see their stats:\n\nA) {deepcopyteams[0]}\nB) {deepcopyteams[1]}\nC) {deepcopyteams[2]}\n\n ")
            if team_select.upper() == "A":
                print(f" --- Team: {deepcopyteams[0]} Stats --- \n\n")
                display_stats(newpanthers)
                break
            elif team_select.upper() == "B":
                print(f" --- Team: {deepcopyteams[1]} Stats --- \n\n")
                display_stats(newbandits)
                break
            elif team_select.upper() == "C":
                print(f" --- Team: {deepcopyteams[2]} Stats --- \n\n")
                display_stats(newwarriors)
                break
            else:
                raise ValueError
        except ValueError as e:
            print(f'{e} Sorry, please enter a valid selection \n')
    
def display_stats(team):
    exp_players = 0
    inex_players = 0
    totalheights = 0
    team_list = []
    team_guardians = []
    print("players:\n________________\n")
    for player in team:
        team_list.append(player["name"])
        if player["experience"] == 1:
            exp_players += 1
        elif player["experience"] == 0:
            inex_players += 1
        totalheights += int(player['height'])
        #gives total height of team players to be averaged a few lines down
        #create a list of all players on the team
        for guardian in player["guardians"]: 
            team_guardians.append(guardian)
        #add all team guardians to list team_guardians
    avg_height = totalheights / len(team_list)
    #calculates average heigh of team players
    player_names = ' , '.join(str(player) for player in team_list)
    print(player_names)
    print(f"Total players: {len(team)}")
    print(f"Total experiented players: {exp_players}")
    print(f"Total experiented players: {inex_players}")
    print(f"Average height: {round(avg_height)} inches")
    guardian_names = ' , '.join(team_guardians)
    print(f"Player guardians: {guardian_names}")

    while True:
        choice = input("\n\nWould you like to view another team stat? or would you like to exit? Y/N...")
        try: 
            if choice.upper() == "Y":
                teamselector()
                break
            elif choice.upper() == "N":
                print("Thanks and have a great day!!!")
                break
            else:
                raise ValueError
        except ValueError as e:
            print(f'{e} Sorry, please enter a valid selection \n')
            

if __name__ == '__main__':
    clean_data()
    menu()
