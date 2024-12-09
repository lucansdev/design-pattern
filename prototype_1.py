"""
especificar os tipos de objetos a serem criados usando uma instancia-prototipo e criar novos objetos pela copia desse prototipo

quais objetos sao copiados com o sinal de atribuição?
"""
from __future__ import annotations
from copy import deepcopy

class StringRprMixin:
    def __str__(self):
        params = ", ".join([f"{k}={v}" for k,v in self.__dict__.items()])
        return f"{self.__class__.__name__}({params})"
    
    def __repr__(self):
        return self.__str__()

class Person(StringRprMixin):
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.adresses = []
    
    def add_address(self,address:Address):
        self.adresses.append(address)

class Address(StringRprMixin):
    def __init__(self,street,number):
        self.street = street 
        self.number = number


if __name__ == "__main__":
    luiz = Person("luiz","miranda")
    endereco_luiz = Address("av.brasil","250A")
    luiz.add_address(endereco_luiz)

    esposa_luiz = deepcopy(luiz)
    esposa_luiz.firstname = "leticia"


    print(luiz)
    print(esposa_luiz)