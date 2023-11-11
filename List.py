#List (ODERED AND MUTABLE) in Python
list1 = [1,2,3]
print(type(list1))
print(list1)
print(list1[2])

#print(list[3])  --> Gives Index Out of Range Error


#To print all the elements in the list
print("Elements in the list are: ")
for i in list1:
    print(i)

#Nested list
nestList = [4,8,[10,7,12],20]
print("Element at nestList[2][1] in the list",nestList, "is:",nestList[2][1])

#Insert the new item at the beginning of the list -> (insert method)
num1 = list1.insert(0,55)
print(list1)
list1[1] = 9
print(list1)

#List can contains mix datatypes 
list2 = [4,10.8,"Apple"]
list2.insert(1,"Grapes")
print(list2)

#Append the item to the last of the list -> (append method)
list2.append(22)
print(list2)

#To combine the two lists -> (extend method)
list1.extend(list2)
print(list1)
list2.extend(list1)
print(list2)

#To list the length of the list -> (len method)
print("The length of",list2,"is: ",len(list2))


#To return the index of the item from the list -> (index method)
print("Printing the index of Apple from the list1: ")
print("List1: ",list1)
print("Index of Apple in list1 is:",list1.index("Apple"))


#Count the number of occurances of the item in the list -> (count method)
list3 = [5,8,2,4,10,5,2,5,10,2]
print("In list",list3,"2 appears ",list3.count(2),"times")


#Remove an item from the list using item name -> (remove method)
lang = ["English","Hindi","French","German"]
print("List before removal of any item: ",lang)
lang.remove("French")
print("List after removal of French language: ",lang)


#Remove an item from the list from list using index of the item -> (pop method)
lang = ["English","Hindi","French","German"]
print("List before removal of any item; ",lang)
lang.pop(1)
print("List after removal of Hindi language is",lang)


#Reverse the elements of the list -> (reverse method)
lang = ["English","Hindi","German","French"]
lang.reverse()
print("List after being reversed: ",lang)


#Sort the items of the list -> (sort method)
#Bydefault - In ascending order
sort_list= [8,5,6,10,45,22,1,9]
print("List before sorting:",sort_list)
sort_list.sort()
print("List after sorting: ",sort_list)


#Sorting the list items in descending order
sort_list= [8,5,6,10,45,22,1,9]
sort_list.sort(reverse=True)
print("List items in descending order: ",sort_list)









