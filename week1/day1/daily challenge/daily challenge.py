#Using the input function, ask the user for a string. The string must be 10 characters long.
#If it’s less than 10 characters, print a message which states “string not long enough”.
#If it’s more than 10 characters, print a message which states “string too long”.
#If it’s 10 characters, print a message which states “perfect string” and continue the exercise.
string=input("write me a string ")
digit_num = len(string)
if digit_num>10:
    print("that string is too long")
elif digit_num<10:
    print ("that string is not long enough")
else:
    print ("just right")
    #Then, print the first and last characters of the given text
    print (string[0])
    print (string[-1])
    #Using a for loop, construct the string character by character:
    for i in range(digit_num):
        print(string[0:i])
