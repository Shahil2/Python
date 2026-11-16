class calci:
    def opt(self,a,b):
        return a+b,a-b,a*b,a/b
c1=calci()
r1,r2,r3,r4=c1.opt(20,10)
print(f'{r1}\n{r2}\n{r3}\n{r4}')
