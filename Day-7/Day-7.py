import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

game_over = False
new_li = []

while game_over == False:
    guess = input("\nGuess a letter: ").lower()

    word = ""

    for letter in chosen_word:
        if letter == guess:
            word += letter
            new_li.append(guess)
        elif letter in new_li:
            word += letter
        else:
            word += "_"
    print(word)

    if "_" not in word:
        game_over = True
        print("You won!")