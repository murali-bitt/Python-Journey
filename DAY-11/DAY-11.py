import random

game_over = False
while game_over != True:
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    com_num = cards[random.randint(0,12)]
    plr_num = cards[random.randint(0,12)]
    score = com_num + plr_num
    print(f"{com_num} + {plr_num} = {score}")
    if score == 21:
        game_over = True