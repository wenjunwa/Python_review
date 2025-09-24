# default arguments =   A default value for certain parameters
#                       default is used when that argument is omitted
#                       make your functions more flexible, reduce # of arguments
#                       1. positional, 2. DEFAULT, 3. keyword, 4. arbitrary

# default argument
# def net_price(list_price, discount=0, tax= 0.085):
#     return list_price*(1-discount)*(1+tax)
# print(net_price(500))
# print(net_price(500,0.1, 0))

import time

def count(end, start = 1):
    for x in range(start, end + 1):
        print(x)
        time.sleep(1)
    print("Done!")
count(10)
