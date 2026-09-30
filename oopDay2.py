class Fraction:
    # parameterized constructor
    def __init__(self,x,y):
        self.num=x
        self.den=y

# magic method-write config code
    def __str__(self):
        return'{}/{}'.format(self.num,self.den) 
    def __add__(self,a):
        new_num=self.num*a.den + a.num*self.den
        new_den=self.den*a.den
        return'{}/{}'.format(new_num,new_den)

    def __sub__(self,a):
        new_num=self.num*a.den - a.num*self.den
        new_den=self.den*a.den
        return'{}/{}'.format(new_num,new_den)
fr1=Fraction(3,4)
fr2=Fraction(1,2)
print(fr1)
print(fr2)    
print(fr1+fr2) 
print(fr1-fr2)
