"""
chain of responsability (COR) e um padrao comportamental  que tem a intencao de evitar o acoplamento do remetente de uma solicitacao ao seu receptor, ao dar a mais de um objeto a oportunidade de tratar a solicitacao.
Encadear os objetos receptores passando a solicitacao ao longo da cadeia ate que um objeto a trate
"""
from __future__ import annotations
from abc import ABC,abstractmethod

class Handler(ABC):
    def __init__(self) -> None:
        self.sucessor:Handler

    @abstractmethod
    def handle(self,letter:str) -> str:pass


class HandlerABC(Handler):
    def __init__(self,sucessor:Handler) -> None:
        self.letters = ["A","B","C"]
        self.sucessor = sucessor

    def handle(self, letter) -> str:
        if letter in self.letters:
            return f"handlerABC: conseguiu tratar o valor {letter}"
        return self.sucessor.handle(letter)
    
class HandlerDEF(Handler):
    def __init__(self,sucessor:Handler) -> None:
        self.letters = ["D","E","F"]
        self.sucessor = sucessor

    def handle(self, letter) -> str:
        if letter in self.letters:
            return f"handlerDEF: conseguiu tratar o valor {letter}"
        return self.sucessor.handle(letter)
    

class HandlerUnsolved(Handler):
    def handle(self, letter) -> str:
        return f"handlerUnsolved: nao conseguiu tratar {letter}"
    
    
if __name__ == "__main__":
    handler_unsolved = HandlerUnsolved()
    handler_def = HandlerDEF(handler_unsolved)
    handler_abc = HandlerABC(handler_def)
        
    print(handler_abc.handle("A"))
    print(handler_abc.handle("D"))
    print(handler_abc.handle("C"))
    print(handler_abc.handle("D"))
    print(handler_abc.handle("E"))
    print(handler_abc.handle("F"))