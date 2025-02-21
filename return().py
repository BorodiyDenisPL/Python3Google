def calculate_fails(failed_attempts, total_attempts):
    fail_percentage = failed_attempts / total_attempts
    return fail_percentage

percentage = calculate_fails(2,4)

if (percentage >= .5):
    print("Account locked.")





def remaining_login_attempts(maximum_attempts, total_attempts):
    return maximum_attempts - total_attempts
remaining_attempts = remaining_login_attempts(3, 3)
if remaining_attempts <= 0:
    print("Your account is locked")




username = "elarson"
print("1:" + username)
def greet():
    username = "bmoreno"
    print("2:" + username)
greet()
print("3:" + username)




security = 1
print(type(security))
