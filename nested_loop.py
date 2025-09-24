# nested loop = A loop within another loop(outer, inner)
# outer loop:
#   inner loop:


# for y in range(3):
#     for x in range(1,10):
#         print(x, end="")
#     print()

# print a rectangle
rows = int(input("Enter row number: "))
columns = int(input("Enter column number: "))
symbol = input("Enter symbol: ")

for y in range(rows):
     for x in range(columns):
        print(symbol, end="")
     print()