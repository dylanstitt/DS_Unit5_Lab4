# Dylan Stitt
# Unit 5 Lab 4
# Positional Doubly Base Class

class PositionalDoublyBase:
    class DoublyNode:
        # Nested Doubly Node Class

        def __init__(self, val):
            """Doubly Node Constructor"""
            self.value = val
            self.next = None
            self.prev = None

        def __str__(self):
            """Doubly Node String Method"""
            return f"|{self.value}|"

        def set_next(self, node):
            """Sets next to a new node"""
            if type(node) == type(self) or node is None:
                self.next = node
            else:
                raise TypeError('Node is not type DoublyNode or None')

        def set_prev(self, node):
            """Sets prev to a new node"""
            if type(node) == type(self) or node is None:
                self.prev = node
            else:
                raise TypeError('Node is not type DoublyNode or None')

    def __init__(self):
        self.header = self.DoublyNode(None)
        self.trailer = self.DoublyNode(None)

        self.header.set_next(self.trailer)
        self.trailer.set_prev(self.header)

        self.__size = 0

    def __str__(self):
        """To String for Positional Doubly Base"""
        out = "HEADER:"

        walk = self.header
        for i in range(self.__size + 2):
            out += f"{walk}"
            walk = walk.next
            if walk is not None:
                out += " <-> "

        out += ":TRAILER"
        return out

    def __len__(self):
        """Return the size of the Positional Doubly Base"""
        return self.__size

    def __is_empty(self):
        """Returns True if Positional Doubly Base is empty"""
        return self.__size == 0

    def __insert_between(self, value, pred=None, succ=None):
        """Inserts a new node between two existing nodes"""
        if pred is None:
            pred = self.header
        if succ is None:
            succ = self.trailer

        if pred.next != succ:
            raise IndexError('Cannot insert between nodes that are not in sequence')

        node = self.DoublyNode(value)
        node.set_next(succ)
        node.set_prev(pred)

        pred.set_next(node)
        succ.set_prev(node)

        self.__size += 1
        return node

    def __delete_node(self, node):
        """deletes a node within the Positional Doubly Base"""
        if type(node) != self.DoublyNode:
            raise TypeError('Node is not type DoublyNode')

        if node.value is None:
            raise ValueError('Cannot delete a sentinel or previously deleted node')

        value = node.value
        node.prev.set_next(node.next)
        node.next.set_prev(node.prev)

        node.value = node.next = node.prev = None

        self.__size -= 1
        return value
