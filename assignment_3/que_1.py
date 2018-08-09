class Strings:
    def __init__(self , string):
        self.string = string


    def getString(self):
        str = input("enter any string:")
        self.string = str

    def printString(self):
        a = self.string
        print(a.upper())



a=Strings(string="")
a.getString()
a.printString()
