# Write a function that takes a 2D binary array and returns the number of 1 islands. An island consists of 1s that are connected to the north, south, east or west. For example:
islands = [[0, 1, 0, 1, 0],
			[1, 1, 0, 1, 1],
			[0, 0, 1, 0, 0],
			[1, 0, 1, 0, 0],
			[1, 1, 0, 0, 0]]

def island_counter(matrix):
	# loop through the islands
	# do a bfs on them and count how many times that bft occurs

	# create a visited matrix
	# walk through each cell in the original matrix
		# if it's not been visited
			# if you reach a 1
				# do a bft and mark each encountered 1 as visited
				# increment counter by 1
	pass

island_counter(islands) # returns 4