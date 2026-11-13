class car:
    def __init__(self):
        self.brand = "BMW"
    def start(self):
        print("Car is starting")
    @staticmethod
    def move():
        print("Car is moving")
    @classmethod
    def stop(cls):
        print("Car is stopping")

c1=car()
print(c1.brand)
c1.start()
c1.move()
c1.stop()
car.move()
car.stop()
car.start()