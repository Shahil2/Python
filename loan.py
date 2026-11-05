class farmer:
    def __init__(self,p,t,r):
        self.principle=p
        self.time=t
        self.rate=r
    def loan(self):
        si=(self.principle*self.time*self.rate)/100
        print(si)
f1=farmer(200000,2,2.5)
f2=farmer(100000,1,2.5)
f1.loan()
f2.loan()
