import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

n = ToastNotifier()

data = requests.get('https://www.bbc.com/weather/1275004')

soup = BeautifulSoup(data.text, 'lxml')

temp1 = soup.find('span', class_="wr-day-temperature__high-value")

temps = temp1.text.split(' ')

tempc = temps[0]

result = "The temperature in Kolkata is " + tempc + "C" + " or " + temps[1] + "F"

n.show_toast("Weather update", result, duration=10)
