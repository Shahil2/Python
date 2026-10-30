class student:
    def __init__(self):
        self.name="Peter"
        self.age=21
        self.usn=46
        self.gender="Male"
    def study(self):
        print("Peter is not studying")
s1=student()
print(s1.name)
print(s1.age)
print(s1.usn)
print(s1.gender)
s1.study()
