# ABSTRACTION
# Clasa abstractă FormaGeometrica
# Conține un field PI=3.14
# Conține o metodă abstractă aria (opțional)
# Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai
# probabil am colturi’
from abc import abstractmethod,ABC
class FormaGeometrica(ABC):
    PI = 3.14
    @abstractmethod
    def aria(self):
        pass
    @staticmethod
    def descriere():
        print('Cel mai probabil am colturi')

FormaGeometrica.descriere()


# INHERITANCE
# Clasa Pătrat - moștenește FormaGeometrica
# constructor pentru latură
# ENCAPSULATION
# latura este proprietate privată
# Implementează getter, setter, deleter pentru latură
# Implementează metoda cerută de interfață (opțional, doar dacă ai ales să
# implementezi metoda abstractă aria)

class Patrat(FormaGeometrica):
    __latura = 0
    def __init__(self,latura):
        self.latura = latura
    def aria(self):
        self.aria = self.latura**2
        print(self.aria)
    def get_latura(self):
        return self.__latura
    def set_latura(self,latura_setata):
        self.__latura = latura_setata
    def del_latura(self):
        self.__latura= None
# Implementează metoda cerută de interfață (opțional, doar dacă ai ales să
# implementezi metoda abstractă aria)
patrat = Patrat(5)
patrat.aria()
print(patrat.get_latura())
patrat.set_latura(10)
print(patrat.get_latura())
patrat.del_latura()
print(patrat.get_latura())

# Clasa Cerc - moștenește FormaGeometrica
# constructor pentru rază
# raza este proprietate privată
# Implementează getter, setter, deleter pentru rază
# Implementează metoda cerută de interfață - în calcul folosește field PI
# mostenit din clasa părinte (opțional, doar dacă ai ales să implementezi metoda
# abstractă aria)
# POLYMORPHISM
# Definește o nouă metodă descrie - printează ‘Eu nu am colturi’

class Cerc(FormaGeometrica):
    def __init__(self,raza):
        self.__raza = raza
    def get_raza(self):
        return self.__raza
    def set_raza(self,set_raza):
        self.__raza = set_raza
    def del_raza(self):
        self.__raza = None
    def aria(self):
        self.aria = self.PI*self.__raza**2
        print(self.aria)
    def descriere(self):
        print('Eu nu am colturi')

cerc = Cerc(10)
cerc.aria()
cerc.set_raza(5)
print(cerc.get_raza())
cerc.del_raza()
print(cerc.get_raza())
cerc.descriere()




