#Tuples (ORDERED & IMMUTABLE) 
tuple1 = (1,2,5)
print(type(tuple1))
print(tuple1)
print(tuple1[1])                    #Access element from the tuple

'''
// Gives error because tuple cannot be assigned value -> IMMUTABLE
tuple1[0]=0
print(tuple1)
'''

#Nested tuple
nestTuple = ("hello",(5,8,2))
print(nestTuple[1][1])

#Negative indexing
nestTuple = ("hello",(5,8,2))
print(nestTuple[-1][-2])


#Adding the tuple
x = (1,2,3)+(1,2,3)
print(x)

y = (1,2,3)+(4,5,6)
print(y)