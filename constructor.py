# Constructor :
class cse1:
    
    def __init__(self,a,b):
        self.a1=a
        self.b1=b
        # self.a=20
        # self.b=30
        print("im constructor")
    def strength(self):
        print("THe strength is 101")
        self.s=101
        
    def kn(self,c,d):
        print("The knowledge is good")
        self.know="Good"
        pro=c+d
        print(pro)
        
    def details(self):
        print("THe current Strength and Knowledge")
        c_s=self.s-10
        print(c_s,self.know)
        print(self.a+self.b)
        
day_2=cse1(2,3)
print("from below is making function call")
day_2.strength()
day_2.kn(2,10)
day_2.details()