#Useful in situations where exceptions may occur

try:
    if name > 3:
        print("hello")
except:
    print("An error occured. Please check your code.")


#The 'except' block executing for specific error
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")


#'else' keyword is used to execute a code if no error occurs
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")               #This will be executed if no error occurs



#'finally' keyword is used to execute a code no matter if there is an exception or not
try:
  print(x)
except:
  print("Something went wrong")
finally:                                    #This will be executed no matter what
  print("The 'try except' is finished")


#Raise an exception
x = -1
if x < 0:
  raise Exception("Sorry, no numbers below zero")     #This will raise an error if x is less than 0


#Raise a TypeError if x is not an integer
x = "hello"
if not type(x) is int:
    raise TypeError("Only integers are allowed")        #This will raise an error if x is not an integer



#Nested Try and Except
try:
  print(x)
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")
finally:
    try:
        print(y)
    except:
        print("Something went wrong")
    else:
        print("Nothing went wrong")
