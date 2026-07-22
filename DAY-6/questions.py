for num in range(1,51):
    if num%2 == 0:
            print(num)

summ = 0
for num in range(0,101):
    summ += num

# print(summ)

i = 0
for i in range(1,11):
    print(f"5 X {i} = {5*i}") 

string = input("Enter a string: ")

count = 0
i = 0

for i in string:
    count += 1

print("Length of string:", count)

string = str(input("Enter String: "))
name = list(string)
vcount = 0  
for i in range(len(string)):

    if name[i] == 'a' or name[i] == 'e' or name[i] == 'i' or name [i] == 'o' or name[i] == 'u':
        vcount += 1
print(vcount)

numbers = [23, 45, 12, 67, 34, 89, 10]
gtr = numbers[0]
for number in numbers:
    if number > gtr:
        gtr = number
print(gtr)

string = str(input("Enter a string: "))
li1 = list(string)
print(li1)
li2 = reversed(li1)
print(li2)

i = 0
n = 5
j = 1
while i<n and j<n:
    print(j*n)
    i += 1
    j += 1

i = 1 
n = 5
while i<5:
    print(i)

i = 1

while i <= 5:
    for i in range(1, i + 1):
        print(i, end="")
    print()
    i += 1

number = int(input("ENter number: "))
list= []

list.append(number)
a = list
print(a)

numb = (input("Enter number: "))
linumb = list(numb)
a = 3
while a >= 0:
    n = linumb[a]
    print(n)
    a -= 1
