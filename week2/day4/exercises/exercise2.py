# # Instructions
# import json
# sampleJson = """{ 
#    "company":{ 
#       "employee":{ 
#          "name":"emma",
#          "payable":{ 
#             "salary":7000,
#             "bonus":800
#          }
#       }
#    }
# }"""


# # Access the nested “salary” key from the JSON-string above.
# # Add a key called “birth_date” to the JSON-string at the same level as the “name” key.
# # Save the dictionary as JSON to a file.
import json

# Sample JSON string
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

# Load the JSON string into a Python dictionary
data = json.loads(sampleJson)

# Access the nested "salary" key
salary = data["company"]["employee"]["payable"]["salary"]
print("Salary:", salary)

# Add a new key "birth_date" to the employee dictionary
data["company"]["employee"]["birth_date"] = "1990-01-01"  # Example birth date

# Save the modified dictionary as JSON to a file
with open("modified_employee.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

print("Modified JSON saved to modified_employee.json")
