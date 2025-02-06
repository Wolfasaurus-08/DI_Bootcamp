# def say_hello():
#     """prints the str 'hello there'"""
#     print("Hello, there") 

# say_hello()
# #doc strings explain the function
# # def say_hello_greet(username):
# #     print(f"Hello{username}")
# # say_hello_greet('harry')
# #positional and key word arguments,
# def say_hello(username, language):
#     if language == "EN":
#         print("Hello "+username)
#     elif language == "FR":
#         print("Bonjour "+username)
#     elif language == "ru":
#         print(f'priviet'{username})

#     else:
#         print("This language is not supported: " + language)

# say_hello("Rick", "FR")
# #key word arguments

def calculate(price,quantity):
    print(price*quantity)
calculate (15,25)