#access tuples
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#check if item exists
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

#tuples are immutable , workaround : change from tuples to list then convert to tuples
x = ("apple","hari","khizar","vino")
y = list(x)

y[0]="praveen"
x = tuple(y)
print(x)

#add tuple to a tuple: create a single item tuple with comma or else its not a tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

#delete a tuple
thistuple = ("apple", "banana", "cherry")
del thistuple
#print(thistuple) #this will raise an error because the tuple no longer exists

#!!!!!unpack tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

#unpack using *astrek if number of variable doesnt match the tuple use an asterisk to collect remaining
fruits = ("apple", "banana", "cherry")
(green, *red) = fruits
print(green)
print(red)

#If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

#iterate thorugh for loop
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
for i in range(len(fruits)):
  print("iterating fruits using for loop with index number "+fruits[i])

#count method in tuples
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)

#index find the occuranece of any value
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)

