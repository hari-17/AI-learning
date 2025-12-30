#dictionaries items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

#dictionaries never allow duplicate with length
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(f"length of dic {len(thisdict)}")
print(f"dictionary content {thisdict}")

#access item from dictionaries & get the key values
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
y = thisdict.get("model")
keys = thisdict.keys()
values = thisdict.values()
items = thisdict.items()
print(f"first way through key : {x} and second way through get: {y}")
print(f"list keys of thisdict: {keys}")
print(f"list value of thisdict: {values}")
print(f"list items of thisdict: {items}")

#check if key exists
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")


#update dictionary : update only accept anothe dictionary to dictionary to get updated
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year":2018})
print(thisdict)

#pop method removes speicifed key
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

#popitem used to remove last inserted item
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

#####Note########
#clear always clear the dictionary and del always delete the whole existense of the dictionary

#loop through keys
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)
  #or
for x in thisdict.keys():
  print(x)

#loop through values
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(thisdict[x])
  #or
for x in thisdict.values():
  print(x)

#loop through keys and values
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(f"Key : {x} && Value: {thisdict[x]}")

#or
for x,y in thisdict.items():
  print(x,y)


#create three dict, then create one dic that will contain the other three dict
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)

#loop through nested dict
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}


for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(f"{y} : {obj[y]}")



