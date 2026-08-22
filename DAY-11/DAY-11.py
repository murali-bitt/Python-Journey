# import random

# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# game_over = False
# player_cards =[cards[random.randint(0,12)]]
# c = cards[random.randint(0,12)]
# dup_computer_cards = [c]
# computer_cards = [c]
# while game_over != True:
#     com_card1 = cards[random.randint(0,12)]
#     plr_card1 = cards[random.randint(0,12)]
#     player_cards.append(plr_card1)
#     player_score = sum(player_cards)
#     computer_cards.append(com_card1)
#     computer_score = sum(computer_cards)
#     print(f"PLAYER CARDS: {player_cards} \nCOMPUTER CARDS: {dup_computer_cards,'...'}")
#     print(player_score,computer_score)
#     repeat = input("Enter \"Y/y\" to HIT and \"N/n\"to STAND: ").lower()
#     if repeat == "n":
#         if player_score < computer_score:
#             print("COMPUTER WON")
#             print(computer_cards)
#             game_over = True
#         elif computer_score < player_score:
#             print("YOU WON!")
#             print(computer_cards)
#             game_over = True
#         elif player_score == computer_score:
#             print("TIE")
#             print(computer_cards)
#             game_over = True

# if player_score > 21:
#     print("COMPUTER WON")
#     print(computer_cards)
#     game_over = True
# elif computer_score > 21:
#     print("YOU WON!")
#     print(computer_cards)
#     game_over = True
# elif player_score == computer_score:
#     print("TIE")
#     print(computer_cards)
#     game_over = True
# else:
#     game_over = False

#actual solution:
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_cards = [cards[random.randint(0, 12)], cards[random.randint(0, 12)]]
computer_cards = [cards[random.randint(0, 12)], cards[random.randint(0, 12)]]

game_over = False

while not game_over:
    player_score = sum(player_cards)
    while player_score > 21 and 11 in player_cards:
        player_cards.remove(11)
        player_cards.append(1)
        player_score = sum(player_cards)

    print(f"Your cards: {player_cards}, current score: {player_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    if player_score >= 21:
        game_over = True
    else:
        choice = input(
            "Type 'y' to hit (get another card), 'n' to stand: "
        ).lower()
        if choice == "y":
            player_cards.append(cards[random.randint(0, 12)])
        else:
            game_over = True

computer_score = sum(computer_cards)
while computer_score > 21 and 11 in computer_cards:
    computer_cards.remove(11)
    computer_cards.append(1)
    computer_score = sum(computer_cards)

if player_score <= 21:
    while computer_score < 17:
        computer_cards.append(cards[random.randint(0, 12)])
        computer_score = sum(computer_cards)

        while computer_score > 21 and 11 in computer_cards:
            computer_cards.remove(11)
            computer_cards.append(1)
            computer_score = sum(computer_cards)

print("\n" + "=" * 30)
print(f"Your final hand: {player_cards}, final score: {player_score}")
print(
    f"Computer's final hand: {computer_cards}, final score: {computer_score}"
)
print("=" * 30)

if player_score > 21:
    print("You went over 21. YOU LOSE!")
elif computer_score > 21:
    print("Computer went over 21. YOU WIN!")
elif player_score > computer_score:
    print("YOU WIN!")
elif player_score < computer_score:
    print("COMPUTER WINS!")
else:
    print("IT'S A TIE!")