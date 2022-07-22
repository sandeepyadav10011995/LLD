from typing import Any

from algorithms.DoublyLinkedListNode import DoublyLinkedListNode


class DoublyLinkedList:
    def __init__(self):
        self.dummyHead = DoublyLinkedListNode(element=None)
        self.dummyTail = DoublyLinkedListNode(element=None)
        self.dummyHead.next = self.dummyTail
        self.dummyTail.prev = self.dummyHead
    
    @staticmethod
    def detachNode(node: DoublyLinkedListNode) -> None:
        if node is not None:
            node.prev.next = node.next
            node.next.prev = node.prev
            
    def addNodeAtFirst(self, node: DoublyLinkedListNode) -> None:
        pred = self.dummyHead
        succ = self.dummyHead.next
        pred.next = node
        node.prev = pred
        succ.prev = node
        node.next = succ
            
    def addElementAtFirst(self, element: Any) -> DoublyLinkedListNode:
        if element is None:
            pass
        newNode = DoublyLinkedListNode(element=element)
        self.addNodeAtFirst(newNode)
        return newNode
    
    def isItemPresent(self) -> bool:
        return self.dummyHead.next != self.dummyTail
    
    def getFirstNode(self) -> DoublyLinkedListNode:
        if not self.isItemPresent():
            pass
        return self.dummyHead.next

    def getLastNode(self) -> DoublyLinkedListNode:
        if not self.isItemPresent():
            pass
        return self.dummyTail.prev
    
            
