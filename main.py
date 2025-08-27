from request import request
from data import getData

blahaj_id = "30373588"

response = request(f"https://www.ikea.com/nl/nl/p/blahaj-pluchen-speelgoed-haai-{blahaj_id}/")
(currency, price_full, price_decimal) = getData(response, "nl/nl")
if price_decimal:
    print(f"Netherlands: {currency} {price_full}.{price_decimal}")
else:
    print(f"Netherlands:   {price_full}{currency}")

response = request(f"https://www.ikea.com/cz/cs/p/blahaj-plysova-hracka-zralok-{blahaj_id}/")
(currency, price_full, price_decimal) = getData(response, "cz/cs")
if price_decimal:
    print(f"Czechia:     {currency} {price_full}.{price_decimal}")
else:
    print(f"Czechia:       {price_full}{currency}")