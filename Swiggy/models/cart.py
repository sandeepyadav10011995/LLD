class Cart:
    def __init__(self):
        self.items = []

    def addItem(self, item):
        self.items.append(item)

    def removeItem(self, item):
        self.items.remove(item)

    def getItems(self):
        return self.items

    def clearCart(self):
        self.items = []
