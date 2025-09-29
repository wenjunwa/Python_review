# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built - in
import math
# local variable first:

from math import e
def fun1 ():
    # local variable
    #a = 1
    #print(a)

    def fun2():
        #locat variable
        a =2
        print(a)

    fun2()
#global variable
a = 5
fun1()

def func3():
    e = math.e
    print(e)
e = 10
func3()


