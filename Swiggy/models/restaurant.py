class Restaurant:
    def __init__(self, restaurantId, location, name):
        self.restaurantId = restaurantId
        self.location = location
        self.name = name
        self.menuItems = []

    def getRestaurantId(self):
        return self.restaurantId

    def setRestaurantId(self, restaurantId):
        self.restaurantId = restaurantId

    def getLocation(self):
        return self.location

    def setLocation(self, location):
        self.location = location

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getMenuItems(self):
        return self.menuItems

    def addMenuItem(self, item):
        self.menuItems.append(item)

    def removeMenuItem(self, item):
        self.menuItems.remove(item)
