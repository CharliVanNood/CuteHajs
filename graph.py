import matplotlib.pyplot as plt

def graph(country, dates, prices):
    plt.figure(figsize=(6,4))
    plt.plot(dates, prices, marker='o', linestyle='-', linewidth=2)
    plt.title("Example Graph")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")

    plt.savefig(f"graphs/graph{country}.png")

    print(f"Graph saved as graphs/graph{country}.png")