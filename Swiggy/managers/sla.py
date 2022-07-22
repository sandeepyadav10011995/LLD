from .utils.utility import distanceBetween


class SLA:
    @staticmethod
    def findSLA(restaurant, customer, speed):
        distanceBetweenCustomerAndRestaurant = distanceBetween(restaurant.getLocation(), customer.getLocation())
        maxPrepTime = 0
        for item in customer.getCart().getItems():
            if distanceBetweenCustomerAndRestaurant > item.getMaxDistanceCanTravel():
                raise Exception(
                    "Cannot fulfil order as the item " + item.getItemName() + " cannot be delivered in the given time")
            maxPrepTime = max(maxPrepTime, item.getPreparationTime())

        # Delivery Time = Max (Assignment Delay + First Mile Time, Prep Time) + Last Mile Time
        # here we assume prep time is more than assignment delay + first mile time
        # i.e. time to reach restaurant by delivery executive
        # this is for sake of simplicity.
        totalTime = (distanceBetweenCustomerAndRestaurant / speed) + maxPrepTime
        return totalTime
