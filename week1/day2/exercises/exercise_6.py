 #Exercise 6 : While Loop
#Instructions
#Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.
while True:
  name_guess = input('whats the name?')
  if name_guess == "Anne":
    print('Congrats! You win!')
    break
  else:
    print('try again')