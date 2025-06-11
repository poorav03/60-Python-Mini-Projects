import random
length = int(input("Enter the lenght of the password: "))
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
password ="".join(random.sample(s,length))
print(password)