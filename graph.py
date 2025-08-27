import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

def graph(country):
    with open(f"histories/{country}", "r") as f:
        data = f.read().split("\n")
    dates = []
    prices = []
    
    for line in data:
        dataSplit = line.split("x")
        if len(dataSplit) < 2: continue
        dates.append(dataSplit[1])
        prices.append(dataSplit[0])

    dates = [datetime.fromtimestamp(int(float(ts))) for ts in dates]

    plt.figure(figsize=(6,3))
    plt.plot(dates, prices, marker='o', linestyle='-', linewidth=2)

    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y/%m/%d"))
    plt.gcf().autofmt_xdate(rotation=20)

    plt.title(country)
    plt.xlabel("")
    plt.ylabel("Price")

    plt.savefig(f"graphs/graph{country}.png")
