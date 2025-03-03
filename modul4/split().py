approved_users = "elarson,bmoreno,tshah,sgilmore,eraab"
print("before .split():", approved_users)
approved_users = approved_users.split(",")
print("after .split():", approved_users)






with open("123.txt", "r") as file:
    updates = file.read()
updates = updates.split()
print(updates)