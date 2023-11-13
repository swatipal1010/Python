#Conditionals

#If-else
num = 3
if num < 5:
    print(num,"is less than 5")
else:
    print(num,"is greater than 5")


#If-elif-else
num = 5
if num < 5:
    print(num,"is less than 5")
elif num == 5:
    print(num,"is equal to 5")
else:
    print(num,"is greater than 5")



#To check whether the number is even or odd
num = 10
if num%2 == 0:
    print(num,"is even")
else:
    print(num,"is odd")


#While loop
i = 1
while i <= 5:
    print(i)
    i += 1

#For loop
print("Numbers from 0 to 4:")
for i in range(5):
    print(i)            #Prints 0 to 4


print("Numbers from 1 to 5:")
for i in range(1,6):
    print(i)            #Prints 1 to 4


#Program to print the sum of first 5 natural numbers
sum=0
for i in range (6):
    sum = sum+i
print("Sum of first 5 natural numbers is:",sum)


#Program to print the even numbers from the list
list1 = [2,5,8,10,13,17,20,22]
print("Even numbers from the list",list1,"are:")
for i in list1:
    if i%2 == 0:
        print(i)

print("Odd numbers from te list",list1,"are:")
for i in list1:
    if i%2 == 1:
        print(i)


#Program to print the sum of even numbers from the list
sum = 0
for i in list1:
    if i%2 == 0:
        sum = sum+i
print("Sum of even numbers from the list",list1,"is:",sum)


#Program to print the elements of the list
list = [1,55.8,"hello"]
print("Elements in the list",list,"are: ")
for item in list:
    print(item)