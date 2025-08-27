from bs4 import BeautifulSoup

def getData(response, country):
    soup = BeautifulSoup(response.text, "html.parser")

    currency = soup.find_all("span", class_="pip-price__currency")
    price_full = soup.find_all("span", class_="pip-price__integer")
    price_decimal = soup.find_all("span", class_="pip-price__decimal")

    if currency: currency = currency[0].text.strip()
    if price_full: price_full = price_full[0].text.strip()
    if price_decimal: price_decimal = price_decimal[0].text.strip().replace(".", "")
    else: price_decimal = None

    return (currency, price_full, price_decimal)