import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("Welcome to Rock, Paper, Scissor!")
usr_input = int(input("Enter 0 for Rock, 1 for Paper, 2 for Scissor: "))
if usr_input == 0:
    print(f"You choose Rock: \n{rock}")
elif usr_input == 1:
    print(f"You choose Paper: \n{paper}")
elif usr_input == 2:
    print(f"You choose Scissor: \n{scissors}")
else:
    print("Error input. Try again!")

computer_input = random.randint(0,2)
li1 = [rock,paper,scissors]
print(f"The computer Chooses: \n{li1[computer_input]}")

if usr_input == computer_input:
    print("It's a TIE!")
elif usr_input == 0 and computer_input == 1:
    print("Computer WON!")
elif usr_input == 1 and computer_input == 2:
    print("Computer WON!")
elif usr_input == 2 and computer_input == 0:
    print("Computer WON!")
else:
    print("YOU WON!")