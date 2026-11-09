class Person:
    '''
    A class representing a person in a social network.
    Attributes:
        name (str): The name of the person.
        friends (list): A list of friends (Person objects).
    Methods:
        add_friend(friend): Adds a friend to the person's friend list.
   '''
    
    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)

class SocialNetwork:
    '''
    A class representing a social network.
    Attributes:
        people (dict): A dictionary mapping names to Person objects.
    Methods:
        add_person(name): Adds a new person to the network.
        add_friendship(person1_name, person2_name): Creates a friendship between two people.
        print_network(): Prints the names of all people and their friends.
    '''
    
    def __init__(self):
        self.people = {}

    def add_person(self, name):
        if name in self.people:
            print(f"{name} already exists in the network!")
            return
        self.people[name] = Person(name)

    def add_friendship(self, person1_name, person2_name):
        if person1_name not in self.people:
            print(f"Friendship not created. {person1_name} doesn't exist.")
            return
        if person2_name not in self.people:
            print(f"Friendship not created. {person1_name} can't befriend themselves.")
            return

        person1 = self.people[person1_name]
        person2 = self.people[person2_name]
        person1.add_friend(person2)
        person2.add_friend(person1)

    def print_network(self):
        for name, person in self.people.items():
            friend_names = ", ".join(friend.name for friend in person.friends)
            print(f"{name} is friends with: {friend_names}")


# Test your code here

if __name__ == "__main__":
    alex = Person("Alex")
    jordan = Person("Jordan")
    print(alex.friends)
    alex.add_friend(jordan)
    print(alex.friends[0].name)

    network = SocialNetwork()

    network.add_person("Alex")
    network.add_person("Jordan")
    print(network.people)
    network.add_person("Morgan")
    network.add_person("Taylor")
    network.add_person("Casey")
    network.add_person("Riley")

    network.add_friendship("Alex", "Jordan")
    network.add_friendship("Alex", "Morgan")
    network.add_friendship("Jordan", "Taylor")
    network.add_friendship("Jordan", "Johnny")

    network.add_friendship("Morgan", "Casey")
    network.add_friendship("Taylor", "Riley")
    network.add_friendship("Casey", "Riley")
    network.add_friendship("Morgan", "Riley")
    network.add_friendship("Alex", "Taylor")
 
    print("\n--- Network after initial setup ---")
    network.print_network()
 
    print("\n--- Edge cases ---")
    network.add_person("Alex")                  
    network.add_friendship("Alex", "Jordan")    
    network.add_friendship("Ghost", "Alex")     
    network.add_friendship("Alex", "Alex")      
 
    network.add_person("Sam")
    network.add_friendship("Sam", "Casey")
 
    print("\n--- Network after more additions ---")
    network.print_network()
 
 
'''
DESIGN MEMO
 
A graph is the right structure for a social network because the data is made
of entities (people) and the relationships between them (friendships). Each
person is a node and each friendship is an edge, and there is no limit on how
many connections a person can have or how those connections link back to each
other. Friendships are mutual, so the edges are undirected, which I modeled by
adding each person to the other's friends list.
 
A list wouldn't work as well because it only stores items in a sequence and has
no built-in way to say who is connected to whom. I would have to keep a second
structure for the relationships anyway. A tree wouldn't work because trees have
a single root, one parent per node, and no cycles. In my test network, Alex,
Jordan, and Taylor all know each other, and Morgan, Casey, and Riley form
another loop. Those cycles are impossible in a tree.
 
I noticed a few trade-offs. With an adjacency list, adding a person or a
friendship is fast, O(1) for the dictionary lookups and appends, and it only
uses space for friendships that exist. The cost is that checking whether two
people are already friends means scanning a friends list, which is O(f) where f
is the number of friends. I did that check to prevent duplicates. Printing the
network is O(V + E) because it visits every person and every friend entry, and
each friendship appears twice since it is stored on both sides. An adjacency
matrix would make friendship checks O(1) but would use O(V^2) space, which is
wasteful when most people are not friends with each other.
'''