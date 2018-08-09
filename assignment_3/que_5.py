class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def CalcArea(self):
        return self.length*self.width

    @property
    def tuple(self):
        return self.length,self.width


    @tuple.setter
    def tuple(self,_tuples):
        self.length,self.width = _tuples



a = Rectangle(length=10,width=20)
print(a.CalcArea())

a.tuple = (20,30)
print(a.tuple)

