from __future__ import annotations
from abc import ABC,abstractmethod

class Sound:
    def __init__(self):
        self.mode:PlayMode = RadioMode(self)
        self.playing = 0

    def change_mode(self,mode:PlayMode):
        self.playing = 0
        self.mode = mode
        print("mudando para o estado: ",self.mode.__class__.__name__)

    def press_next(self) -> None:
        self.mode.press_next()
        print(self)

    def press_prev(self) -> None:
        self.mode.press_prev()
        print(self)

    def __str__(self) -> str:
        return str(self.playing)

class PlayMode(ABC):
    def __init__(self,sound:Sound) -> None:
        self.sound = sound

    @abstractmethod
    def press_next(self) -> None:pass

    @abstractmethod
    def press_prev(self) -> None: pass

class RadioMode(PlayMode):
    def press_next(self):
        self.sound.playing += 1000

    def press_prev(self):
        self.sound.playing -= 1000 if self.sound.playing > 1 else 0

class MusicaMode(PlayMode):
    def press_next(self):
        self.sound.playing += 1000

    def press_prev(self):
        self.sound.playing -= 1000 if self.sound.playing > 1 else 0


if __name__ == "__main__":
    sound = Sound()
    sound.press_next()
    sound.press_next()
    sound.press_prev()


    print()
    sound.change_mode(MusicaMode(sound))