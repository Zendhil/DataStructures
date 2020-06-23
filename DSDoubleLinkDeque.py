from DSDoublyLinkedList import DoubleLinkedList

class LinkedDeque(DoubleLinkedList):

    def first(self):
        pass

    def last(self):
        pass

    def insert_first(self, e):
        self._insert_between(e,self._header,self._header._next)

    def insert_last(self, e):
        self._insert_between(e, self._trailer._prev, self._trailer)

    def delete_first(self):
        if self.isempty(): print ("Error")
        else: self._delete_node(self._header._next)



    def delete_last(self):
        if self.isempty():
            print("Error")
        else:
            self._delete_node(self._trailer._prev)
