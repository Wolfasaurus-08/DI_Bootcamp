# class Door:
#     def __init__(self):
#         self.is_opened= True
#     def open_door(self):
#         self.is_opened= True
#     def close_door(self):
#         self.is_opened= False
# class BlockedDoor(Door):
#     def __init__(self):
#         super(Door).is_opened= False
#     def open_door(self):
#         self.is_opened= True
#         print("a blocked door cannot be opened")
#         print (f"the door is open{self.is}")
    
#     def close_door(self):
#         self.is_opened= False
class Computer():

    def __init__(self):
        self.name = "Apple Computer" # public
        self.__max_price = 900 # private

    def sell(self):            # public method
        print(f"Selling Price: {self.__max_price}")

    def __sell(self):          # private method
      print('This is private method')

    def set_max_price(self, price):
        self.__max_price = price

c = Computer()
c.sell()
c.set_max_price(5000)
c.sell()