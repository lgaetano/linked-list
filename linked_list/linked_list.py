
# Defines a node in the singly linked list
class Node:

    def __init__(self, value, next_node = None):
        self.value = value
        self.next = next_node

# Defines the singly linked list
class LinkedList:
    def __init__(self):
      self.head = None # keep the head private. Not accessible outside this class

    # returns the value in the first node
    # returns None if the list is empty
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def get_first(self):
        if not self.head:
            return None
        return self.head.value

    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def add_first(self, value):
        new_node = Node(value)

        new_node.next = self.head
        self.head = new_node

    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def search(self, value):
        cur = self.head

        while cur:
            if cur.value == value:
                return True
            cur = cur.next
        return False

    # method that returns the length of the singly linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1) -> O(2)
    def length(self):
        count = 0
        cur = self.head
        
        while cur:
            count += 1
            cur = cur.next
        return count

    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns None if there are fewer nodes in the linked list than the index value
    # Time Complexity: O(n) -> O(2n)
    # Space Complexity: O(1) -> O(3)
    def get_at_index(self, index):
        if index < 0:
            return "Error: this is a singly linked list..."

        length = self.length()
        if length == 0 or length < index:
            return None

        cur = self.head
        if index == 0:
            return cur.value
    
        for _ in range(0, index):
            cur = cur.next
        return cur.value


    # method that returns the value of the last node in the linked list
    # returns None if the linked list is empty
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_last(self):
        if self.head == None:
            return None
        
        cur = self.head
        while cur.next:
            cur = cur.next 
        return cur.value

    # method that inserts a given value as a new last node in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1) -> O(2)
    def add_last(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            return

        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    # method to return the max value in the linked list
    # returns the data value and not the node
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def find_max(self):
        max_val = None

        cur = self.head
        while cur:
            if max_val == None or cur.value > max_val:
                max_val = cur.value
            cur = cur.next
        
        return max_val

    # method to delete the first node found with specified value
    # Time Complexity: O(n)
    # Space Complexity: O(1) -> O(2)
    def delete(self, value):
        if self.head == None:
            return

        if self.head.value == value:
            self.head = self.head.next
            return

        cur = self.head.next
        prev_seen = self.head

        while cur:
            if cur.value == value:
                prev_seen.next = cur.next
                cur.next = None
            prev_seen = cur
            cur = cur.next

    # method to print all the values in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1) -> O(2)
    def visit(self):
        helper_list = []
        current = self.head

        while current:
            helper_list.append(str(current.value))
            current = current.next
        
        print(", ".join(helper_list))

    # method to reverse the singly linked list
    # note: the nodes should be moved and not just the values in the nodes
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def reverse(self):
        if self.head == None:
            return None

        cur = self.head
        prev = None
        next = None
        
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        self.head = prev
  
    ## Advanced/ Exercises
    # returns the value at the middle element in the singly linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def find_middle_value(self):
        mid = self.length() // 2

        cur = self.head

        for _ in range(mid):
            cur = cur.next

        return cur.value


    # find the nth node from the end and return its value
    # assume indexing starts at 0 while counting to n
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def find_nth_from_end(self, n):
        length = self.length()
        if n >= length or length == 0:
            return None

        n_from_front = length - n

        cur = self.head
        for _ in range(n_from_front):
            cur = cur.next

        if not cur:
            return None
        else:
            return cur.value

    # checks if the linked list has a cycle. A cycle exists if any node in the
    # linked list links to a node already visited.
    # returns true if a cycle is found, false otherwise.
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def has_cycle(self):
        unique_nodes = set()

        cur = self.head
        while cur:
            if cur in unique_nodes:
                return True
            unique_nodes.add(cur)
            cur = cur.next
        return False

    # Helper method for tests
    # Creates a cycle in the linked list for testing purposes
    # Assumes the linked list has at least one node
    def create_cycle(self):
        if self.head == None:
            return

        # navigate to last node
        current = self.head
        while current.next != None:
            current = current.next

        current.next = self.head # make the last node link to first node
