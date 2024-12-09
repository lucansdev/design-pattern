"""
iterator e um padrao comportamental que tem a intencao de fornecer um meio de acessar,sequencialmente, os elementos de um objeto agregado sem expor sua representacao subjacente.

- uma colecao deve fornecer um meio de acessar seus elementos sem expor sua estrutura interna
- uma colecao pode ter maneiras e percursos diferentes para expor seus elementos
- voce deve separar a complexidade dos algoritmos de iteracao da colecao emsi 

a ideia principal do padrao e retirar a responsabilidade de acesso e percuso de uma colecao, delegando tais tarefas para um objeto iterador.
"""
from __future__ import annotations
from typing import List,Any
from collections.abc import Iterator,Iterable

class MyIterator(Iterator):
    def __init__(self,collection:List[Any]) -> None:
        self._collection = collection
        self._index = 0

    def next(self):
        try:
            return self.__next__()
        except StopIteration:
            return None
    
    def __next__(self):
        try:
            item = self._collection[self._index]
            self._index += 1
            return item
        except IndexError:
            raise StopIteration


class ReverseIterator(Iterator):
    def __init__(self,collection:List[Any]) -> None:
        self._collection = collection
        self._index = -1

    
    def next(self):
        try:
            return self.__next__()
        except StopIteration:
            return None

    def __next__(self):
        try:
            item = self._collection[self._index]
            self._index -= 1
            return item
        except IndexError:
            raise StopIteration


class MyList(Iterable):
    def __init__(self) -> None:
        self._items:List[Any] = []
        self._iterator = MyIterator(self._items)

    def add(self,value:Any)-> None:
        self._items.append(value)

    def __iter__(self) -> None:
        return self._iterator

    def reverse_iterator(self):
        return ReverseIterator(self._items)

    def __str__(self) ->str:
        return f"{self.__class__.__name__}{self._items}"

if __name__ == "__main__":
    mylist = MyList()
    mylist.add("lucas")
    mylist.add("bruna")
    mylist.add("farias")




for value in mylist:
    print(value)

print()

for value in mylist.reverse_iterator():
    print(value)

