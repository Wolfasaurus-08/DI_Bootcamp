from faker import Faker

# Create an instance of the Faker class
fake = Faker()

# Create an empty list called users
users = []

# Function to add new dictionaries to the users list
def add_user(users_list, num_users=1):
    for _ in range(num_users):
        user = {
            "name": fake.name(),
            "address": fake.address(),
            "language_code": fake.language_code()
        }
        users_list.append(user)

# Example: Add 5 new users to the users list
add_user(users, 5)

# Print the users list to see the fake data
for user in users:
    print(user)
