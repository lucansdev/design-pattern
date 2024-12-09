"""
GoF - memento e um padrao de projeto comportamental que tem a intencao de permitir que voce salve e restaure um estado anterior de um objeto originator sem revelar os detalhes da sua implementacao e sem violar o encapsulamento

originator e o objeto que deseja salvar seu estado.memento e usado para salvar o estado do originator. caretaker e usado para armazenar mementos.carataker tambem e usado com o padrao command.
"""
from __future__ import annotations
from typing import Dict,List
from copy import deepcopy

class Memento:
    def __init__(self,state:Dict) -> None:
        self._state:Dict 
        super().__setattr__("_state",state)

    def get_state(self) -> Dict:
        return self._state
    
    def __setattr__(self, name, value):
        raise AttributeError("sorry,i am immutable")
    
class ImageEditor:
    def __init__(self,name:str,widht:int,height:int) ->None:
        self.name = name
        self.widht = widht
        self.height = height

    def save_state(self) -> Memento:
        return Memento(deepcopy(self.__dict__))
    
    def restore(self,memento:Memento) ->None:
        self.__dict__ = memento.get_state()

    def __str__(self):
        return f"{self.__class__.__name__}{self.__dict__}"


class Caretaker:
    def __init__(self,originator:ImageEditor):
        self._originator = originator
        self._mementos:List[Memento] = []


    def backup(self)->None:
        self._mementos.append(self._originator.save_state())

    def restore(self) -> None:
        if not self._mementos:
            return
        self._originator.restore(self._mementos.pop())



if __name__ == "__main__":
    img = ImageEditor("foto_1.jpg",111,111)
    caretaker = Caretaker(img)
    caretaker.backup()

    img.name = "fot_2.jpg"
    img.widht = 222
    img.height = 222
    caretaker.backup()

    img.name = "fot_3.jpg"
    img.widht = 333
    img.height = 333
    caretaker.backup()

    img.name = "fot_4.jpg"
    img.widht = 444
    img.height = 444
    caretaker.restore()

    print(img)