# basic value types 
  #strings, integers, floats, and booleans

#string functions 
 # indexes
#name='johnathan'
#print(name[2:4])
#len( ) prints the length of the char including space 
#print(len('harry potter'))
#name='anne calabrese'
#print (name[2])
#print (name[1])
#print (name[1:3])

#print(name.capitalize())
#print (name.title())
#print(name.upper())
#my_mar_name=name.replace('calabrese', 'wolf')
#print(my_mar_name)

#user_name=' happy banana'
#cleaned_user_name=user_name.strip()
#print(cleaned_user_name)

#price='$100'
#cleaned_price = price.strip('$')
#print (cleaned_price)

#numbers
#print (4/2)
#print (5%2)
#score=0
#score+=1
#print(score)
#user_age=input('tell me your age')#output is always a string
#typeecasting changes the type of value
#user_age_int=int(user_age)
#print(user_age_int+7)
#print ("hello world\n"*4)
first_name= "anne"
last_name= "wolf"
full_name=first_name+' '+last_name
print (full_name)

#f-string
print(f"hello my name is {first_name} {last_name}")
#take the name of the user #
# check if the user name is a this same as yours
# # if so print "we have the same name
user_name= input("whats your name")
if user_name == 'anne':
    print ("that's my name")
elif user_name=="daniel":
    print("great name")
else:
    print ("we have a different name")