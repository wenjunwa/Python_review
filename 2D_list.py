#2D list: could be list of lists, list of tuples.
#2D tuples: could be tuple of tuples, tuple os lists, tuple of sets
# fruits =        ["apple", "orange", "banana", "coconut"]
# vegetables =    ["celery", "carrots", "potato"]
# meats =         ["chicken", "fish", "turkey"]
#
# #groceries = [fruits, vegetables, meats]
# groceries = [["apple", "orange", "banana", "coconut"],
#              ["celery", "carrots", "potato"],
#              ["chicken", "fish", "turkey"]]
#
# #index of 2D list
# print(groceries[0][1])
#
# #trasverse of a 2D list
# for collection in groceries:
#     for item in collection:
#         print (item, end=" ")
#     print()

#practice: create a keypad
pad = ((1,2,3),
       (4,5,6),
       ('*',9,'#'))
for row in pad:
    for symbol in row:
        print(symbol,end=" ")
    print()

