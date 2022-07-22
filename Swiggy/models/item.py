class Item:
    def __init__(self, itemId, itemName, preparationTime, sensitivity, maxDistanceCanTravel):
        self.itemId = itemId
        self.itemName = itemName
        self.preparationTime = preparationTime
        self.sensitivity = sensitivity
        self.maxDistanceCanTravel = maxDistanceCanTravel

    def getItemId(self):
        return self.itemId

    def setItemId(self, itemId):
        self.itemId = itemId

    def getItemName(self):
        return self.itemName

    def setItemName(self, itemName):
        self.itemName = itemName

    def getPreparationTime(self):
        return self.preparationTime

    def setPreparationTime(self, preparationTime):
        self.preparationTime = preparationTime

    def getSensitivity(self):
        return self.sensitivity

    def setSensitivity(self, sensitivity):
        self.sensitivity = sensitivity

    def getMaxDistanceCanTravel(self):
        return self.maxDistanceCanTravel

    def setMaxDistanceCanTravel(self, maxDistanceCanTravel):
        self.maxDistanceCanTravel = maxDistanceCanTravel
