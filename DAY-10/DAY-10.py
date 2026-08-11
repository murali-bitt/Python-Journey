# def fun():
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
#     c = a+b
#     # return(f"{a} + {b} = {c}")
#     print(f"{a} + {b} = {c}")
# fun()
n = input("Enter your name: ")
b = input("Enter the total amount: $")
def receipt(name,bill):
    print(f"Hello {name}, \nThanks for shopping.\nthe bill made was: ${bill}")
receipt(n,b)
