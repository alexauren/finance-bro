from model import Model
from models.arima import Arima


class Predictor(): 

    def __init__(self, model: Model):
        self.model = model
    
    def predict_price(self, data):
        return self.model.predict(data)

arima = Arima()
pred = Predictor(arima)
data = 0
print(pred.predict_price(data))

