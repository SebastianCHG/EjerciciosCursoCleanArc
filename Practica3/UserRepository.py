from abc import ABC, abstractmethod

class UserRepository(ABC):

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def add(self, user):
        pass
