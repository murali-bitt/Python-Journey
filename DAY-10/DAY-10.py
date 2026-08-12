# def fun():
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
#     c = a+b
#     # return(f"{a} + {b} = {c}")
#     print(f"{a} + {b} = {c}")
# fun()
# n = input("Enter your name: ")
# b = input("Enter the total amount: $")
# def receipt(name,bill):
#     print(f"Hello {name}, \nThanks for shopping.\nthe bill made was: ${bill}")
# receipt(n,b)

# def is_leap_year(year):
#     a= 0
#     if year % 4 == 0:
#         a += 1
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 a += 1
#         else:
#             a +=1
#     return (a>=2)

# li1 = list(map(int, input("Enter elements of the list: ").split()))
# print(li1)
# li2 = li1*2
# print(li2)

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

should_continue = True
# n1 = int(input("Enter first number: "))
while should_continue:
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
    operation = input("Enter operation to peform(+ , - , * , /): ")
    if operation == "+":
        # n1 = add(n1,n2)
        print(add(n1,n2))
    elif operation == "-":
        # n1 = subtract(n1,n2)
        print(subtract(n1,n2))
    elif operation == "*":
        # n1 = multiply(n1,n2)
        print(multiply(n1,n2))
    elif operation == "/":
        # n1 = divide(n1,n2)
        print(divide(n1,n2))
    else:
        print("Invalid operation")
    ask_continution = input("Type \"Y\" to continue the program and \"N\" to stop: ")
    if ask_continution == "N":
        should_continue = False
    elif ask_continution != "N" and ask_continution != "Y":
        print("Invalid function")