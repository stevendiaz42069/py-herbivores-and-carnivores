from __future__ import annotations


class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.health = health
        self.name = name
        self.hidden = False
        self.__class__.alive.append(self)

    def die(self) -> None:
        if self in self.__class__.alive:
            self.__class__.alive.remove(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, prey: "Animal") -> None:
        if isinstance(prey, Carnivore) or prey.hidden:
            return
        prey.health -= 50
        if prey.health <= 0:
            prey.die()
