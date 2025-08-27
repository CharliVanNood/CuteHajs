import matplotlib.pyplot as plt

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

    plt.figure(figsize=(6,4))
    plt.plot(dates, prices, marker='o', linestyle='-', linewidth=2)
    plt.title("Example Graph")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")

    plt.savefig(f"graphs/graph{country}.png")
