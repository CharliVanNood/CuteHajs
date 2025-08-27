import requests
from bs4 import BeautifulSoup

def getData(response):
    soup = BeautifulSoup(response.text, "html.parser")

    currency = soup.find_all("span", class_="pip-price__currency")
    price_full = soup.find_all("span", class_="pip-price__integer")
    price_decimal = soup.find_all("span", class_="pip-price__decimal")

    if currency: currency = currency[0].text.strip()
    else: currency = None
    if price_full: price_full = price_full[0].text.strip()
    if price_decimal and not price_decimal[0].text == ":-" and not price_decimal[0].text == ".-":
        price_decimal = price_decimal[0].text.strip().replace(".", "").replace(",", "")
    else: price_decimal = None

    return (currency, price_full, price_decimal)

def request(url):
    response = requests.get(url)
    return response