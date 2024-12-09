from typing import Any,Dict


#class Meta(type):
#    def __call__(cls, *args: Any, **kwds: Any) -> Any:
#        return super().__call__(*args, **kwds)
    
#class Pessoa(metaclass=Meta):
#    def __new__(cls,*args,**kwargs):
#        return super().__new__(cls)

#    def __init__(self,nome) -> None:
 #       self.nome = nome

 #   def __call__(self, x,y) -> Any:
#        print("call chamado",self.nome, x+y)


#p1 = Pessoa("luiz")
#p1(2,2)
#print(p1.nome)

class Singleton(type):
    _instances:Dict = {}

    def __call__(cls,*args,**kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args,**kwargs)
            return cls._instances[cls]

class AppSettings(metaclass=Singleton):    
    def __init__(self):
        self.tema = "o tema escuro"
        self.font = "18px"

if __name__ == "__main__":
    as1 = AppSettings()
    as1.tema = "o tema claro"
    as2 = AppSettings()
    print(as2.tema)