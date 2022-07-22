import sys
# swiggy folder is at below location. including it in sys.path

# sys.path.append('/Users/spoylios/Desktop/mc')

# change path as per your system
from swiggy.models.item import Item
from swiggy.models.location import Location
from swiggy.models.cart import Cart
from swiggy.models.restaurant import Restaurant
from swiggy.models.customer import Customer
from swiggy.models.sensitivity import Sensitivity

from swiggy.managers.restaurant_display_manager import RestaurantDisplayManager
from swiggy.managers.sla import SLA

item1 = Item(1, 'dosa', 10, Sensitivity.LOW, 5)
item2 = Item(2, 'ice cream', 1, Sensitivity.HIGH, 1)

location_rest1 = Location(120.1, 120.2)
location_rest1 = Location(120.3, 120.4)
rest1 = Restaurant(1, location_rest1, 'Anand')
rest2 = Restaurant(2, location_rest1, 'Baskin Robbins')

rest1.addMenuItem(item1)
rest2.addMenuItem(item2)

cart = Cart()
cart.addItem(item1)

customer1_loc = Location(120.12, 120.23)
customer1 = Customer(1, cart, customer1_loc)

rest_list = RestaurantDisplayManager()._show([rest1, rest2], customer1, 2)
print(rest_list)

sla_delivery = SLA().findSLA(rest1, customer1, 2)
print(sla_delivery)
