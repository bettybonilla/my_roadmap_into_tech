from abc import ABC


# Abstract base parent Vehicle class
# Uses ABC (stands for ABstractClass) to signify that the whole class is
# abstract
class Vehicle(ABC):
    # Private class attribute
    _wheels = 0

    def __str__(self) -> str:
        pass


# Subclass child LandVehicle class
# LandVehicle is a child of Vehicle and therefore inherits everything from the
# abstract base parent Vehicle class
class LandVehicle(Vehicle):
    pass


# Subclass child Car class
# Car is a child of LandVehicle and inherits everything from LandVehicle
# which inherits everything from the abstract base parent Vehicle class
class Car(LandVehicle):
    # Overrides the _wheels private class attribute from the abstract base
    # parent Vehicle class
    def __init__(self):
        self._wheels = 4

    # Overrides the __str__ dunder method from the abstract base parent
    # Vehicle class
    def __str__(self) -> str:
        return f"I drive on land and transport you with {self._wheels} wheels"


# Subclass child CityBus class
# CityBus is a child of LandVehicle and inherits everything from LandVehicle
# which inherits everything from the abstract base parent Vehicle class
class CityBus(LandVehicle):
    # Overrides the _wheels private class attribute from the abstract base
    # parent Vehicle class
    def __init__(self):
        self._wheels = 6

    # Overrides the __str__ dunder method from the abstract base parent
    # Vehicle class
    def __str__(self) -> str:
        return f"I drive on land and transport you with {self._wheels} wheels"


# Subclass child WaterVehicle class
# WaterVehicle is a child of Vehicle and therefore inherits everything from the
# abstract base parent Vehicle class
class WaterVehicle(Vehicle):
    pass


# Subclass child Boat class
# Boat is a child of WaterVehicle and inherits everything from WaterVehicle
# which inherits everything from the abstract base parent Vehicle class
class Boat(WaterVehicle):
    # Overrides the __str__ dunder method from the abstract base parent
    # Vehicle class and since it inherited the _wheels private class attribute
    # it is left as is and not overriden since it does not need to be changed
    def __str__(self) -> str:
        return f"I float on water and transport you with {self._wheels} wheels"


child_vehicle1 = Car()
print(child_vehicle1)

child_vehicle2 = CityBus()
print(child_vehicle2)

child_vehicle3 = Boat()
print(child_vehicle3)
