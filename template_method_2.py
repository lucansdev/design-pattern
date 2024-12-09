from __future__ import annotations
from abc import ABC,abstractmethod

class Pizza(ABC):
    """class abstrata"""

    def prepare(self):
        """template method"""
        self.hook_before_add_ingredients() #hook
        self.add_ingredients() #abstract
        self.hook_after_add_ingredients() #hook
        self.cook() #abstract
        self.cut() #concreto
        self.serve() #concreto

    def hook_before_add_ingredients(self):pass
    def hook_after_add_ingredients(self):pass

    def cut(self):
        print(f"{self.__class__.__name__}: cortando pizza.")
    
    def serve(self):
        print(f"{self.__class__.__name__}: servindo pizza.")
        
    @abstractmethod
    def add_ingredients(self):pass
    
    @abstractmethod
    def cook(self):pass


class aModa(Pizza):
    def add_ingredients(self):
        print(f"aModa:presunto,queijo,goiabada")   

    def cook(self):
        print(f"aMod: cozinhando por 45 minutos no forno a lenha")

class Veg(Pizza):
    def hook_before_add_ingredients(self):
        print(f"veg: lavando os ingredientes")

    def add_ingredients(self):
        print(f"veg: ingredientes veganos")   

    def cook(self):
        print(f"veg: cozinhando por 5 minutos no forno comum")


if __name__ == "__main__":
    a_moda = aModa()
    a_moda.prepare()

    print()

    veg = Veg()
    veg.prepare()