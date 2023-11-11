#String(Sequence of Characters) in Python 
str1 = "Hello"          #Single line string
print(str1)
print(str1[2])


#Multi-line string
str2 = '''
Hey Everyone!
Let's learn Python.
Isn't it interesting?
'''
print(str2)

#string slicing  -> (slice method)
slice_str = "My name is Programmer"
print(slice_str[0:10])
print(slice_str[2:14])
print(slice_str[-1])
print(slice_str[0:])
print(slice_str[:14])
print(slice_str[-1:])
print(slice_str[0:12:2])   #Characters from index 0 to 9 gets printed but with a gap of 2(Every second character from the character you're on currently)

#Reverse a string -> (revere method)
rev_str = "Hello Everyone"
print(rev_str[::-1])