class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

# def get_neighbors(vertex, graph_matrix):
# 	x = vertex[0]
# 	y = vertex[1]
# 	neighbors = []
# 	# check north
# 	if y > 0 and graph_matrix[y - 1][x] == 1:
# 		neighbors.append((x, y - 1))
# 	# check south
# 	if y < len(graph_matrix) - 1 and graph_matrix[y + 1][x] == 1:
# 		neighbors.append((x, y + 1))
# 	# check east
# 	if x < len(graph_matrix[0]) - 1 and graph_matrix[y][x + 1] == 1:
# 		neighbors.append((x + 1, y))
# 	# check west
# 	if x > 0 and graph_matrix[y][x - 1] == 1:
# 		neighbors.append((x - 1, y))
# 	return neighbors

# def bft(x, y, matrix, visited):
# 	q = Queue()
# 	q.enqueue((x, y))
# 	while q.size() > 0:
#     		v = q.dequeue()
# 		x = v[0]
# 		y = v[1]
#         # If that vertex has not been visited...
#         if not visited[x][y]:
#                 # Mark it as visited
#                 # print(v)
#                 visited[y][x] = True
#                 # Then add all of its neighbors to the back of the queue
#                 for neighbor in get_neighbors((x, y), matrix):
#                     q.enqueue(neighbor)
# 	return visited

# # Write a function that takes a 2D binary array and returns the number of 1 islands. An island consists of 1s that are connected to the north, south, east or west. For example:
# islands = [[0, 1, 0, 1, 0],
# 			[1, 1, 0, 1, 1],
# 			[0, 0, 1, 0, 0],
# 			[1, 0, 1, 0, 0],
# 			[1, 1, 0, 0, 0]]

# def island_counter(matrix):
# 	# loop through the islands
# 	# do a bfs on them and count how many times that bft occurs
# 	# create a visited matrix
# 	visited = []
# 	for i in range(len(matrix)):
# 		visited.append([False] * len(matrix[0]))
# 	#create island counter; init to zero
# 	island_counter = 0
# 	# walk through each cell in the original matrix
# 	for x in range(len(matrix[0])):
# 		for y in range(len(matrix)):
# 			# if it has not been visited
# 			if not visited[y][x]:
# 				# if you reach a 1
# 				if matrix[y][x] == 1:
# 					# do a bft, and mark each 1 as visited
# 					visited = bft(x, y, matrix, visited)
# 				# increment counter by 1
# 					island_counter += 1
# 	pass

# print(island_counter(islands)) # returns 4

from util import Stack, Queue  # These may come in handy

'''
Write a function that takes a 2D binary array and returns the number of 1 islands.
An island consists of 1s that are connected to the north, south, east or west.

For example:
'''

# 1. Translate the problem into graphs terminology you've learned this week
# 2. Build your graph
# 3. Traverse your graph

def get_neighbors(vertex, graph_matrix):
    x = vertex[0]
    y = vertex[1]
    neighbors = []
    # Check north
    if y > 0 and graph_matrix[y - 1][x] == 1:
        neighbors.append((x, y-1))
    # Check south
    if y < len(graph_matrix) - 1 and graph_matrix[y + 1][x] == 1:
        neighbors.append((x, y+1))
    # Check east
    if x < len(graph_matrix[0]) - 1 and graph_matrix[y][x+1] == 1:
        neighbors.append((x+1, y))
    # Check west
    if x > 0 and graph_matrix[y][x-1] == 1:
        neighbors.append((x-1, y))
    return neighbors


def bft(x, y, matrix, visited):
    q = Queue()
    q.enqueue( (x, y) )
    while q.size() > 0:
        v = q.dequeue()
        x = v[0]
        y = v[1]
        if not visited[y][x]:
            visited[y][x] = True
            for neighbor in get_neighbors((x, y), matrix):  # STUB
                q.enqueue(neighbor)
    return visited


def island_counter(matrix):
    visited = []
    for i in range(len(matrix)):
        visited.append([False] * len(matrix[0]))
    # Create a counter, initialize to 0
    counter = 0
    # Walk through each cel in the original matrix
    for x in range(len(matrix[0])):
        for y in range(len(matrix)):
            # If it has not been visited...
            if not visited[y][x]:
                # If you reach a 1...
                if matrix[y][x] == 1:
                    # Do a BFT and mark each 1 as visited
                    visited = bft(x, y, matrix, visited)  # STUB
                    # Increment counter by 1
                    counter += 1
    return counter




islands = [[0, 1, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 1, 0, 0],
        [1, 0, 1, 0, 0],
        [1, 1, 0, 0, 0]]

print(island_counter(islands)) # returns 4

islands = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
        [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
    	[0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
        [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
        [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
        [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
        [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
        [0, 0, 1, 1, 0, 1, 0, 0, 1, 0],
        [1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
        [1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
        [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]]

print(island_counter(islands))  # 14