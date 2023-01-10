"""
	Brandon Quinn

"""

# Determine if a graph is acyclic...

def acyclic():
	print("False")


def DFS_ALL(G, adjacency, classify, clock):
	clock = PreProcess(clock)
	stack = []
	# stack.clear()
	for x in range(0, len(G)):
		if G[x][0] not in stack:
			clock = DFS(G[x][0], adjacency, classify, clock, stack)


def DFS(v, adjacency, classify, clock, stack):
	stack.append(v)
	clock = PreVisit(v, classify, clock)
	edges = adjacency.get(v)
	for x in edges:
		if x not in stack:
			stack.append(x)
			classify.get(x)[2] = v
			DFS(x, adjacency, classify, clock, stack)
	clock = PostVisit(v, classify, clock)
	return clock


def PostVisit(v, classify, clock):
	clock = clock + 1
	classify.get(v)[1] = clock
	for x in classify:
		print(x, "HERE")
		if not(x == v) and classify.get(v)[2] == classify.get(x)[2]:
			exit(acyclic())
	# print(clock)
	return clock


def PreProcess(clock):
	# print(clock)
	return 0


def PreVisit(v, classify, clock):
	clock = clock + 1
	classify.get(v)[0] = clock
	# print(clock)
	return clock


def main():
	scans = int(input())
	lines = [input().split(" ") for _ in range(scans)]
	adjacency_list = {}
	classify = {}
	clock = 0
	for x in range(0, len(lines)):
		adjacency_list.update({lines[x][0]: set({})})
		classify.update({lines[x][0]: [None, None, None]})
		for y in range(1, len(lines[x])):
			adjacency_list.get(lines[x][0]).add(lines[x][y])
	# print(adjacency_list)
	# print(classify)

	DFS_ALL(lines, adjacency_list, classify, clock)
	print("True")
	# print(classify)

	# print(DFS_ALL(lines, adjacency_list, classify, clock))

	# pre = 0
	# post = 1
	# post_times = []
	# for x in classify:
	# 	post_times.append(classify.get(x)[1])
	#
	# post_times.reverse()
	#
	# acyclic = True
	# for x in range(0, len(post_times) - 1):
	# 	if post_times[x] > post_times[x + 1]:
	# 		acyclic = False
	# 		break
	# print(str(acyclic))


if __name__ == "__main__":
	main()
