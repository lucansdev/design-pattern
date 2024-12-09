#factory method(e um padarao de criacao que permite definir uma interface para criar objetos,mas deixa a subclasses decidirem que objetos criar)
from abc import ABC,abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None:
        pass


class CarroLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print("carro de luxo esta buscando o cliente")



class CarroPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print("carro popular esta buscando o cliente")


class Moto(Veiculo):
    def buscar_cliente(self) -> None:
        print("Moto esta buscando o cliente")


class MotoLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print("moto de luxo esta buscando cliente")


class VeiculoFactory(ABC):
    def __init__(self,tipo) -> None:
        self.carro = self.get_carro(tipo)
    @staticmethod
    @abstractmethod
    def get_carro(tipo:str) -> Veiculo:
        pass

    def buscar_cliente(self):
        self.carro.buscar_cliente()

class ZonaNorteVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo:str) -> Veiculo:
        if tipo == "luxo":
            return CarroLuxo()
        if tipo == "popular":
            return CarroPopular()
        if tipo == "moto":
            return Moto()
        if tipo == "moto_luxo":
            return MotoLuxo()
        
        assert 0,"veiculo nao existe"


class ZonaSulVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo:str) -> Veiculo:
        if tipo == "popular":
            return CarroPopular()
        
        
        assert 0,"veiculo nao existe"


if __name__ == "__main__":
    from random import choice
    veiculos_disponiveis_zona_norte = ["luxo","popular","moto","moto_luxo"]
    veiculos_disponiveis_zona_sul = ["popular"]

    print("zona sul")
    for i in range(10):
        carro1 = ZonaSulVeiculoFactory(choice(veiculos_disponiveis_zona_sul))
        carro1.buscar_cliente()

    print("zona norte")
    for i in range(10):
        carro2 = ZonaNorteVeiculoFactory(choice(veiculos_disponiveis_zona_norte))
        carro2.buscar_cliente()