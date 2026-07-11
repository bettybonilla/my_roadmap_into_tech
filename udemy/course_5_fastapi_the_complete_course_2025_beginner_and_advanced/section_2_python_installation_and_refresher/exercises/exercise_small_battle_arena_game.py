"""
Create a small battle arena game using the four pillars of OOP where characters can fight each other!
- Criteria:
    - Characters that can fight one another
    - Different types of enemies
        - Ex:
            - Ogre
            - Zombie
    - Each character has a different name, health points, attack points
- NOTE: The program below is polymorphic since it uses inheritance with method overriding which should be used with
caution
"""

import random
from typing import Self


class Character:
    def __init__(self, name: str, health_points: int, attack_points: int):
        self.name = name
        self.health_points = health_points
        self.attack_points = attack_points
        self.max_health_points = health_points

    def __str__(self) -> str:
        return f"{self.name} has {self.health_points} health points and has an attack damage of {self.attack_points}"

    def attack(self, enemy: Self):
        if self.still_alive() and enemy.still_alive():
            enemy.health_points = self.clamp(
                enemy.take_damage(self.attack_points), 0, enemy.max_health_points
            )

    def still_alive(self) -> bool:
        if self.health_points > 0:
            return True
        return False

    def take_damage(self, enemy_attack_points: int) -> int:
        return self.health_points - enemy_attack_points

    def take_health(self, hp_increase: int) -> int:
        return self.clamp(self.health_points + hp_increase, 0, self.max_health_points)

    def display_health_points(self):
        print(f"{self.name} HP: {self.health_points}")

    # Helper function
    # Using a clamp is typical in gaming and in programming in general so that your values are within an acceptable and
    # expected specific range, ensuring that they never fall below a minimum value or exceed above a maximum value
    @staticmethod
    def clamp(value: int, min_value: int, max_value: int) -> int:
        if value < min_value:
            return min_value
        elif value > max_value:
            return max_value
        else:
            return value

        # Alternative code
        # return max_value(min_value, min_value(value, max_value))


class Weapon:
    def __init__(self, weapon_name: str, ap_increase: int):
        self.weapon_name = weapon_name
        self.ap_increase = ap_increase


class Hero(Character):
    def __init__(self, name: str, health_points: int, attack_points: int):
        super().__init__(name, health_points, attack_points)
        self.weapon: Weapon | None = None

    def equip_weapon(self):
        if self.weapon is not None:
            self.attack_points += self.weapon.ap_increase

    def display_attack(self):
        print(f"{self.name} attacks for {self.attack_points} damage")

    @staticmethod
    def stares() -> str:
        return "** stares enemy down **"

    @staticmethod
    def intro_move() -> str:
        return "The hero gets into fighting stance"


class Enemy(Character):
    def __init__(self, name: str, health_points: int, attack_points: int):
        super().__init__(name, health_points, attack_points)

    def walk_forward(self) -> str:
        return f"{self.name} moves closer to you"

    def display_attack(self):
        print(f"{self.name} attacks for {self.attack_points} damage")

    @staticmethod
    def special_attack() -> str:
        return "Enemy has no special attack"

    @staticmethod
    def speak() -> str:
        return "I am an enemy, be prepared to fight!"


class Ogre(Enemy):
    def __init__(self):
        super().__init__(name="Ogre", health_points=20, attack_points=5)

    # Method override
    def special_attack(self) -> str:
        return "Ogre has no special attack"

    # Method override
    @staticmethod
    def speak() -> str:
        return "** snarls **"

    @staticmethod
    def intro_move() -> str:
        return "The ogre slams things around"


class Zombie(Enemy):
    def __init__(self):
        super().__init__(name="Zombie", health_points=15, attack_points=3)

    # Method override
    def special_attack(self) -> str:
        if self.still_alive():
            special_attack_worked = random.random() > 0.5
            if special_attack_worked:
                old_health_points = self.health_points
                new_health_points = self.take_health(2)
                self.health_points = new_health_points
                gained_health_points = new_health_points - old_health_points
                if gained_health_points == 0:
                    return "Zombie already at max HP!"
                return f"Zombie regenerated {gained_health_points} HP!"
            return "Zombie's special attack failed!"

    # Method override
    @staticmethod
    def speak() -> str:
        return "** grumbles **"

    @staticmethod
    def intro_move() -> str:
        return "The zombie is trying to spread disease"


# Application logic
def enemy_battle(e1: Enemy, e2: Enemy):
    print("\n-------- ENEMY BATTLE --------\n")

    print(e1)
    print(f"{e1.speak()}\n{e1.intro_move()}\n")
    print(e2)
    print(f"{e2.speak()}\n{e2.intro_move()}\n")
    print("----------" * 3)

    while True:
        if e1.still_alive() and e2.still_alive():
            e1.display_attack()
            e1.attack(e2)
            e2.display_health_points()
            if e2.still_alive():
                print(e1.special_attack())
                print("----------" * 3)
            if e1.still_alive() and e2.still_alive():
                e2.display_attack()
                e2.attack(e1)
                e1.display_health_points()
                if e1.still_alive():
                    print(e2.special_attack())
                    e2.display_health_points()
                    print("----------" * 3)
        else:
            if e1.health_points > 0:
                print("----------" * 3)
                print(f"{e1.name} wins!")
                break
            print("----------" * 3)
            print(f"{e2.name} wins!")
            break


def hero_battle(hero: Hero, enemy: Enemy):
    print("\n-------- HERO BATTLE --------\n")

    print(hero)
    print(f"{hero.stares()}\n{hero.intro_move()}\n")
    print(enemy)
    print(f"{enemy.speak()}\n{enemy.intro_move()}\n")
    print("----------" * 3)

    while True:
        if hero.still_alive() and enemy.still_alive():
            hero.display_attack()
            hero.attack(enemy)
            enemy.display_health_points()
            print("----------" * 3)
            if hero.still_alive() and enemy.still_alive():
                enemy.display_attack()
                enemy.attack(hero)
                hero.display_health_points()
                if hero.still_alive():
                    print(enemy.special_attack())
                    enemy.display_health_points()
                    print("----------" * 3)
        else:
            if hero.health_points > 0:
                print(f"{hero.name} wins!")
                break
            print(f"{enemy.name} wins!")
            break


if __name__ == "__main__":
    link = Hero("Link", 100, 5)
    lynel = Enemy("Lynel", 50, 100)
    ogre = Ogre()
    zombie = Zombie()
    print(link)
    print(lynel)
    print(ogre)
    print(zombie)
    print("")

    print(lynel.walk_forward())
    lynel.display_attack()
    print(lynel.speak())
    print("")

    print(ogre.walk_forward())
    ogre.display_attack()
    print(ogre.speak())
    print(ogre.intro_move())
    print("")

    print(zombie.walk_forward())
    zombie.display_attack()
    print(zombie.speak())
    print(zombie.intro_move())

    enemy_battle(ogre, zombie)

    zombie = Zombie()
    weapon = Weapon("sword", 5)
    link.weapon = weapon
    link.equip_weapon()

    hero_battle(link, zombie)
