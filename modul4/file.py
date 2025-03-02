with open("/home/coolman/123.txt", "r") as file:
    file_text = file.read()
print(file_text)




line = "jrafael,192.168.243.140,4:56:27,True"
with open("/home/coolman/123.txt", "w") as file:
    file.write(line)





