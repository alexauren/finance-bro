from abc import ABC, abstractmethod
from visualization.plot import Plotter
 
class Model(ABC):

    @abstractmethod
    def predict(self, data):
        pass

    def plot(self, data, title='Stock Price'):
        Plotter.plot_data(data, title)
        

