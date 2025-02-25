
print("Hello"[1:4])
# ell
 

print("Hello".upper()[1:4])
# ELL 

print("Hello".index("e"))


device_id = "h32rb17"
print("h32rb17"[0])
print(device_id[0])





# Assign `url` to a specific URL

url = "https://exampleURL1.com"

# Extract the protocol of `url` along with the syntax following it, display the result
print(url[0:8])



# Assign `url` to a specific URL

url = "https://exampleURL1.com"

# Display the index where the domain extension ".com" is located in `url`

print(url.index(".com"))




"""Вы хотите найти индекс, с которого начинается подстрока "192.168.243.140" в строке, содержащейся 
в переменной ip_addresses. Выполните код Python, чтобы найти и вывести на экран начальный индекс.
 (Если Вы хотите отменить свои изменения в коде, Вы можете нажать кнопку Reset)"""

ip_addresses = "192.168.140.81, 192.168.109.50, 192.168.243.140"
print(ip_addresses.index("192.168.243.140"))




username_list = ["elarson", "fgarcia", "tshah", "sgilmore"]
print(username_list[0:2])