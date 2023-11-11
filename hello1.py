print("Hello, world!")

#Numbers in python
num1 = 10       #Integer
num2 = 11.5     #Float
num3 = 2+5j     #Complex number

print("Datatype of ",num1, "is: ", type(num1))
print("Datatype of ",num2, "is: ", type(num2))
print("Datatype of ",num3, "is: ", type(num3))


#max function
num1a, num1b, num1c = 2,8,5
print(max(num1a,num1b,num1c))


#min function
num2a, num2b, num2c = 3.9,8.6,13.5
print(min(num2a,num2b,num2c))

print(max(num1a,num1b,num1c,num2a,num2b,num2c))


#Implicit TYpe conversion
x = 12.6
y = 5
z = x+y
print("Sum of ",x,"+",y,"is: ",z,"and the resulting datatype is: ",type(z))

#Explicit datatype conversion
num1d = 12
str1 = "Python"
result = str(num1d)+str1
print(result)

#Mutli-line string
str2 = '''
Hello Everyone!
Namaste!
Hola!
'''
print(str2)


'''PRODUCES VALUE ERROE AS int() EXPECTS A VALID INTEGER NUMBER AS ITS ARGUMENT
num1d = 12
str1 = "Python"
result = num1d+int(str1)
print(result)
'''


#Taking input from user
numA = int(input("Enter the first number: "))
numB = int(input("Enter the second number: "))
sumAB = numA+numB
print("Sum of ",numA,"+",numB,"is: ",sumAB)


#Aritmetic operations on Numbers
a = 100
b = 25
random = 12
c = a+b
print("Sum of ",a,"+",b,"is: ",c)
print("Difference of ",a,"-",b,"is: ",a-b)
print("Product of ",a,"*",b,"is: ",a*b)
print("Division of ",a,"/",b,"is: ",a/b)
print("Modulus of ",a,"%",random,"is: ",a%random)
print("Floor division of ",a,"//",random,"is: ",a//b)


#Comparison Operations
print(numA,">",numB,":",numA>numB)
print(numA,"<",numB,":",numA<numB)
print(numA,">=",numB,":",numA>=numB)
print(numA,"<=",numB,":",numA<=numB)
print(numA,"==",numB,":",numA==numB)
print(numA,"!=",numB,":",numA!=numB)

#Logical Operators
log1 = True
log2 = False
print(log1,"and",log2,":",log1 and log2)
print(log1,"or",log2,":",log1 or log2)
