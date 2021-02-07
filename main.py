# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
# Use a breakpoint in the code line below to debug your script.
# print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

print("Volleyball Project\nJoão H Carneiro Xavier\n\n")
team_1 = []
team_2 = []
game_changer = False
for i in range(1, 6):
    game_changer = False
    while not game_changer:
        score_1 = eval(input(f'Enter score that Team 1 got in the game {i}: '))
        if isinstance(score_1, float):
            print('Input error: please enter integer values only.')
        score_2 = eval(input(f'Enter score that Team 2 got in the game {i}: '))
        if isinstance(score_2, float):
            print('Input error: please enter integer values only.')
        result_1 = score_1 - score_2
        result_2 = score_2 - score_1
        if score_1 < 15 and score_2 < 15:
            print("Illegal score, one team must score at least 15 points. Try again.\n")
        elif (result_1 >= 0) and (result_1 < 2) or (result_2 < 2) and (result_2 >= 0):
            print("Sorry, one team must win by at least 2 points. Try again.\n")
        elif (score_1 > 15 and result_1 > 2) or (score_2 > 15 and result_2 > 2):
            print("Illegal score, you have to win by 2 when scoring over 15 points. Try again.\n")
        else:
            team_1 = [*team_1, score_1]
            team_2 = [*team_2, score_2]
            game_changer = True
    print('\n')
print("{:>5s}{:>10s}{:>10s}{:>10s}".format("Game", "Team 1", "Team 2", "Winner"))

team_winner_1 = 0
team_winner_2 = 0
winner = ""
for i in range(0, 5):
    if team_1[i] > team_2[i]:
        winner = "Team 1"
        team_winner_1 += 1
    else:
        winner = "Team 2"
        team_winner_2 += 1
    # print("printList", team_1[i-1])
    print("{:>5d}{:>10d}{:>10d}{:>10s}".format(i+1, team_1[i], team_2[i], winner))

if team_winner_1 > team_winner_2:
    print("\nThe winner of the match is Team 1")
else:
    print("\nThe winner of the match is Team 2")
