#while loop
#i=0
#while i<5:
    #print(1)
    #i+=1
#fruits = ['apple', 'banana', 'kiwi', 'pear']
#i=0
#while i< len(fruits):
    #print(fruits[i])
    #i+=1
pizza_order =[]
max_pizza=5 
while len(pizza_order)<(max_pizza):
    flavor =input('which flavor?(if you are finished type"done")')

    if flavor == 'done':
        print ("succesfully added")
        print (pizza_order)
        print ('we will deliver your pizza in 30 min')
        break
    pizza_order.append(flavor)