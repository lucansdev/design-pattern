"""
strategy e um padrao de projeto comportamental que tem a intencao de definir uma familia de algoritmos,encapsular cada uma delas e torna-las intercambiaveis.strategy permite que o algoritmo varie independentemente dos clientes que o utilizam.

principio:
entidades devem ser abertas para extensao,mas fechadas para modificação
"""
from __future__ import annotations
from abc import ABC,abstractmethod

class Order:
    def __init__(self,total:float,discount:DiscountStrategy):
        self._total = total
        self._discount = discount


    @property
    def total(self):
        return self._total

    @property
    def total_with_discount(self):
        return self._discount.calculate(self.total)


class DiscountStrategy(ABC):
    @abstractmethod
    def calculate(self,value:float)-> float:
        pass


class twentyPercent(DiscountStrategy):
    def calculate(self, value:float) -> float:
        return value - (value * 0.2)

class fiftyPercent(DiscountStrategy):
    def calculate(self, value:float) -> float:
        return value - (value * 0.5)


class NoDiscount(DiscountStrategy):
    def calculate(self, value:float) -> float:
        return value

class CustomDiscount(DiscountStrategy):
    def __init__(self,discount):
        self.discount = discount / 100

    def calculate(self, value:float) -> float:
        return value - (value  * self.discount)

if __name__ == "__main__":
    twentypercent = twentyPercent()
    fiftypercent = fiftyPercent()
    no_discount = NoDiscount()
    five_Discount = CustomDiscount(5)

    order = Order(1000,twentypercent)
    print(order.total,order.total_with_discount)

    order = Order(1000,fiftypercent)
    print(order.total,order.total_with_discount)

    order = Order(1000,no_discount)
    print(order.total,order.total_with_discount)

    order = Order(1000,five_Discount)
    print(order.total,order.total_with_discount)

