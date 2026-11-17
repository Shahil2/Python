class student:
    def __init__(self,name,age,usn):
        self.name=name
        self.age=age
        self.usn=usn
    def disp(self):
        print(f'Name = {self.name} Age = {self.age} USN = {self.usn}')
s1 = student('Shahil',22,7559)
s2 = student('Peter',22,5588)
s1.disp()
s2.disp()