#Exercise 8: Who ordered a pizza ?
#Instructions
#Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
#As they enter each topping, print a message saying you’ll add that topping to their pizza.
#Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).
pizza_order =[] 
while True:
    topping =input('what toppings do you want? (if you are finished type"done") ')

    if topping != 'done':
        print (f"succesfully added {topping}")
        pizza_order.append(topping)
    else:
        break

for topping in pizza_order:
    print(topping)

print(f"The total price is {10 + (2.5* len(pizza_order))}")
