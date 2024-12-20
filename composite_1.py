"""
Composite é um padrão de projeto estrutural que permite que
você utilize a composição para criar objetos em estruturas
de árvores. O padrão permite aos clientes tratarem de maneira
uniforme objetos individuais (Leaf) e composições de
objetos (Composite).

IMPORTANTE: só aplique este padrão em uma estrutura que possa
ser representada em formato hierárquico (árvore).

No padrão composite, temos dois tipos de objetos:
Composite (que representa nós internos da árvore) e Leaf
(que representa nós externos da árvore).

Objetos Composite são objetos mais complexos e com filhos.
Geralmente, eles delegam trabalho para os filhos usando
um método em comum.
Objetos Leaf são objetos simples, da ponta e sem filhos.
Geralmente, são esses objetos que realizam o trabalho
real da aplicação.
"""

from __future__ import annotations
from abc import ABC,abstractmethod
from typing import List

class BoxStructure(ABC):
    """component"""
    @abstractmethod
    def print_content(self) -> None:pass

    @abstractmethod
    def get_price(self) -> float:pass

    def add(self,child:BoxStructure) -> None:
        pass

    def remove(self,child:BoxStructure) ->None:
        pass


class Box(BoxStructure):
    """composite"""
    def __init__(self,name):
        self.name = name
        self._children:List[BoxStructure] = []

    def print_content(self) -> None:
        for child in self._children:
            child.print_content()

    def get_price(self) -> float:
        return sum([child.get_price() for child in self._children])

    def add(self,child:BoxStructure) -> None:
        self._children.append(child)

    def remove(self,child:BoxStructure) ->None:
        if child in self._children:
            self._children.remove(child)


class Product(BoxStructure):
    """leaf"""
    def __init__(self,name,price)->None:
        self.name = name
        self.price = price
    
    def print_content(self) -> None:
        print(self.name,self.price)

    def get_price(self) -> float:
        return self.price


if __name__ == "__main__":
    camiseta1 = Product("camiseta1",49.90)
    camiseta2 = Product("camiseta2",19.90)
    camiseta3 = Product("camiseta3",10.90)


    caixa_camisetas = Box("caixa de camisetas")
    caixa_camisetas.add(camiseta1)
    caixa_camisetas.add(camiseta2)
    caixa_camisetas.add(camiseta3)


    smartphone1 = Product("smartphone1",9000)
    smartphone2 = Product("smartphone2",11000)

    caixa_smartphones = Box("caixa de smartphones")
    caixa_smartphones.add(smartphone1)
    caixa_smartphones.add(smartphone2)

    caixa_grande = Box("caixa grande")
    caixa_grande.add(caixa_camisetas)
    caixa_grande.add(caixa_smartphones)
    caixa_grande.print_content()
    print(caixa_grande.get_price())

