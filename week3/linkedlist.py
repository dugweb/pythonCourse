"""
A Linked List (https://en.wikipedia.org/wiki/Linked_list) is a linear data structure. You can think of it as an implementation of a regular Python List.

Using Object Oriented programming, build a simple Linked List that shares the same interface with Python Lists:

    l = LinkedList()

    l.append(2)
    l.count()  # Should return 1

    l + [2, 3]     # Should return [1, 2, 3] but not mutate the original list
    l += [3, 4]   # Should return None and append [3, 4] to the original list

    l.pop(0)       # Should remove and return the first element.

    # Important. This should be True:
    LinkedList([1, 2, 3]) == LinkedList([1, 2, 3])

To ease your task, a LinkedList is constructed using different Nodes. Each node has a reference to other Node, what makes it a recursive class, it'll point to itself.

"""

class Node(object):
    def __init__(self):
        self.value = None
        self.next = None


class LinkedList(object):
    
    def __init__(self, list = []):
        self.current_node = None
        self.__iadd__(list)
        

    def append(self, value):
        n = Node()
        n.value = value
        n.next = self.current_node

        self.current_node = n

    def count(self):
        count = 0
        node = self.current_node
        while node is not None:
            count += 1
            node = node.next

        return int(count)

    def __add__(self, other):
        output = []
        node = self.current_node

        while node is not None:
            output.append(node.value)
            node = node.next

        return output + other

    def __iadd__(self, other):
        output = []

        for val in other:
            n = Node()
            n.value = val
            output.append(val)
            n.next = self.current_node
            self.current_node = n

        return self

    def pop(self, index):
        removalNode = self.current_node
        prevNode = None
        for i in range(index):
            prevNode = removalNode
            removalNode = removalNode.next

        if (prevNode):
            prevNode.next = removalNode.next  
        else:
            self.current_node = self.current_node.next

        return removalNode.value
        

    def __repr__(self):
        l = []
        node = self.current_node

        while node is not None:
            l.append(node.value)
            node = node.next

        return str(l)

    def __eq__(self, other):
        return self.__repr__() == other.__repr__()



l = LinkedList([3,4,5])
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.append(5)

l2 = LinkedList([9,8,7,6])
l2 += [3,4]
l2.count()




