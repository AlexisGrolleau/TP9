class BlankSapling:
    def __init__(self,weight = 0,weightdeco = 0,decoration = []):
        self.__weight = weight
        self.__weightdeco = weightdeco
        self.__decoration = decoration

    def getWeight(self): return self.__weight
    def getWeightDeco(self): return self.__weightdeco

    def setWeight(self,weight):
        self.__weight = weight
    def setWeightDeco(self,weightDeco):
        self.__weightdeco = weightDeco

    def addDeco(self,myDeco):
        self.__weightdeco += myDeco.getWeight()
        self.__decoration.append(myDeco)
    def delDeco(self,myDeco):
        self.__weightdeco -= myDeco.getWeight()
        self.__decoration.remove(myDeco)

    def print(self):
        print(f"Ce sapin de noel peut supporter {self.__weight}g de décorations")
        if self.__weightdeco == 0:
            print(f"Il ne contient actuellement aucune décorations")
        else:
            print(f"Il contient actuellement {self.__weightdeco}g de décorations listées ci-après :")
            for i in self.__decoration:
                i.print()
        print(120*"-")


class Decoration:
    def __init__(self,color,weight):
        self._color = color
        self._weight = weight

    def getWeight(self): return self._weight
    def getColor(self): return self._color

    def print(self):
        pass

class Boule(Decoration):
    def __init__(self,color,weight,diam):
        Decoration.__init__(self,color,weight)
        self.__diam = diam

    def getDiam(self): return self.__diam
    def setDiam(self,diam):
        self.__diam = diam
    def print(self):
        print(f"* Boule {self._color} de {self.__diam} cm de diamètre, pesant {self._weight}g")

class Guirlande(Decoration):
    def __init__(self, color, weight, length):
        Decoration.__init__(self,color,weight)
        self._length = length

    def getLenght(self): return self._length

    def setLenght(self,length):
        self._length = length

    def print(self):
        print(f"* Guirlande {self._color} de {self._length}cm de long, pesant {self._weight}g")

class GuirlandeLight(Guirlande):
    def __init__(self, color, weight, length, numberlight):
        Guirlande.__init__(self,color, weight, length)
        self.__number = numberlight

    def getNumber(self): return self.__number

    def setNumber(self,number): self.__number = number

    def print(self):
        print(f"* Guirlande lumineuse {self._color} de {self._length}cm de long, possédant {self.__number} lumières pesant {self._weight}g")


monSapin = BlankSapling()
monSapin.setWeight(2650)
monSapin.print()
maBoule = Boule("bleu", 50, 15)
maGuirlande = Guirlande("rouge",50,10)
maGuirlandeLumineuse = GuirlandeLight("Violette mais pas trop",150,300,5960)
monSapin.addDeco(maBoule)
monSapin.addDeco(maGuirlande)
monSapin.addDeco(maGuirlandeLumineuse)
monSapin.print()
monSapin.delDeco(maGuirlandeLumineuse)
monSapin.print()

