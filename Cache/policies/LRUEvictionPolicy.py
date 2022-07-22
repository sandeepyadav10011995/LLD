from algorithms.DoublyLinkedList import DoublyLinkedList
from cache.policies.EvictionPolicy import EvictionPolicy


class LRUEvictionPolicy(EvictionPolicy):
    def __init__(self):
        self.dll = DoublyLinkedList()
        self.mapper = dict()

    def keyAccessed(self, key):
        if key in self.mapper:
            self.dll.detachNode(self.mapper.get(key))
            self.dll.addNodeAtFirst(self.mapper.get(key))
        else:
            newNode = self.dll.addNodeAtFirst(key)
            self.mapper[key] = newNode

    def evictKey(self, key):
        res = self.dll.getLastNode()
        if res is None:
            return None
        self.dll.detachNode(res)
        return res.getElement()
