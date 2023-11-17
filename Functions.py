def greeting():                     #Defining a function
    print("Hello programmer!")

greeting()                          #Calling a function

def addnum():
    print(10+20+30)

addnum()

#Passing argument(s) to parameter(s) of the function
def hello(name):
    print("Hello",name)

hello("John")
name = "Katy"
hello(name)


def fullname(f, l):
    print("Hello",f,l)

fname = "Peter"
lname = "Kevinson"
fullname(fname,lname)


#TYPES OF FUNCTIONS
# 1. built-in function - min(), max(), len(), int(), float(), type()
print(max(55,10,88,20))
x = 10
print(type(x))

# 2. User-defined functions
def hello(name):
    print("Hello",name)

hello("John")

def func(num, num1):
    print(num+1, num1-1)
hello(1,-1)