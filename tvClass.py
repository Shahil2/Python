class Tv:
    def __init__(self):
        self.brand='LG'
        self.cost=80000
    def Display(self):
        print("Display is broken")
        print(self)
t1=Tv()
print(t1.brand)
print(t1.cost)
t1.Display()
print(t1)