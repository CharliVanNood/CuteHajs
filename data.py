from currency_converter import CurrencyConverter
import time

converter = CurrencyConverter()

def convertCurrency(price, currency_in, currency_out):
    if currency_in == "Czechia": currency_in = "CZK"
    elif currency_in == "Poland": currency_in = "PLN"
    elif currency_in == "Canada": currency_in = "CAD"
    elif currency_in == "Sweden": currency_in = "SEK"
    elif currency_in == "Denmark": currency_in = "DKK"
    elif currency_in == "Switzerland": currency_in = "CHF"
    elif currency_in == "America": currency_in = "USD"
    else: return "UNKNOWN"
    return round(converter.convert(price, currency_in, currency_out), 2)

def show(country, currency, price_full, price_decimal):
    stringResult = ""
    spaces = " " * (20 - len(country) - len(currency))

    price = ""

    if currency == "€":
        if price_decimal and currency:
            stringResult += f"{country}:|{spaces}{currency} {price_full}.{price_decimal}     |(€ {price_full}.{price_decimal})"
            price = f"{price_full}.{price_decimal}"
        elif currency:
            stringResult += f"{country}:|{spaces}{currency} {price_full}.00     |(€ {price_full}.00)"
            price = f"{price_full}.00"
        elif price_decimal:
            stringResult += f"{country}:| {spaces}{price_full}.{price_decimal}     |(€ {price_full}.{price_decimal})"
            price = f"{price_full}.{price_decimal}"
        else:
            stringResult += f"{country}:| {spaces}{price_full}     |(€ {price_full})"
            price = f"{price_full}.00"
    else:
        if price_decimal:
            converted = convertCurrency(float(price_full + "." + price_decimal), country, 'EUR')
        else:
            converted = convertCurrency(float(price_full), country, 'EUR')
        price = f"{converted}"

        if price_decimal and currency:
            stringResult += f"{country}:|{spaces}{currency} {price_full}.{price_decimal}     |(€ {converted})"
        elif currency:
            stringResult += f"{country}:| {spaces}  {price_full}{currency}     |(€ {converted})"
        elif price_decimal:
            stringResult += f"{country}:| {spaces}{price_full}.{price_decimal}     |(€ {converted})"
        else:
            stringResult += f"{country}:| {spaces}{price_full}       |(€ {converted})"
    
    with open(f"histories/{country}", "a") as f:
        f.write(price + "x" + str(time.time()) + "\n")

    return (stringResult, price)