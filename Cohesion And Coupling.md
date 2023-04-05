
Cohesion : It is the degree to which elements of a certain class or function belong together. A function should not do a
           lot of different things that do not really belong together. A function with strong Cohesion has clear
           responsibility.

Coupling : It is a measure of how two parts of your code are dependent on each other. High Coupling is problematic and
           not good.
           
Github Repo Link -: https://github.com/arjancodes/betterpython

## Cohesion & Coupling --> Before

```
import string
import random


class VehicleRegistry:

  def generate_vehicle_id(self, length):
     return ''.join(random.choices(string.ascii_uppercase, k=length))

  def generate_vehicle_license(self, id):
     return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"

```


```
class Application:

    def register_vehicle(self, brand: string):
        # create a registry instance
        registry = VehicleRegistry()

        # generate a vehicle id of length 12
        vehicle_id = registry.generate_vehicle_id(12)

        # now generate a license plate for the vehicle
        # using the first two characters of the vehicle id
        license_plate = registry.generate_vehicle_license(vehicle_id)

        # compute the catalogue price
        catalogue_price = 0
        if brand == "Tesla Model 3":
            catalogue_price = 60000
        elif brand == "Volkswagen ID3":
            catalogue_price = 35000
        elif brand == "BMW 5":
            catalogue_price = 45000

        # compute the tax percentage (default 5% of the catalogue price, except for electric cars where it is 2%)
        tax_percentage = 0.05
        if brand == "Tesla Model 3" or brand == "Volkswagen ID3":
            tax_percentage = 0.02

        # compute the payable tax
        payable_tax = tax_percentage * catalogue_price

        # print out the vehicle registration information
        print("Registration complete. Vehicle information:")
        print(f"Brand: {brand}")
        print(f"Id: {vehicle_id}")
        print(f"License plate: {license_plate}")
        print(f"Payable tax: {payable_tax}")


app = Application()
app.register_vehicle("Volkswagen ID3")

```

## Cohesion & Coupling --> After 
```
class VehicleInfo:

    def __init__(self, brand: str, electric: bool, catalogue_price: float):
        self.brand = brand
        self.electric = electric
        self.catalogue_price = catalogue_price

    def compute_tax(self):
        tax_percentage = 0.02 if self.electric else 0.05
        return tax_percentage * self.catalogue_price

    def print(self):
        print(f"Brand: {self.brand}")
        print(f"Payable tax: {self.compute_tax()}")


class Vehicle:

    def __init__(self, id: str, license_plate: str, info: VehicleInfo):
        self.id = id
        self.license_plate = license_plate
        self.info = info

    def print(self):
        print(f"Id: {self.id}")
        print(f"License plate: {self.license_plate}")
        self.info.print()


class VehicleRegistry2:

    def __init__(self) -> None:
        self.vehicle_info = {}
        self.add_vehicle_info("Tesla Model 3", True, 60000)
        self.add_vehicle_info("Volkswagen ID3", True, 35000)
        self.add_vehicle_info("BMW 5", False, 45000)
        self.add_vehicle_info("Tesla Model Y", True, 75000)

    def add_vehicle_info(self, brand: str, electric: bool, catalogue_price: float) -> None:
        self.vehicle_info[brand] = VehicleInfo(brand, electric, catalogue_price)

    @staticmethod
    def generate_vehicle_id(length) -> str:
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    @staticmethod
    def generate_vehicle_license(id) -> str:
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"

    def create_vehicle(self, brand: str) -> Vehicle:
        id = self.generate_vehicle_id(12)
        license_plate = self.generate_vehicle_license(id)
        return Vehicle(id, license_plate, self.vehicle_info[brand])


class Application:

    @staticmethod
    def register_vehicle(brand: str) -> Vehicle:
        # create a registry instance
        registry = VehicleRegistry2()
        return registry.create_vehicle(brand)


app = Application()
vehicle = app.register_vehicle("Volkswagen ID3")
# print out the vehicle registration information
print("Registration complete. Vehicle information:")
vehicle.print()
```
