class Laptop:
    def __init__(self):
        self.brand='HP'
        self.color='Black'
    def display(self):
        self.type="OLED"
       # type="LED"
l1=Laptop()
print(l1.brand)
print(l1.color)
l1.display()
print(l1.type)
l1.cost=40000
print(l1.cost)
