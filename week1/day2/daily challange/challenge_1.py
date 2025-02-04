#Ask the user for a number and a length.
#Create a program that prints a list of multiples of the number until the list length reaches length.
number=int(input("choose a number:  "))
length=int(input("chose a length:  "))
multiples=[]
for x in range(number, length*number+1, number):
    multiples.append(x)
print(multiples)