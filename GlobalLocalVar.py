#Local Variables are those variables which are defined inside the function
def hello():
    x = "hello"                     #Local Variable
    print(x)
hello()

#print(x)                            #Gives error here because 'x' doesn't lies in this scope


def hello1():
    global y                           #Variable 'y' is made global
    y = "Hii"                     
    print(y)
hello1()

print(y)                               #Since local var is made global, this gives no error


def hello2():
    print(y)                           #We can use the local var (made global) in another function with no error



num = 100                              #Global variable
def add(a):
    num = 20
    print("Sum of",a,"and",num,"is:",a+num)
add(50)
print(num)


#To change the value of a global variable inside a function, refer to the variable by using the global keyword
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()                                #This will change the value of x to "fantastic"

print("Python is " + x)