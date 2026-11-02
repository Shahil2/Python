class Mobile():
    def __init__(self):
        self.brand="Nokia"
        self.color="Blue"
        self.cost=1200
    def call(self):
        print("Mobile is ringing")
m1=Mobile()
print(m1.brand)
print(m1.color)
print(m1.cost)
m1.call()