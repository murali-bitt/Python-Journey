import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)


l = len(chosen_word)
blanks = ("_"*l)
print(f"the word is: ", blanks)

guess = input("\nGuess a letter: ").lower()

print(len(blanks))
for i in range(0,l):
    if guess == chosen_word[i]:
        print("the word is there.")
    else:
        print("The word is not there")
    i += 1