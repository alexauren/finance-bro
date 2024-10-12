from models.model import Model

class Predictor(): 

    def __init__(self, model: Model):
        self.model = model
    
    def predict_price(self, data):
        self.model.predict(data)