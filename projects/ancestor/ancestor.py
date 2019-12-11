from graph import Graph
from util import Queue, Stack

def earliest_ancestor(ancestors, starting_node):
	# obv need a graph.
	graph = Graph()

	# let's see what we have:
	print(f"starting node: {starting_node}")
	for i in ancestors:
		print(i)

	# planning - to start:
	# build a graph from the incoming data (ancestors, starting node)
	# create a queue and enqueue the starting node
	# keep planning from there