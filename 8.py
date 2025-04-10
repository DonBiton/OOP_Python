 

class Fraction:
    def __init__(self, n1,n2=None): 
        if n2==None:
            self.n1,self.n2=self.translation(n1)
        else:
            self.n1 = n1
            self.n2 = n2
        
    
    def __setattr__(self, key, value):
        if key not in ['n1','n2']:
            raise AttributeError(f"Local attributes are not allowed")
        if self.validate(key, value):
            super().__setattr__(key, value)
        else:  
            raise ValueError('Числа должныбыть целыми и делитеть не может быть равен 0')
        
    
    @classmethod
    def validate(self, key, arg):
        return type(arg)==int and (key!='n2' or arg!=0 )
    

    def __str__(self, val=False ):
        if val==True:
            return round(self.n1/self.n2,3)
        else:
            return f"{self.n1//self.NOD()}/{self.n2//self.NOD()}"
    
    def value(self):
        decimal=self.__str__(True)
        return decimal
    @staticmethod
    def translation(n1):
        n2=1
        while n1%1!=0:
            n1=n1*10
            n2=n2*10
        return int(n1),int(n2)
    @classmethod
    def verify_data(cls, other):
        if not isinstance(other, (int, Fraction)):
            raise TypeError("Операнд справа должен быть целым числом или объектом эксземпляра класса Fraction")
        return other
    
    def NOD(self):
        if self.n1==0 or self.n2==0:
            return 1
        nod = 1
        for i in range(1,min(abs(self.n1),abs(self.n2))+1):
            if self.n1%i==0 and self.n2%i==0:
                nod=i
        return nod
    
    def __add__(self,other):
        other= self.verify_data(other)
        other= other.value()
        return Fraction(self.value()+other)
    def __radd__(self, other):

        return self.__add__(other)  
        
    def __sub__(self,other):
        other= self.verify_data(other)
        other= other.value()  

        return Fraction(self.value()-other)
    def __rsub__(self, other):
        return self.__sub__(other)
    
    def __mul__(self,other):

        other= other.value() if isinstance(other, Fraction) else other
        return Fraction(self.value()*other)
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __truediv__(self,other):
        other= self.verify_data(other)
        other= other.value()          

        return Fraction(self.value()/other)
    def __rtruediv__(self, other):
        other= self.verify_data(other)
        other= other.value()  
        return self.__truediv__(other)
    
    def __ne__(self,other):
        other= self.verify_data(other)
        other= other.value()  
        return self.value()!=other
    
    def __eq__(self,other):
        other= self.verify_data(other)
        other= other.value()          
        return self.value()==other
    
    def __lt__(self,other):
        other= self.verify_data(other)
        other= other.value()  

        return self.value()<other
    
    def __le__(self,other):
        other= self.verify_data(other)
        other= other.value()  

        return self.value()<=other
    
    def __gt__(self,other):
        
        other= self.verify_data(other)
        other= other.value()
        return self.value()>other
    
    def __ge__(self,other):
        other= self.verify_data(other)
        other= other.value()        
        return self.value()>=other
    
    def __hash__(self):
        return hash(self.value())


        

f1 = Fraction(1, 2)
f2 = Fraction(2, 4)
print(f1)
print(f1 + f2)  # 5/4
print(f2 - f2)  # -1/4
print(f1 * f2)  # 3/8
print(f2 / f1)  # 2/3
print(f1.value()) # 0.5


print(f1 == f2)  
print(f1 != f2)  
print(f1 > f2)  
print(f2 < f1)  
print(hash(f1), hash(f2), sep='\n')
print(f1 == f2)
