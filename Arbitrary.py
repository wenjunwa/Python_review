# *args     = allows you to pass multiple non-key arguments
# **kwargs  = allows you to pass multiple keyword arguments
#             * unpacking operator
#             1. positional, 2. default, 3.keyword, 4. ARBITRARY

# *args
def add(*nums):
    total = 0
    for num in nums:
        total += num
    return total

print(add(1))

#Display name
def display_name(*args):
    for arg in args:
        print(arg, end=" ")
display_name("Dr.","Spongebob", "Squarepant")
print()

#**kwargs
def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key:10}:    {value}")

print_address(street="123 Fake st.",
              city="Detroit",
              state="MI",
              zip="54321")

# shipping label
def shipping_label(*args, **wkargs):
    for arg in args:
        print(f"{arg}", end=" ")
    print()
    print(wkargs.get("street"))
    print(f"{wkargs.get("city")}, {wkargs.get("state")}, {wkargs.get("zip")}")

shipping_label("Dr.","Spongebob", "Squarepant",
               street="123 Fake st.",
               city="Detroit",
               state="MI",
               zip="54321"
               )