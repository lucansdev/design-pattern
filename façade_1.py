"""
façade (fachada) e um padrao de projeto estrutural que tem a intencao de fornecer uma interface unificada para um conjunto de interfaces em um subsistema. façade define uma interface de nivel mais alto que torna o subsistema mais facil de ser usado
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


class WeatherStationFacade:
    def __init__(self) -> None:
        self.weather_statio = WeatherStation()
        self.smartphone = SmartPhone("iphone",self.weather_statio)
        self.samsung = SmartPhone("galaxy",self.weather_statio)
        self.weather_statio.add_observer(self.smartphone)
        self.weather_statio.add_observer(self.samsung)

    def add_observer(self,observer:IObserver) -> None:
        self.weather_statio.add_observer(observer)

    def add_observer(self,observer:IObserver) -> None:
        self.weather_statio.remove_observer(observer)            
    
    def change_state(self,state:Dict) -> None:
        self.weather_statio.state = state

    def reset_state(self) -> None:
        self.weather_statio.reset_state()


if __name__ == "__main__":
    weather_station = WeatherStationFacade()

    weather_station.change_state({"temperature":"30"})
    weather_station.change_state({"humidity":"90%"})

    
