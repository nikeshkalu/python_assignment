class Nepalese:
    def __init__(self,nationality):
        self.nationality = nationality



class Newari(Nepalese):
    def __init__(self,language,nationality):
        self.language = language
        Nepalese.__init__(self,nationality)

    def getCharacteristics(self):
        return "Some " + self.nationality + " Speak " + self.language + " language"

person = Nepalese(nationality = "Nepal")
man = Newari(nationality = "Nepali", language = "newari")

print(person.nationality)
print("Newari People speak",man.language,"language")
print(man.getCharacteristics())