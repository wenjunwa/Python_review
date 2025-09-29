# Match-case statement (switch): an alternative to using many 'elif' statements
#                                execute some code if a value matches a 'case'
#                                Benefits: cleaner and syntax is more readable

def week_day (day):
    if day == 1:
        print("It is Sunday!")
    elif day == 2:
        print("It is Monday!")
    elif day == 3:
        print("It is Tuesday!")
    elif day == 4:
        print("It is Wednsday!")
    elif day == 5:
        print("It is Thursday!")
    elif day == 6:
        print("It is Friday!")
    elif day == 7:
        print("It is Saturday!")
    else:
        print("It is not a valid weekday.")
week_day("i")

#case
def week_day_case (day):
    match day :
        case 1:
            print("It is Sunday!")
        case 2:
            print("It is Monday!")
        case 3:
            print("It is Tuesday!")
        case 4:
            print("It is Wednsday!")
        case 5:
            print("It is Thursday!")
        case 6:
            print("It is Friday!")
        case 7:
            print("It is Saturday!")
        case _:
            print("It is not a valid weekday.")
week_day(2)

def is_weekend (day):
    match day:
        case 1 | 7:
            print("It is a weekend!")
        case 2 | 3 | 4 | 5 | 6 | 7:
            print("It is not a weekend!")
        case _:
            print("It's not a valide weekday!")
is_weekend("1")

