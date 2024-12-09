"""
o padrao de projeto state e um padrao comportamental que tem a intencao de permitir a um objeto mudar seu comportamento quando o seu estado interno muda.
o objeto parecera ter mudado sua classe.
"""
from __future__ import annotations
from typing import Dict,List
from abc import ABC,abstractmethod

class Order:
    """context"""
    def __init__(self) -> None:
        self.state:OrderState = PaymentPending(self)

    def pending(self):
        print("tentando executar pending()")
        self.state.pending()
        print("estado atual: ",self.state)
        print()

    def approve(self):
        print("tentando executar approve()")
        self.state.approve()
        print("estado atual: ",self.state)
        print()

    def reject(self):
        print("tentando executar reject()")
        self.state.reject()
        print("estado atual: ",self.state)    
        print()

class OrderState(ABC):
    def __init__(self,order:Order) -> None:
        self.order = order


    @abstractmethod
    def pending(self) ->None:pass

    @abstractmethod
    def approve(self) -> None:pass

    @abstractmethod
    def reject(self) -> None:pass

    def __str__(self):
        return self.__class__.__name__

class PaymentPending(OrderState):
    def __init__(self,order:Order) -> None:
        self.order = order

    def pending(self) ->None:
        print("pagamento pendente,nao posso fazer nada")
    
    def approve(self) -> None:
        self.order.state = PaymentApproved(self.order)
        print('pagamento aprovado!')
        
    def reject(self) -> None:
        self.order.state = PaymentReject(self.order)
        print("pagamento recusado!")

class PaymentApproved(OrderState):
    def __init__(self,order:Order) -> None:
        self.order = order

    def pending(self) ->None:
        self.order.state = PaymentPending(self.order)
    
    def approve(self) -> None:
        print("pagamento ja aprovado,nao posso fazer nada")
        
    def reject(self) -> None:
        self.order.state = PaymentReject(self.order)

class PaymentReject(OrderState):
    def __init__(self,order:Order) -> None:
        self.order = order

    def pending(self) ->None:
        print("pagamento recusado,nao posso mover para pedente")
    
    def approve(self) -> None:
        print("pagamento recusado,nao posso mover para aprovado")

    def reject(self) -> None:
        print("pagamento ja rejeitado!")

if __name__ == "__main__":
    order = Order()
    order.pending()
    order.approve()
    order.pending()
    order.reject()
    order.pending()
    order.approve()
    order.reject()