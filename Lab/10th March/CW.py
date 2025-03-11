#if else
from dataclasses import dataclass

if 2>3:
    print("I am rich")
else:
    print("I am poor")
#for loop
for i in range(2,10,2): #Range(Start, Stop, Step)
    print(i)

#Match case
a=100
match(a):
    case 1:
        print("One")
    case 5:
        print("Five")
    case 10:
        print("Ten")
    case _: #default
        print("Default")

#Data Structure
"""
List - Mutable, ordered, allow duplicates
Tuples - Immutable, ordered, allow duplicates
Set - immutable(can add and remove but no modify), unordered, No duplicates
Dictionary - mutable, ordered, no duplicates
"""
#List
myList = ["Zobaer", 22, 3.50]
for i in myList:
    print(i, end= " ")
#Add a element in the list at the last index
myList.append(199)
#Specific index you want
myList.insert(2,200)
myList[1] = "Ahmed"
#To remove the last data (Follows lifo by default)
myList.pop()
#To remove specific data
myList.remove("Zobaer")
#To seeee the length of the list
print("\nThe length", len(myList))
print("\n",myList)

#Sorting
myList2 = [5, 1, 7, 8, 10]
myList2.sort()
print("The sorted list is", myList2)