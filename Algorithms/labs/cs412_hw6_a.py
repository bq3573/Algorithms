"""
	Brandon Quinn

"""

# Greedy algorithm implementation
# Given an integer array of seeds where the int value of
# each element is the number of days it takes
# for that plant to fully grow. You can only plant one seed type per day.
# Determine the order in which the seeds should be planted for all
# plants to be fully grown in the shortest amount of time.

def plant_seeds(seeds):
	day = 1  # keep track of what day we're one.
	planted = []  # array to hold what's been planted and decrement every day
	seed = 0  # keep track of which seed to plant from seeds

	# Loop until all the seeds have been planted and grown to completion
	# Can't check sum at first because planted is empty.
	while True:
		# Don't wanna decrement on day one
		if day != 1:
			# loop through what's been planted and decrement how many days
			# they have left to grow
			for x in range(0, len(planted)):
				# if x still has days left to grow decrement
				if planted[x] != 0:
					planted[x] -= 1
		# plant a batch of seeds every day until there are no seeds left
		if seed < len(seeds):
			planted.append(seeds[seed])
			seed += 1

		# If the planted seeds are all fully grown
		if sum(planted) == 0:
			break

		# Increment the day
		day += 1
	return day + 1


def main():
	# Get input
	seeds = [int(x) for x in input().split(" ")]
	# Sort and reverse the list to get highest values first
	seeds = sorted(seeds, key=lambda x: x)
	seeds.reverse()
	day_of_party = plant_seeds(seeds)
	print(day_of_party)


if __name__ == "__main__":
	main()
