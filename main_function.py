# if __name__ == __main__: (this script can be imported OR run standalone)
#                           Functions and classes in this module can be reused
#                           without the main block of code executing
# Good practices (Code is modular,
#                 helps readability,
#                 avoid unintended execution)

# ex. library = import library for functionality
#               when running library directly, display a help page

from main_function2 import *

def favorite_food(food):
    print(f"Yor favorite food is {food}.")

def main():
    print("this is main_function")
    favorite_food("apple")
    favorite_drink("Beer")
    print("Goodbye!")

if __name__ == '__main__':
    main()

