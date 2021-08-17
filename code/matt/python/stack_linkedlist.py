class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

    def __str__(self):
        return f'({self.item}, {self.next})'


class Stack:
    def __init__(self):
        self.head = None

    def push(self, element):  # insert an element at the start (new head)
        self.head.append(element)

    def pop(self):  # remove an element from the start (the head becomes the next node)
        self.head.pop()

    def peek(self):  # returns the element on the head node or None if there is no head
        if self.head != None:
            return self.head[-1]
        else:
            return None

    def __len__(self):  # return the number of elements
        return len(self.head)

    def to_list(self):
        if self.head == None:
            self.head = []

    def __str__(self):
        for head in self.head:
            print(head)


# create nodes
n3 = Node('pears')
n2 = Node('bananas', n3)
n1 = Node('apples', n2)

# n1 -> n2 -> n3
print(n1.item)  # apples
print(n1.next.item)  # bananas
print(n1.next.next.item)  # pears
print(n1)  # ('apples',('bananas',('pears',None)))

# iterate over the nodes
n = n1  # temporary node we advance each iteration
while n is not None:  # stop when we run out of nodes
    print(n.item)  # prints apples, bananas, pears
    n = n.next  # advance the node to the next node

s = Stack()
s.to_list()
s.push(5)
s.push(6)
print(s.peek())

# print(s.length())  # 2
print(s.pop())  # 6
# print(s.pop()) # 5
