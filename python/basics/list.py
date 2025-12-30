#length
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#type
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#list constructor
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#negative indexing
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#check if item exist
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#insert item in list
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#append at end of list
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#join two list using extend list to list+
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#join two list with extend list -> tuples, set and dictionary
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#remove second item
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#remove the first item
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#delete the entire list
thislist = ["apple", "banana", "cherry"]
del thislist
#print(thislist) #error will say "thisList is not defined"









