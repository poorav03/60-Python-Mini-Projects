def convert(s):
    f = float(s)
    c = (f-32)* 5/9
    return c
inp = input("Enter the Fahrenheit value: ")
print(convert(inp))
