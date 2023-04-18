#tuples is a sequence of immutable objects.
#tuples are unchangeable,ordered and allows duplicate
#we use paranthesis to initialize a tuple

thistuple = ("apple", "banana", "cherry")
print(thistuple)

#tuple length  # determines how many items a tuple has.

a = ("apple", "banana", "cherry")
print(len(a))

#loop through a tuple
#for loop  #Iterate through the items and print the values:
b = ("apple", "banana", "cherry")
for x in b:
  print(x)

  #join tuples
  # using the +operator
  tuple4 = (1,2,3,4,5,6)
  tuple5= ("a","b","c","d")
  tuple6= tuple4+tuple5
  print(tuple6)

  #multiplying tuples  #repeates a tuple a numberof times  to create a new tuple
  fruits = ("apple", "banana", "cherry")
  tuple1= fruits * 2

  print(tuple1)

#sets  //a sequence of python objects
#to create set we use curly braces
#set is unordered,unchangeable,and don't allows duplicates

#length of set  #returns the  number of items in a set
fruits = {"apple", "banana", "cherry"}

print(len(fruits))

#add set items  #adds items in a set
x = {"apple", "banana", "cherry","melon","lemon"}
x.add("orange")
print(x)

#update  #it add items in a set #the method does not have to be a set,it can be dict,tuple
list = {"apple", "banana", "cherry"}
list1 = ["kiwi", "orange"]

list.update(list1)

print(list)

#remove set tems
z = {"apple", "banana", "cherry"}
z.remove("banana")
print(z)

#we can also use pop #removes the last item in a set
fru = {"apple", "banana", "cherry"}
y = fru.pop()
print(y) #removed item
print(fru) #the set after removal

#loop through set
#for loop
a = {"cow","goat","sheep","hen","cock"}
for x in a:
  print(x)

#join sets
#  union () //returns a set that containing all values in two set duplicate excluded 
s = {10,20,30,10,30,40,50}
s1 ={10,20,30,40,50,40}
s3 = s.union(s1)
print(s3)

#intersection()# returns a set contain values that exist in both set
s = {10,20,30,10,30,40,50}
s1 ={10,20,30,40,50,40}
s3 = s.intersection(s1)
print(s3)

#difference() #returns a set of values that are in the first set but not in the second
s = {10,20,30,10,30,40,50,70}
s1 ={10,20,30,40,50,40}
s3 = s.difference(s1)
print(s3)

#dictionary #it is a sequence of key and value pairs.
#dictionary are ordered,changeable and do not allow duplicates
#Example
#dictionary length #returns the length of a dictionary
fruits = {"mango":3,"apple":10,"banana":54}
print(len(fruits))

#removing items from a list
#pop() #removes the item with the specified key name
fruits = {"mango":3,"apple":10,"banana":54}
fruits.pop("banana")
print(fruits)

#What I have learned
#how to add,remove,join and loop through sets,tuples,dictionary
#Dictionary contain a key and a value
#I have learned that set,dictionaries are mutable while tuple immutable 




