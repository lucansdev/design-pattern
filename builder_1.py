"""
builder e um padrao de criação que tem a intencao de separar a construcao de um objeto complexo da sua representacao,de modo que o mesmo processo de construcao possa criar diferentes representações.

builder te da a possibilidade de criar objetos passo a passo e isso ja e possivel no python sem este padrao

geralmente o builder aceita o encadeamento de metodos(method chaining)
"""
from abc import ABC,abstractmethod

class StringRprMixin:
    def __str__(self):
        params = ", ".join([f"{k}={v}" for k,v in self.__dict__.items()])
        return f"{self.__class__.__name__}({params})"
    
    def __repr__(self):
        return self.__str__()

class User(StringRprMixin):
    def __init__(self):
        self.firstname = None
        self.lastname = None
        self.age = None
        self.phone_numbers = []
        self.adress = []


class IUserBuilder(ABC):
    @property
    @abstractmethod
    def result(self):pass

    @abstractmethod
    def add_firstname(self,firstname):pass

    @abstractmethod
    def add_lastname(self,lastname):pass

    @abstractmethod
    def add_age(self,age):pass

    @abstractmethod
    def add_phone(self,phone):pass

    @abstractmethod
    def add_adress(self,adress):pass


class UserBuiler(IUserBuilder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._result = User()

    @property
    def result(self):
        return_data = self._result
        self.reset()
        return return_data
    
    def add_firstname(self,firstname):
        self._result.firstname = firstname
        return self
    
    def add_lastname(self,lastname):
        self._result.lastname = lastname
        return self
    
    def add_age(self,age):
        self._result.age = age
        return self
    
    def add_phone(self,phone):
        self._result.phone_numbers.append(phone)
        return self
    
    def add_adress(self,adress):
        self._result.adress.append(adress)
        return self
class UserDirector:
    def __init__(self,builder:UserBuiler):
        self._builder = builder

    def with_age(self,firstname,lastname,age):
        self._builder.add_firstname(firstname)\
        .add_lastname(lastname)\
        .add_age(age)
        return self._builder.result

if __name__ == "__main__":
    user_builder = UserBuiler()
    user_director = UserDirector(user_builder)
    user1 = user_director.with_age("lucas","andrade",18)
    print(user1)