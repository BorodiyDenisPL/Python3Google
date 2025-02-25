my_list = ["a", "b" , "c"]
my_bist = [1,2,3]
print(my_bist + my_list)




ip_adresses = ["192.168.1.1", "154.145.1.2"]
networks = []
for adress in ip_adresses:
    networks.append(adress[0:3])
print(networks)



username_list = ["bmoreno", "wjaffrey", "tshah", "sgilmore"]
print("Before appending an element:", username_list)
username_list.append("btang")
print("After appending an element:", username_list)



numbers_list = []
print("Before appending a sequence of numbers:", numbers_list)
for i in range(10):
    numbers_list.append(i)
print("After appending a sequence of numbers:", numbers_list)
