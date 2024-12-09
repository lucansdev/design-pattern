"""
command tem intencao de encapsular uma solicitacao como um objeto, desta forma permitindo parametrizar clientes com diferentes solicitacoes ,enfileirar ou fazer registro (log) de solicitacoes e suportar operacoes que podem ser desfeitas

e formado por um cliente (quem orquestra tudo) , um invoker (que invoca as solicitacoes), um ou varios objetos de comando (que fazem ligacao entre o receiver e a acao a ser executada) e um receiver (o objeto que vai executar  a acao no final)
"""
from __future__ import annotations
from abc import ABC,abstractmethod
from typing import List,Dict,Tuple

class Light:
    """receiver"""
    def __init__(self,name:str,room_name:str)-> None:
        self.name = name
        self.room_name = room_name
        self.color = "default color"

    def on(self) -> None:
        print(f" light {self.name} in {self.room_name} is now ON")

    def off(self) -> None:
        print(f" light {self.name} in {self.room_name} is now OFF")

    def change_color(self,color:str) -> None:
        self.color = color
        print(f" light {self.name} in {self.room_name} is now {self.color}")


class ICommand(ABC):
    """interface"""
    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def undo(self) -> None:
        pass


class LightOnCommand(ICommand):
    def __init__(self,light:Light):
        self.light = light

    def execute(self) -> None:
        self.light.on()

    def undo(self):
        self.light.off()


class LightChangeColor(ICommand):
    def __init__(self,light:Light,color:str):
        self.light = light
        self.color = color
        self.old_color = self.light.color

    def execute(self) -> None:
        self.old_color = self.light.color
        self.light.change_color(self.color)

    def undo(self):
        self.light.change_color(self.old_color)


class RemoteController:
    """invoker"""
    def __init__(self):
        self._buttons:Dict[str,ICommand] = {}
        self.undos:List[Tuple[str,str]] = []
        
    
    def button_add_command(self,name:str,command:ICommand) -> None:
        self._buttons[name] = command

    def button_execute(self,name:str) -> None:
        if name in self._buttons:
            self._buttons[name].execute()
            self.undos.append((name,"execute"))

    def button_undo(self,name:str) -> None:
        if name in self._buttons:
            self._buttons[name].undo()
            self.undos.append((name,"undo"))

    def global_undo(self):
        if not self.undos:
            return
        button_name , action = self.undos[-1]

        if action == "execute":
            self._buttons[button_name].undo()
        else:
            self._buttons[button_name].execute()


        self.undos.pop()


if __name__ == "__main__":
    bedroom_light = Light("luz do quarto","quarto")
    bathroom_light = Light("luz do banheiro","banheiro")

    bedroom_light_on = LightOnCommand(bedroom_light)
    bathroom_light_on = LightOnCommand(bathroom_light)
    bedroom_light_blue = LightChangeColor(bedroom_light,"blue")
    bedroom_light_red = LightChangeColor(bedroom_light,"red")

    remote = RemoteController()
    remote.button_add_command("first_button",bedroom_light_on)
    remote.button_add_command("second_button",bathroom_light_on)
    remote.button_add_command("third_button",bedroom_light_blue)
    remote.button_add_command("fourth_button",bedroom_light_red)

    remote.button_execute("first_button")
    remote.button_undo("first_button")

    remote.button_execute("second_button")
    remote.button_undo("second_button")

    remote.button_execute("third_button")
    remote.button_undo("third_button")

    remote.button_execute("fourth_button")
    remote.button_undo("fourth_button")

    print()

    remote.global_undo()