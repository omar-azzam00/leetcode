class DoubleLinkedList:
    """
    * You can't instantiate a node object directly instead use one of the add methods
    to add a value to the linked list and you will get a node object in return

    * never access or manipulate any private variables in the Node object instead use the
    corresponding read-only properties

    * if a specific node is no longer a part of the tree then its valid property will be False,
    and its before and after properties will be None.

    * trying to do operations using a node that is no longer part of the tree (aka its valid property is false) will
    raise an exception

    * you can edit the value property (aka Node.value) of a Node object as you want
    """

    class Node:
        def __init__(self, _before=None, value=None, _after=None):
            self._before = _before
            self.value = value
            self._after = _after
            self._valid = True

        @property
        def before(self):
            if not self._valid:
                return None

            return self._before

        @property
        def after(self):
            if not self._valid:
                return None

            return self._after

        @property
        def valid(self):
            return self._valid

    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_start(self, value):
        if self.head == None:
            self.head = self.Node(value=value)
            self.tail = self.head
            return self.head

        new = self.Node(value=value, _after=self.head)
        self.head._before = new
        self.head = new
        return new

    def add_to_end(self, value):
        if self.head == None:
            self.head = self.Node(value=value)
            self.tail = self.head
            return self.head

        new = self.Node(_before=self.tail, value=value)
        self.tail._after = new
        self.tail = new
        return new

    def add_before(self, value, node):
        if not node.valid:
            raise Exception(
                "You are trying to do operations using a node that is no longer part of the linked list!"
            )

        if node == self.head:
            return self.add_to_start(value)

        new = self.Node(_before=node._before, value=value, _after=node)
        node._before = new
        (new._before)._after = new
        return new

    def add_after(self, value, node):
        if not node.valid:
            raise Exception(
                "You are trying to do operations using a node that is no longer part of the linked list!"
            )

        if node == self.tail:
            return self.add_to_end(value)

        new = self.Node(_before=node, value=value, _after=node._after)
        node._after = new
        (new._after)._before = new
        return new

    def remove_from_start(self):
        if self.head == None:
            return
        if self.head == self.tail:
            self.head._valid = False
            self.head = None
            self.tail = None
            return

        self.head._valid = False
        self.head = self.head._after
        self.head._before = None

    def remove_from_end(self):
        if self.head == None:
            return
        if self.head == self.tail:
            self.head._valid = False
            self.head = None
            self.tail = None
            return

        self.tail._valid = False
        self.tail = self.tail._before
        self.tail._after = None

    def remove_at(self, node: Node):
        if not node.valid:
            raise Exception(
                "You are trying to do operations using a node that is no longer part of the linked list!"
            )

        if node == self.head:
            return self.remove_from_start()
        if node == self.tail:
            return self.remove_from_end()

        node._valid = False
        node_1 = node._before
        node_2 = node._after
        node_1._after = node_2
        node_2._before = node_1

    def traverse(self):
        current = self.head

        while current != None:
            yield current
            current = current._after

    def find(self, value, default=None):
        for node in self.traverse():
            if node.value == value:
                return node
        return default

    def find_all(self, value):
        equal_nodes = []

        for node in self.traverse():
            if node.value == value:
                equal_nodes.append(node)

        return equal_nodes

    def __str__(self):
        string = ""
        for node in self.traverse():
            string += str(node.value)
            if node != self.tail:
                string += " -> "
        return string

# Hash Table (Dictionary) will save the cache as keys and values

# 1, 3

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.history = DoubleLinkedList()
        self.size = 0
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        # Key In the cache
        if key in self.cache:
            value, old_node = self.cache[key]
            self.history.remove_at(old_node)
            node = self.history.add_to_end(key)
            self.cache[key] = (value, node)
            return value
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        # Update Existing Key
        if key in self.cache:
            _, node = self.cache[key]
            self.history.remove_at(node)
            node = self.history.add_to_end(key)
            self.cache[key] = (value, node)
        # Add new Key
        else:
            # Cache is still not full
            if self.size < self.capacity:
                node = self.history.add_to_end(key)
                self.cache[key] = (value, node)
                self.size += 1 
            # Cache Full
            else:
                node = self.history.add_to_end(key)
                self.cache[key] = (value, node)
                old_key = self.history.head.value
                self.history.remove_from_start()
                self.cache.pop(old_key)

if __name__ == "__main__":
    lru = LRUCache(2)
    lru.put(1, 0)
    lru.put(2, 2)
    lru.get(1)
    lru.put(3,3)
    lru.get(2)
    lru.put(4,4)
    lru.get(1)
    lru.get(3)
    lru.get(4)