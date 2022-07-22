class Customer:
    def __init__(self, customerId, cart, location):
        # not including other details like name,email
        # focusing on main attributes
        self.customerId = customerId
        self.cart = cart
        self.location = location

    def getCustomerId(self):
        return self.customerId

    def setCustomerId(self, customerId):
        self.customerId = customerId

    def getCart(self):
        return self.cart

    def setCart(self, cart):
        self.cart = cart

    def getLocation(self):
        return self.location

    def setLocation(self, location):
        self.location = location
