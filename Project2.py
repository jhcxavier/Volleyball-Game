print("Volleyball Project\nJoão H Carneiro Xavier\n\n")

integer_values_only = 'Input error: please enter integer values only.'
illegal_score_1 = "Illegal score, one team must score at least 15 points. Try again.\n"
illegal_score_2 = "Illegal score, you have to win by 2 when scoring over 15 points. Try again.\n"
win_by_2 = "Sorry, one team must win by at least 2 points. Try again.\n"

team_1 = []
team_2 = []

game_changer = False

for i in range(1, 6):

    game_changer = False
    score_1 = ""
    while not game_changer:

        def get_int(prompt):
            while True:
                try:
                    answer = int(input(prompt))
                    break
                except ValueError:
                    print(integer_values_only)
                    return False
            return answer

        score_1 = get_int(f'Enter score that Team 1 got in the game {i}: ')
        if not score_1:
            continue

        score_2 = get_int(f'Enter score that Team 2 got in the game {i}: ')
        if not score_2:
            continue
        result_1 = score_1 - score_2
        result_2 = score_2 - score_1

        if score_1 < 15 and score_2 < 15:
            score_1 = ""
            print(illegal_score_1)
        elif (result_1 >= 0) and (result_1 < 2) or (result_2 < 2) and (result_2 >= 0):
            score_1 = ""
            print(win_by_2)
        elif (score_1 > 15 and result_1 > 2) or (score_2 > 15 and result_2 > 2):
            score_1 = ""
            print(illegal_score_2)
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
    print("{:>5d}{:>10d}{:>10d}{:>10s}".format(i + 1, team_1[i], team_2[i], winner))

print("\nThe winner of the match is Team 1") if team_winner_1 > team_winner_2 else print("\nThe winner of the match "
                                                                                         "is Team 2")
