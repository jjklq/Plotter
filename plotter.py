import requests
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

def fetch_exchange_rate_data():
    url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=USD&date=20000101&json'
    response = requests.get(url)
    data = response.json()

    # Инициализация списков для данных
    dates = []
    exchange_rates = []

    for entry in data:
        date = entry['exchangedate']
        rate = entry['rate']
        dates.append(date)
        exchange_rates.append(rate)

    return list(zip(dates, exchange_rates))


def plot_exchange_rate(data):
    df = pd.DataFrame(data, columns=['Date', 'Exchange Rate'])
    df['Date'] = pd.to_datetime(df['Date'], format='%d.%m.%Y')

    plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df['Exchange Rate'], label='Курс UAH/USD', color='blue')
    plt.xlabel('Дата')
    plt.ylabel('Курс обмена')
    plt.title('Курс UAH/USD с 2000 года')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    data = fetch_exchange_rate_data()
    plot_exchange_rate(data)
