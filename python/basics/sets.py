#Access item in sets
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

#Add item to set
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

#merge one set to another set
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

#merge one set to any tuples,list, distionaries
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

#remove item using remove : if the item doesnt exist it will throw error
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

#remove item using discard : if the item doesnt exist it will not throw error : Safe use
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

#join multiple sets with assigned to new set
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)
print(myset)

#join set and tuple assign to another value
x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)

#keep only duplicates : intersection or & will return a new set, contains only duplicates
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)

#keep only duplicates: intersection_update will modify the exisitng set
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)

