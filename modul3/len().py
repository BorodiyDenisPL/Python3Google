new_string = "123345"
print(len(new_string))




device_id_length = len("h32rb17")
if device_id_length == 7:
    print("The device ID has 7 characters.")




# Assign `employee_id` to a four digit number as an initial value

employee_id = 4186

# Reassign `employee_id` to the same value but in the form of a string

employee_id = str(employee_id)

# Display the `employee_id` as it currently stands

print(employee_id)

# Conditional statement that updates the `employee_id` if its length is less than 5 digits

if len(employee_id) < 5:
    employee_id = "E" + employee_id  
    
# Display the `employee_id` after the update
    
print(employee_id)