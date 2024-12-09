def sigleton(the_class):
    instace = {}
    def get_class(*args,**kwargs):
        if the_class not in instace:
            instace[the_class] = the_class(*args,**kwargs)
            return instace[the_class]
    return get_class

@sigleton
class AppSettings:
    def __init__(self) -> None:
        self.tema = "o tema escuro"
        self.font = "18px"

if __name__ == "__main__":
    as1 = AppSettings()
    as1.tema = "o tema claro"
    print(as1.tema)

    as2 = AppSettings()
    print(as2.tema)