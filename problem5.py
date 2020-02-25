a = input("enter a string")
a = a.lower()
b = a.split()
n = b[::-1]
s = " "
s = s.join(n)
s = s.capitalize()
print(s)