programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                          "Function": "A piece of code that you can easily call over and over again."}
print(programming_dictionary["Bug"])
fruits_and_colours = {
    "Apple" : "red",
    "Mango" : "Yellow",
    "pear" : "Green",
    "dragon fruit" : "Pink"
}

for key in fruits_and_colours:
    print(key)
    print(f"{fruits_and_colours[key]}\n")