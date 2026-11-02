print("Different Variable Different Values")
a,b,c,d=10,20,30,40
print(a)
print(id(a))
print(b)
print(id(b))
print(c)
print(id(c))
print(d)
print(id(d))

print("Different variable Repeated Values")

a,b,c,d=10,20,10,40
print(a)
print(id(a))
print(b)
print(id(b))
print(c)
print(id(c))
print(d)
print(id(d))

print("Same variable Different Values")

a,a,a=10,20,30
print(a)
print(id(a))

