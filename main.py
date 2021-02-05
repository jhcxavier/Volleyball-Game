# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

print("Volleyball Project\nJoão H Carneiro Xavier\n\n")
game_changer = False;
for i in range(1, 6):
    game_changer = False
    while not game_changer:
        score_1 = eval(input(f'Enter score that Team 1 got in the game {i}: '))
        score_2 = eval(input(f'Enter score that Team 2 got in the game {i}: '))
        result_1 = score_1 - score_2
        result_2 = score_2 - score_1
        if score_1 < 15 and score_2 < 15:
            print("Illegal score, one team must score at least 15 points. Try again.")
        elif (result_1 >= 0) and (result_1 < 2) or (result_2 < 2) and (result_2 >= 0):
            print("result 1", result_1)
            print("result 2", result_2)
            print("Sorry, one team must win by at least 2 points. Try again.")
        elif (score_1 > 15 and score_2 < 14) or (score_2 > 15 and score_1 < 14):
            print("Illegal score, you have to win by 2 when scoring over 15 points. Try again.")
        else:
            game_changer = True
