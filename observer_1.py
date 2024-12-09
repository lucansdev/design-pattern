"""
o padrao observer tem a intencao de definir uma dependencia de um-para-muitos entre objetos, de maneira que quando um objeto muda de estado, todo os seus dependentes sao notificados e atualizados automaticamente.

um observer e um objeto que gostaria de ser informado,um observable (subject) e a entidade que gera as informacoes
"""
from __future__ import annotations
from abc import ABC,abstractmethod
from typing import List,Dict

class IObservable(ABC):
    @property
    @abstractmethod
    def state(self):
        pass
    
    @abstractmethod
    def add_observer(self,observer:IObserver) -> None:
        pass

    @abstractmethod
    def remove_observer(self,observer:IObserver) -> None:
        pass

    @abstractmethod
    def notify_observers(self) -> None:
        pass


class WeatherStation(IObservable):
    def __init__(self):
        self._observers :List[IObserver] = []
        self._state:Dict = {}
    
    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self,state_update:Dict) ->None:
        new_state:Dict = {**self._state,**state_update}

        if new_state != self._state:
            self._state = new_state
            self.notify_observers()

    def reset_state(self):
        self._state = {}
        self.notify_observers()

    def add_observer(self,observer:IObserver) -> None:
        self._observers.append(observer)

    
    def remove_observer(self,observer:IObserver) -> None:
        if observer not in self._observers:
            return
        self._observers.remove(observer)

    
    def notify_observers(self) -> None:
        for observer in self._observers:
            observer.update()


class IObserver(ABC):
    @abstractmethod
    def update(self) -> None:pass


class SmartPhone(IObserver):
    def __init__(self,name,observable:IObservable) -> None:
        self.name = name
        self.observable = observable

    def update(self):
        observable_name = self.observable.__class__.__name__
        print(f"{self.name} o objeto {observable_name} acabou de ser atualizado => {self.observable.state}")
        

if __name__ == "__main__":
    weather_statio = WeatherStation()
    smartphone = SmartPhone("iphone",weather_statio)
    samsung = SmartPhone("galaxy",weather_statio)
    weather_statio.add_observer(smartphone)
    weather_statio.add_observer(samsung)

    weather_statio.state = {"temperature":"30"}
    weather_statio.state = {"humidity":"90%"}

    weather_statio.reset_state()