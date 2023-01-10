"""
	Brandon Quinn

"""

# Fractional Knapsack Problem:
# In this problem,
# - you are given n items,
# - each with item having a dollar value and a weight.
# - The knapsack can carry a maximum weight W.
# - The algorithm selects the subset of items
# with maximum value where the sum of the weights of the items does not exceed W.

def thievery(goodies, weight, taken):

	for x in goodies:
		if x[2] <= weight:
			weight = weight - x[2]
			taken.append(x[:3])
		elif weight != 0:
			reduced = weight / x[2]
			new_weight = x[2] * reduced
			new_val = x[1] * reduced
			weight -= new_weight
			new_taken = (x[0], new_val, new_weight)
			taken.append(new_taken)

	return taken


def create_ratios(goodies):
	for x in range(0, len(goodies)):
		name = goodies[x][0]
		value = goodies[x][1]
		weight = goodies[x][2]
		goodies[x] = (name, value, weight, weight/value)
	goodies = sorted(goodies, key=lambda i: i[3])
	return goodies


def main():
	taken = []
	goodies = []
	weight = int(input())
	n = int(input())
	lines = [input() for _ in range(n)]
	for line in lines:
		x = line.split()
		goodies.append((x[0], int(x[1]), int(x[2])))

	goodies = create_ratios(goodies)
	taken = thievery(goodies, weight, taken)

	# This is so ugly but it was to get the correct formatting in gradescope
	total = 0
	count = 0
	for x in taken:
		if count < len(taken) - 1:
			print(x[0], "(", format(float(x[1]), ".2f"), ", ", format(float(x[2]), ".2f"), ")", sep="", end=" ")
			total += float(x[1])
		else:
			print(x[0], "(", format(float(x[1]), ".2f"), ", ", format(float(x[2]), ".2f"), ")", sep="")
			total += float(x[1])
			print(total)
		count += 1


if __name__ == "__main__":
	main()
