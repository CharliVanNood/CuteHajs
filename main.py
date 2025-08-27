import requests
from bs4 import BeautifulSoup

url = "https://www.ikea.com/nl/nl/p/blahaj-pluchen-speelgoed-haai-30373588/"
response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

currency = soup.find_all("span", class_="pip-price__currency")[0].text.strip()
price_full = soup.find_all("span", class_="pip-price__integer")[0].text.strip()
price_decimal = soup.find_all("span", class_="pip-price__decimal")[0].text.strip().replace(".", "")

print(f"{currency} {price_full} {price_decimal}")
