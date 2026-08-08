# programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
#                           "Function": "A piece of code that you can easily call over and over again."}
# print(programming_dictionary["Bug"])
# fruits_and_colours = {
#     "Apple" : "red",
#     "Mango" : "Yellow",
#     "pear" : "Green",
#     "dragon fruit" : "Pink"
# }

# for key in fruits_and_colours:
#     print(key)
#     print(f"{fruits_and_colours[key]}\n")

# name = input("Enter your name: ")
# Bid = int(input("Enter your Bid amount: "))
# def game():

# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }

# def grade():
#     for grades in student_scores:
#         val = student_scores[grades]
#         print(grades)
#         if 91<= val <=100:
#             print("Outstanding\n")
#         elif 81<= val <=90:
#             print("Exceeds\n")
#         elif 71<= val <=80:
#             print("Acceptable\n")
#         else:
#             print("Fail\n")

# student_grades = grade()

# starting_dictionary = {
#     "a": 9,
#     "b": 8,
# }


# final_dictionary = {
#     "a": 9,
#     "b": 8,
#     "c": 7,
# }

# starting_dictionary["c"] = 7
# print(starting_dictionary)


def high():
    bidd = 0

    for w in data:
        if data[w] > bidd:
            bidd = data[w]
            winner = w
    print(f"The winner is {winner} and the amount is: ${bidd}")

cnt = True
data = {}
while cnt:
    name = input("Enter your name: ")
    bid = int(input("Enter your bidding amount: "))
    data[name] = bid
    opn = input("type \"y\" if there is another biider and \"n\" to know who is the winner: ")
    if opn == "n":
        cnt = False
        high()
    elif opn == "y":
        print("\n"*20)