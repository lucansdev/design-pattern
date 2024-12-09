"""
monostate (ou borg) - e uma variação do singleton proposto por alex martelli que tem a intenção de garantir que o estado do objeto seja igual para toda as instancias
"""

class StringRprMixin:
    def __str__(self):
        params = ", ".join([f"{k}={v}" for k,v in self.__dict__.items()])
        return f"{self.__class__.__name__}({params})"
    
    def __repr__(self):
        return self.__str__()

class A(StringRprMixin):
    def __init__(self):
        self.x = 10
        self.y = 20

class MonoState(StringRprMixin):
    _state = {"x":10,"y":10}

    def __init__(self,nome=None,sobrenome=None):
        self.__dict__ = self._state
        if nome is not None:
            self.nome = nome

        if sobrenome is not None:
            self.sobrenome = sobrenome
        

if __name__ == "__main__":
    m1 = MonoState(nome="lucas")
    m2 = MonoState(sobrenome="andrade")
    print(m1)
    print(m2)