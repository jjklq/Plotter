import matplotlib.pyplot as plt
import pandas as pd

def plot_exchange_rate(data):

    df = pd.DataFrame(data, columns=['Date', 'Exchange Rate'])
    
    
    df['Date'] = pd.to_datetime(df['Date'])

   
    plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df['Exchange Rate'], label='UAH/USD Exchange Rate', color='blue')
    plt.xlabel('Date')
    plt.ylabel('Exchange Rate')
    plt.title('UAH/USD Exchange Rate Since 2000')
    plt.legend()
    plt.grid(True)
    plt.show()
