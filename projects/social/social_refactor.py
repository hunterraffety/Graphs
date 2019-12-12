import random
import time

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

class User:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            # print("WARNING: You cannot be friends with yourself")
            return False
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            # print("WARNING: Friendship already exists")
            return False
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            return True

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
        # Add users
        # Time complexity: O(n)
        for i in range(num_users):
            self.add_user(f"User {i+1}")
        # Create friendships
        # Create a list with all possible friendship combinations,
        # Time complexity: O(n^2)
        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append( (user_id, friend_id) )
        # shuffle the list,
        # Time complexity: O(n)
        random.shuffle(possible_friendships)
        # then grab the first N elements from the list.
        # Number of times to call add_friendship = avg_friendships * num_users / 2
        # Time Complexity: O(n^2)
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def populate_graph_random_sampling(self, num_users, avg_friendships):
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        # Time complexity: O(n)
        for i in range(num_users):
            self.add_user(f"User {i+1}")

        # Create friendships
        target_friendships = avg_friendships * num_users
        total_friendships = 0
        collisions = 0

        # While number of friendships < avg_friendships * num_users:
        while total_friendships < target_friendships:
            # Pick two random users
            user_id = random.randint(1, self.last_id)
            friend_id = random.randint(1, self.last_id)
            # Try to create the friendship
            if self.add_friendship(user_id, friend_id):
                total_friendships += 2
            else:
                collisions += 1
        print(f"COLLISIONS: {collisions}")

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument
​
        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.
​
        The key is the friend's ID and the value is the path.
        """
        # Create an queue
        q = Queue()
        # Enqueue a path to the starting user
        q.enqueue( [user_id] )
        # Create a dictionary to store visited users and the social path to them
        visited = {}
        # While the queue is not empty:
        while q.size() > 0:
            # Dequeue the first social path
            path = q.dequeue()
            # Grab the last user from the social path
            u = path[-1]
            # If it has not been visited:
            if u not in visited:
                # Add it to the visited dictionary with the path as the value
                visited[u] = path
                # Then enqueue paths to each friend
                for friend in self.friendships[u]:
                    path_copy = path.copy()
                    path_copy.append(friend)
                    q.enqueue(path_copy)
        return visited




if __name__ == '__main__':
    num_users = 4000
    avg_friendships = 50
    sg = SocialGraph()
    start_time = time.time()
    sg.populate_graph(num_users, avg_friendships)
    end_time = time.time()
    print("----")
    print(f"Populate graph: {end_time - start_time} seconds")
    print("----")

    sg = SocialGraph()
    start_time = time.time()
    sg.populate_graph_random_sampling(num_users, avg_friendships)
    end_time = time.time()
    print(f"Populate graph sampling: {end_time - start_time} seconds")
    # print("----")
    # print(sg.users)
    # print("----")
    # print(sg.friendships)
    # print("----")
    # connections = sg.get_all_social_paths(1)
    # print(connections)