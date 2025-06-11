inp = str(input("Enter a Phrase:"))
txt = inp.split()
a = " "
for i in txt:
    a += i[0].upper()
print(a)
