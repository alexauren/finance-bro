from abc import ABC, abstractmethod
 
class Model(ABC):

    @abstractmethod
    def predict(self, data):
        pass

    