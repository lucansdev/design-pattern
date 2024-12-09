"""
o singleton tem a intencao de garantir que uma classe tenha somente uma instancia e fornece um ponto global de acesso para a mesma.
"""

class AppSettings:
    _instance = None


    def __new__(cls,*args,**kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls,*args,**kwargs)
        return cls._instance
    
    def __init__(self) -> None:
        self.tema = "o tema escuro"
        self.font = "18px"

if __name__ == "__main__":
    as1 = AppSettings()
    as1.tema = "o tema claro"
    print(as1.tema)

    as2 = AppSettings()
    print(as2.tema)