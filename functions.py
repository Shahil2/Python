# No Parameter no Return
def add():
    a = 10
    b = 20
    c = a + b
    print(c)
add()

# No Parameter with Return
def add():
    a = 10
    b = 20
    c = a + b
    return c

print(add())

# with Parameter no Return
def add(a,b):
    c = a + b
    print(c)
print(add(10,20))

# with Parameter with Return
def add(a,b):
    c = a + b
    return c
res=add(10,20)
print(res)
