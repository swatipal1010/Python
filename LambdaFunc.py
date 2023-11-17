#Lambda function also called Anonymous Function -- Created without a name
multi = lambda x:x*2
print(multi(8))

add = lambda a,b:a+b
print(add(10,9))

def add2(a,b):
    return a+b
print(add2(11,7))

#To check is the given number is Odd or Even
oddeven = lambda num: True if num%2 == 0 else False
print(oddeven(100))
