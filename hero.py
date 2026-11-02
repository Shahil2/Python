class Hero:
    def __init__(self):
        self.name="Sharukh"
        self.age=60
        self.numOfMovies=75
    def act(self):
        print("Sharukh is a good actor")

h1=Hero()
print(h1.name)
print(h1.age)
print(h1.numOfMovies)
h1.act()