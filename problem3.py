a = [1, 2, 3, 2, 0, 65, 21, 4, 2, 10]
b = int(input("enter the key"))
c = []
for i,j in enumerate(a):
  if b==j:
    c.append(i)
print(c)
