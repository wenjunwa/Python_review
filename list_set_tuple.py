# collection =single "variable" used to store multiple values
#   list = [] ordered and changeable. duplication is ok
#   set = {} unordered and immutable, but Add/Remove is ok. No duplication.
#   Tuple = () ordered and unchangeable. Duplication is OK, Faster
from os import remove
from wsgiref.util import application_uri

# # index lists like strings
# fruits = ["apple", "orange", "banana", "coconut"]
# print(fruits[:3])
#
# # iterate a list
# for fruit in fruits:
#     print(fruit)
#
# # show list of methods with dir
# print(dir(fruits))
#
# # show description of methods with help
# print(help(fruits))
#
# # show number of items in a list with len()
# print(len(fruits))
#
# # use an in function to see if an item is in a list
# print("peach" in fruits)
#
# # change an element in a list
# fruits[0] = "peach"
# print(fruits)
#
# # append an element with an append()
# fruits.append("apple")
# print(fruits)
#
# # remove an element with remove()
# fruits.remove("apple")
# print(fruits)
#
# # insert an item to an index location
# fruits.insert(2, "pineapple")
# print(fruits)
#
# #sort a list
# fruits.sort()
# print(fruits)
#
# #reverse a list
# fruits.reverse()
# print(fruits)
#
# # # clear a list
# # fruits.clear()
# # print(fruits)
#
# # return an index of an item
# print(fruits.index("peach"))
#
# # count the number of duplicates in an list
# fruits.append("banana")
# print(fruits.count("banana"))

#Set practice
# fruit_set = {"apple", "orange", "banana", "coconut"}
# print(fruit_set)
# print("coconut" in fruit_set)
# print(len(fruit_set))
# fruit_set.add("pineapple")
# print(fruit_set)
# fruit_set.remove("pineapple")
# print(fruit_set)
# # fruit_set.pop()
# # print(fruit_set)
# fruit_set.add("banana")
# print(fruit_set)

#Tuple practice
fruit_tuple = ("apple", "orange", "banana", "coconut", "coconut")
print(len(fruit_tuple))
print(fruit_tuple.count("coconut"))

#iterate a tuple
for fruit in fruit_tuple:
    print(fruit)

