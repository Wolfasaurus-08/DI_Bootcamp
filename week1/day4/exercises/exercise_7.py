from random import randint
# def get_random_temp():
#    return (randint(-10,40))
# def main():
#     temp=get_random_temp()
#     print (f"The temperature right now is {temp} degrees celsius.")
def get_random_temp(season):
   if season=="winter":
       return (randint(-10,16))
   elif season=="spring":
       return (randint(16,32))
   elif season =="summer":
       return (randint(32,40))
   elif season=="autumn":
       return (randint(16,32))
   else:
       return ('define season')

def main(season):
    temp=get_random_temp(season)
    print (f"The temperature right now is {temp} degrees celsius.")
    if temp <=0:
        print("Bundle up it's Freezing!")
    elif temp <= 16:
        print ("you may want to wear a coat")
    elif temp<=23:
        print("It's not too hot, not too cold. All you need is a light jacket,")
    elif temp <=32:
        print ("its beautiful, go take a walk!")
    else:
        print("go home, its too hot to function.")
main ("winter")
main ("spring")
main ("summer")
main ("autumn")

