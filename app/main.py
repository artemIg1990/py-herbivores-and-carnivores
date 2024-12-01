class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100,
                 hiden: bool = False) -> None:
        self.health = health
        self.hidden = hiden
        self.alive = True
        self.name = name
        Animal.alive.append(self)

    def check_alive(self) -> None:
        if self.health < 1:
            self.alive = False
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        if self.hidden == False:
            self.hidden = True
        elif self.hidden == True:
            self.hidden = False


class Carnivore(Animal):
    def bite(self, victim: object) -> None:
        if victim.__class__ != Carnivore and victim.hidden == False:
            victim.health -= 50
        victim.check_alive()
