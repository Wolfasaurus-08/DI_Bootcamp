from random import randint

def number_compare():
    a = int(input('pick a number between 1 and 100 '))
    computer_number = randint(1,100)
    if a == computer_number:
        print (f"success!{a} is the number!")
    elif a>100:
        print ("under 100 dummy! ")
    else:
        print (f"you failed, the computer number is {computer_number}, your number is {a}.")

number_compare()
number_compare()
number_compare()
number_compare()
number_compare()
number_compare()
number_compare()
number_compare()
number_compare()

