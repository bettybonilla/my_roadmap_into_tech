"""
Similar to a library management system, write a program to provide layers of
abstraction for a car rental system
- Your program should perform the following:
    - Hatchback, Sedan, SUV should be the type of cars that are being provided
    for rent
    - Cost per day:
        - Hatchback: $30
        - Sedan: $50
        - SUV: $100
    - Give a prompt to the customer asking him the type of car and the number
    of days he would like to rent and provide the fare details to the customer
"""

from dataclasses import dataclass


@dataclass
class _CarInformation:
    def __init__(self, car_type: str, cost_per_day: int):
        self.car_type = car_type
        self.cost_per_day = cost_per_day

    def __repr__(self) -> str:
        return f"{self.car_type}: ${self.cost_per_day}"


class CarRental:
    _cars_for_rent_per_day: list[_CarInformation] = [
        _CarInformation("Hatchback", 30),
        _CarInformation("Sedan", 50),
        _CarInformation("SUV", 100),
    ]

    @staticmethod
    def pricing_details(
        requested_car_for_rent: str, requested_days_for_rent: int
    ) -> bool:
        for i in CarRental._cars_for_rent_per_day:
            if requested_car_for_rent == i.car_type:
                total = i.cost_per_day * requested_days_for_rent
                print("\nBelow are your pricing details\n")
                print(f"Car Type: {requested_car_for_rent}")
                print(f"Cost per Day: ${i.cost_per_day}")
                print(f"Days for Rent: {requested_days_for_rent}")
                print(f"Total: ${total}")
                return True
        return False

    @staticmethod
    def display_cars_for_rent_per_day():
        for car in CarRental._cars_for_rent_per_day:
            print(car)


class Customer:
    def __init__(self):
        self.car = None
        self.days = None

    def request_car_for_rent(self) -> str | bool:
        self.car = input()
        for i in CarRental._cars_for_rent_per_day:
            if self.car == i.car_type:
                return self.car
        return False

    def request_days_for_rent(self) -> int:
        self.days = int(input())
        return self.days


car_rental = CarRental()
customer = Customer()

print("Welcome!\n")

while True:
    print("Enter 1 to display cars for rent per day")
    print("Enter 2 to request a car for rent")
    print("Enter 3 to exit\n")

    user_choice = int(input())

    match user_choice:
        case 1:
            print("\nCars for Rent per Day\n")
            car_rental.display_cars_for_rent_per_day()
            print("")
        case 2:
            print("\nEnter the type of car you would like to rent:")
            requested_car_for_rent = customer.request_car_for_rent()
            if requested_car_for_rent:
                print("\nEnter the number of days you would like to rent:")
                requested_days_for_rent = customer.request_days_for_rent()
                if car_rental.pricing_details(
                    requested_car_for_rent, requested_days_for_rent
                ):
                    print("")
            else:
                print("\nSorry that car is not available\n")
        case 3:
            quit(0)
        case _:
            print("\nPlease enter a valid choice!\n")
