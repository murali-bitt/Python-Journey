# a = 1
# while a<=10:
#     print(f"{a} Hello")
# #     a += 1

# a =100
# while a >=1:
#     print(a)
#     a -= 1

# li1 = [1,4,9,16,25,36,49,64,81,100]
# for a in range(0,len(li1)):
#     print(li1[a])

# a = int(input("Enter number to get multiplication table: "))
# for i in range(1,13):
#     print(f"{i} X {a} = {i*a}")

# num = int(input("Enter a number to search: "))
# tp1 = (1,4,9,16,25,36,49,64,81,100)
# print(tp1)
# found = False
# b = 0
# for a in range(0,len(tp1)):
#     if num == tp1[a]:
#         found = True
#         b = a
# if found:
#     print(f"The number is there at {b+1}")

li1 = list(map(int, input("Enter the items in list: ").split()))
li2 = sorted(li1,reverse= True)
print(li2)
print(f"The product of largest two numbers is \"{(li2[0])*(li2[1])}\"")
print(f"The sum of largest two numbers is \"{(li2[0]+li2[1])}\"")

