from graph import Graph
from util import Queue, Stack

def earliest_ancestor(ancestors, starting_node):
	# obv need a graph.
	graph = Graph()

	# let's see what we have:
	# print(f"starting node: {starting_node}")
	# for i in ancestors:
	#	print(f"ancestors: {i}")

	# planning - to start:
	# build a graph from the incoming data (ancestors, starting node). test file assumed a range of 12 elements (1-11).
	for num in range(1, 12):
		graph.add_vertex(num)

	for pairs in ancestors:
		graph.add_edge(pairs[0], pairs[1])

	# variable used to check if an element is present
	check = 0

	# create a list to check against
	check_list = []

	# create a list of children elements to check
	sub_items = []

	# for every element
	for g in graph.vertices:
		# a check at this index position to ensure there are elements attached, otherwise it will try to pop from an empty set
		if graph.vertices[g] != set():
			# while the length of each set is greater than 0, we move forward in the loop
			while len(graph.vertices[g]) > 0:
				print(f"graph.vertices[g]: {graph.vertices[g]}")
				# we are now able to assume that we will encounter a child element
				check = graph.vertices[g].pop()
				print(f"check: {check}, g: {g}")
				# we can add this element as well as the parent element as the second parameter
				check_list.append((check, g))
				# we can add the child element to our list of subitems
				sub_items.append(check)

	# we can begin to look at our list of elements
	for c in check_list:
		# if the element at this index exists, we need to begin looking upward through the tree of elements
		if c[0] == starting_node:
			print(f"bing bing bing ==> c[0]: {c[0]}, starting: {starting_node}")
			# we now need to look at the parent node is existent in the children list, to ensure that it's not the end (top) of the tree.
			if c[1] in sub_items:
				# invoke recursion to root the element out
				return earliest_ancestor(ancestors, c[1])
			else:
				# otherwise, we have hit the end and have no node above it, the tree is over
				return c[1]
	# this element does not exist, so quit while you're ahead
	return -1