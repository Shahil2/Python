class farmer:
    r =2.5
    def __init__(self,p,t):
        self.principle=p
        self.time=t
    def loan(self):
        si = (self.principle*self.time*farmer.r)/100
        print(si)
f1= farmer(200000,3)
f2= farmer(300000,3)
f1.loan()
f2.loan()
print(farmer.r)