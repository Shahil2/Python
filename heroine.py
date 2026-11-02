class Heroine:
    def __init__(self):
        self.name="Kajal"
        self.age=50
    def Dance(self):
        print("Kajal is a good Dancer")
h1=Heroine()
print(h1.name)
print(h1.age)
h1.Dance()
h1.Movie="Dheera"
print(h1.Movie)
h1.age=55
print(h1.age)
del h1.age
print(h1.age)