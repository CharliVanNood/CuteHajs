from request import request, getData
from data import show

blahaj_id = "30373588"
country_codes = {
    "Netherlands": ["nl/nl", 30373588], "Czechia": ["cz/cs", 30373588], "Germany": ["de/de", 30373588], 
    "Belgium": ["be/nl", 30373588], "France": ["fr/fr", 30373588], "Spain": ["es/en", 30373588], 
    "Poland": ["pl/pl", 30373588], "Italy": ["it/it", 30373588], "Canada": ["ca/en", 90373590],
    "Sweden": ["se/en", 30373588], "Denmark": ["dk/da", 30373588], "Slovakia": ["sk/sk", 30373588],
    "Austria": ["at/en", 30373588], "Switzerland": ["ch/en", 30373588]
}

print("Getting Data")

mdStart = "# Hey hey, we track haj prices  \nBelieve it or not, BLÅHAJ pricing is really not as static as it may seem!  \n"
mdStart += "So like it's only logical if we tracked them, imagine overpaying for your haj collection!  \n"
mdStart += "Here is all the data we collect:  \n"

stringResult = mdStart + "| Country | Price Local | Price Euro |  \n| ------- | ------- | ------- |  \n"
for country in country_codes:
    response = request(f"https://www.ikea.com/{country_codes[country][0]}/p/{country_codes[country][1]}/")
    (currency, price_full, price_decimal) = getData(response)
    stringResult += show(country, currency, price_full, price_decimal) + "  \n"
print(stringResult)

with open("README.md", "w") as f:
    f.write(stringResult)