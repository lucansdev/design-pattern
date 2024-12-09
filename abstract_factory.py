"""
abstract factory e um padrao de criacao que fornece uma interface para criar familias de objetos relacionados ou dependentes sem especificar sua classes concretas. Geralmente abstract factory conta com um ou mais metodos para criar seus objetos

uma diferença importate entre factory method e abstract factory e que a factory usa herança, enquanto a abstract usa composição

principio:programe para interfaces, nao para implementações

"""
from abc import ABC,abstractmethod

#familias sao essa separacao de veiculos
class VeiculoLuxo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None:
        pass

class VeiculoPopular(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None:
        pass


class CarroLuxoZN(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print("carro de luxo ZN esta buscando o cliente")

class CarroPopularZN(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print("carro popular ZN esta buscando o cliente")


class MotoZN(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print("Moto esta buscando ZN o cliente")


class MotoLuxoZN(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print("moto de luxo esta ZN buscando cliente")





class CarroLuxoZS(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print("carro de luxo ZS esta buscando o cliente")

class CarroPopularZS(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print("carro popular ZS esta buscando o cliente")


class MotoZS(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print("Moto esta buscando ZS o cliente")


class MotoLuxoZS(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print("moto de luxo esta ZS buscando cliente")


class VeiculoFactory(ABC):
    @staticmethod
    @abstractmethod
    def get_carro_luxo() -> VeiculoLuxo:
        pass
    @staticmethod
    @abstractmethod
    def get_carro_popular() -> VeiculoPopular:
        pass
    @staticmethod
    @abstractmethod
    def get_moto_luxo() -> VeiculoLuxo:
        pass
    @staticmethod
    @abstractmethod
    def get_moto_popular() -> VeiculoPopular:
        pass
    

class ZonaNorteVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro_luxo() -> VeiculoLuxo:
        return CarroLuxoZN()

    @staticmethod
    def get_carro_popular() -> VeiculoPopular:
        return CarroPopularZN()

    @staticmethod
    def get_moto_luxo() -> VeiculoLuxo:
        return MotoLuxoZN()

    @staticmethod
    def get_moto_popular() -> VeiculoPopular:
        return MotoZN()



class ZonaSulVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro_luxo() -> VeiculoLuxo:
        return CarroLuxoZS()

    @staticmethod
    def get_carro_popular() -> VeiculoPopular:
        return CarroPopularZS()

    @staticmethod
    def get_moto_luxo() -> VeiculoLuxo:
        return MotoLuxoZS()

    @staticmethod
    def get_moto_popular() -> VeiculoPopular:
        return MotoZS()


class Cliente:
    def buscar_cliente(self):
        for factory in [ZonaNorteVeiculoFactory(),ZonaSulVeiculoFactory()]:
            carro_popular = factory.get_carro_popular()
            carro_popular.buscar_cliente()

            carro_luxo = factory.get_carro_luxo()
            carro_luxo.buscar_cliente()

            moto_popular = factory.get_moto_popular()
            moto_popular.buscar_cliente()

            moto_luxo = factory.get_moto_luxo()
            moto_luxo.buscar_cliente()

if __name__ == "__main__":
    cliente = Cliente()
    cliente.buscar_cliente()