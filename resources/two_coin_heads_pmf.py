import matplotlib.pyplot as plt


def create_two_coin_heads_pmf() -> dict[int, float]:
	"""Return the PMF for the number of heads in two fair coin tosses."""
	return {0: 1 / 4, 1: 1 / 2, 2: 1 / 4}


def plot_two_coin_heads_pmf() -> None:
	"""Plot the PMF for the number of heads in two fair coin tosses."""
	pmf = create_two_coin_heads_pmf()
	outcomes = list(pmf.keys())
	probs = list(pmf.values())

	plt.figure(figsize=(8, 4.5))
	plt.bar(outcomes, probs, width=0.55, color="#1f77b4")
	plt.title("PMF of Number of Heads in Two Fair Coin Tosses")
	plt.xlabel("Number of Heads")
	plt.ylabel("Probability")
	plt.xticks(outcomes)
	plt.ylim(0, 0.6)
	plt.grid(axis="y", alpha=0.3)
	plt.tight_layout()
	plt.savefig("resources/two_coin_heads_pmf.png", dpi=200)


if __name__ == "__main__":
	plot_two_coin_heads_pmf()
