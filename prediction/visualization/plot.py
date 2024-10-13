import matplotlib.pyplot as plt

class Plotter:

    @staticmethod
    def plot_data(data, title='Stock Price'):
        plt.figure(figsize=(16, 8))
        plt.title(title)
        plt.plot(data['Close'])
        plt.xlabel('Date', fontsize=18)
        plt.ylabel('Price', fontsize=18)
        plt.show()

