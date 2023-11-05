"""
The below shows hybrid inheritance since it contains multi-level inheritance
and hierarchical inheritance
"""

from abc import ABC


# Abstract base parent class
# Uses ABC (stands for ABstractClass) to signify that the whole class is
# abstract
class Vehicle(ABC):
    # Private class attribute
    _wheels = 0

    def __str__(self) -> str:
        pass


# Intermediary subclass child class
# Hierarchical inheritance
# LandVehicle is a child of Vehicle and therefore inherits everything from the
# Vehicle abstract base parent class
class LandVehicle(Vehicle):
    pass


# Subclass child class
# Multi-level inheritance
# Hierarchical inheritance
# Car is a child of LandVehicle and inherits everything from LandVehicle
# which inherits everything from the Vehicle abstract base parent class
class Car(LandVehicle):
    # Overrides the _wheels private class attribute from the Vehicle abstract
    # base parent class
    def __init__(self):
        self._wheels = 4

    # Overrides the __str__ dunder method from the Vehicle abstract base
    # parent class
    def __str__(self) -> str:
        return f"I drive on land and transport you with {self._wheels} wheels"


# Subclass child class
# Multi-level inheritance
# Hierarchical inheritance
# CityBus is a child of LandVehicle and inherits everything from LandVehicle
# which inherits everything from the Vehicle abstract base parent class
class CityBus(LandVehicle):
    # Overrides the _wheels private class attribute from the Vehicle abstract
    # base parent class
    def __init__(self):
        self._wheels = 6

    # Overrides the __str__ dunder method from the Vehicle abstract base
    # parent class
    def __str__(self) -> str:
        return f"I drive on land and transport you with {self._wheels} wheels"


# Intermediary subclass child class
# Hierarchical inheritance
# WaterVehicle is a child of Vehicle and therefore inherits everything from the
# Vehicle abstract base parent class
class WaterVehicle(Vehicle):
    pass


# Subclass child class
# Multi-level inheritance
# Boat is a child of WaterVehicle and inherits everything from WaterVehicle
# which inherits everything from the Vehicle abstract base parent class
class Boat(WaterVehicle):
    # Overrides the __str__ dunder method from the Vehicle abstract base
    # parent class and since it inherited the _wheels private class attribute
    # it is left as is and not overridden since it does not need to be changed
    def __str__(self) -> str:
        return f"I float on water and transport you with {self._wheels} wheels"


child_vehicle1 = Car()
print(child_vehicle1)

child_vehicle2 = CityBus()
print(child_vehicle2)

child_vehicle3 = Boat()
print(child_vehicle3)
