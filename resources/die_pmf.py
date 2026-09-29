import matplotlib.pyplot as plt


def create_die_pmf() -> dict[int, float]:
	"""Return the PMF for one fair six-sided die."""
	return {face: 1 / 6 for face in range(1, 7)}


def plot_die_pmf() -> None:
	"""Plot the PMF for one fair six-sided die."""
	pmf = create_die_pmf()
	outcomes = list(pmf.keys())
	probs = list(pmf.values())

	plt.figure(figsize=(8, 4.5))
	plt.stem(outcomes, probs, basefmt=" ")
	plt.title("PMF of One Fair Six-Sided Die")
	plt.xlabel("Outcome")
	plt.ylabel("Probability")
	plt.xticks(outcomes)
	plt.grid(axis="y", alpha=0.3)
	plt.tight_layout()
	plt.savefig("resources/die_pmf.png", dpi=200)


if __name__ == "__main__":
	plot_die_pmf()
