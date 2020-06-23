class DoubleLinkedList:
    class _node:
        __slots__ = '_element', '_next','_prev'
        def __init__(self, element,next,prev):
            self._element = element
            self._next = next
            self._prev = prev

        def getNext(self):
            return self._next

        def getElement(self):
            return self._element

        def getPrev(self):
            return self._prev

    # length  of linkedlist
    def __len__(self):
        return self._size

    def __init__(self):
        self._size = 0
        self._header = self._node(None, None, None)
        self._trailer = self._node(None, None, None)
        self._header._next = self._trailer  # trailer is after header
        self._trailer._prev = self._header  # header is before trailer
        self.size = 0

    def isempty(self):
        return self._size == 0


    def _insert_between(self, e, predecessor, successor):

        newest = self._node(e, predecessor, successor)  # linked to neighbors
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -=1
        element = node._element  # record deleted element
        node._prev = node._next = node._element = None  # deprecate node
        return element