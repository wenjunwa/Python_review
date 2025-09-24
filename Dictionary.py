# dictionary = a collection of {key: value} pairs
#               ordered and changeable. No duplicates

capital = {"USA": "Washington D.C.",
           "India": "New Delhi",
           "China": "Beijing",
           "Russia": "Moscow"}

# print(capital.get("Japan"))
#
# if capital.get("Japan"):
#     print("That capital exit")
# else:
#     print("Thant capital does not exit")

# capital.update({"Germany":"Berlin"})
# capital.update(({"USA":"Detroit"}))
# capital.pop("China")
# capital.popitem()
# capital.clear()

print(capital.keys())
print(capital)

for key in capital.keys():
    print(key)

for value in capital.values():
    print(value)
items = capital.items()
print(items)
for key, value in capital.items():
    print(f"{key} : {value}")