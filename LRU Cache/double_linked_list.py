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


if __name__ == "__main__":
    linked = DoubleLinkedList()
    linked.remove_from_start()
    linked.add_to_start(0)
    linked.remove_from_start()
    linked.remove_from_end()
    linked.add_to_end(5)
    linked.remove_from_end()
    five_node = linked.add_to_start(5)
    linked.remove_at(five_node)
    # linked.add_after(4, five_node)
    one_node = linked.add_to_end(1)
    three_node = linked.add_to_end(3)
    linked.add_to_start(-1)
    linked.add_before(2, three_node)
    linked.add_to_end(4)
    linked.add_after(3.5, three_node)
    hundred_node = linked.add_after(100, one_node)
    linked.remove_at(hundred_node)
    linked.add_before(-2, linked.find(-1))
    print(linked)
