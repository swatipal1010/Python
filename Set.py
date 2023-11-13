#Sets(UNORDERED & IMMUTABLE, DON'T ALLOW DUPLICATE VALUES)
set1 = {2,3,1,0,15,9}
print(type(set1))       #Results are not displayed in the same order as we have described in the set
print(set1)

# print(set1[1])        //Gives error because the set is unordered so we can't access the item at a particular index

'''
//Gives error because set cannot be assigned value -> IMMUTABLE
set1[0] = 100
print(set1)
'''

#Prints the duplicate elements only once
set2 = {11,2,5,20,2,3,2,5} 
print(set2)

#To add an item in the set using -> add() method
set2.add(50)
print(set2)

#Multiple items can be added using -> update() method
set2.update([100,200,300])
print(set2)

#To remove an item from the set using -> remove() method
set2.remove(100)
print(set2)


#Set Opeartions
# 1.UNION
setX = {0,1,2,3}
setY = {3,4,5}
print(setX|setY)

# 2.INTERSECTION
print(setX&setY)