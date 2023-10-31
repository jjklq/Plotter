import requests
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta

# Функция для получения данных о курсе UAH/USD с 2000 года до текущей даты
def fetch_exchange_rate_data():
    start_date = datetime(2000, 1, 1)
    end_date = datetime.now()

    dates = []
    exchange_rates = []

    current_date = start_date
    while current_date <= end_date:
        date_str = current_date.strftime('%d.%m.%Y')
        url = f'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=USD&date={date_str}&json'
        response = requests.get(url)
        data = response.json()
        if data:
            date = data[0]['exchangedate']
            rate = data[0]['rate']
            dates.append(date)
            exchange_rates.append(rate)
        current_date += timedelta(days=1)

    return list(zip(dates, exchange_rates))

# Функция для построения графика
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
