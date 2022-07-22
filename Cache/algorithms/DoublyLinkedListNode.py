

class DoublyLinkedListNode:
    def __init__(self, element):
        self.element = element
        self.next = None
        self.prev = None

    def getElement(self):
        return self.element

    def getNext(self):
        return self.next

    def getPrev(self):
        return self.prev
