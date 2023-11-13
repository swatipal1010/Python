#Dictionary (KEY-VALUE PAIR, UNORDERED, MUTABLE AND DON'T ALLOW DUPLICATES)

dict1 = {
    "name":"John",
    "age":25,
    "work_As":"Programmer",
    "Company":"Microsoft"
    }
print(dict1["name"], "work as", dict1["work_As"],"in",dict1["Company"])


#New Key-Pair assignment at the end of the dictionary
dict1["SirName"] = "Levi"
print(dict1)

#Printing keys
print(dict1.keys())

#Printing values
print(dict1.values())

#Storing multiple values in a key
dict2 = {"fruit":"apple","vegetable":["carrot","potato","onion"],"color":"red"}
print(dict2["vegetable"])
print(dict2["vegetable"][1])