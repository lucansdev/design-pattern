"""
template method (comportamental) tem a intencao de definir um algoritmo em um metodo,postergando alguns passos para as subclasses por heranca. template method permite que subclasses redefinam certos passos de um algoritmo sem mudar a estrutura do mesmo.

tambem e possivel definir hooks para que as subclasses utilizem caso necessario

the hollywood principle: "don't call us,we'll call you." (ioc - inversao de controle)
"""
from __future__ import annotations
from abc import ABC,abstractmethod

class Abstract(ABC):
    def template_method(self):
        self.hook()
        self.operation1()
        self.base_class_method()
        self.operation2()

    def hook(self):pass

    def base_class_method(self):
        print("OLA SOU DA CLASS ABSTRATA E SEREI EXECUTADO TAMBEM")

    @abstractmethod
    def operation1(self):pass

    @abstractmethod
    def operation2(self):pass

class ConcreteClass(Abstract):
    def hook(self):
        print("user o hook")

    def operation1(self):
        print("operacao 1 concluida")
    
    def operation2(self):
        print("operacao 2 concluida")

class ConcreteClass2(Abstract):
    def operation1(self):
        print("operacao 1 concluida (de maneira diferente)")
    
    def operation2(self):
        print("operacao 2 concluida (de maneira diferente)")



if __name__ == "__main__":
    c1 = ConcreteClass()
    c1.template_method()

    c2 = ConcreteClass2()
    c2.template_method()