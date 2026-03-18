class Animal:
    sound: str
    def __init__(self, sound: str, color: str) -> None:
        self.sound = sound
        self.color = color
    def makeSound(self) -> None:
        print(self.sound)
    def showcolor(self) -> None: 
        print (self.color)
class Cat(Animal):
    def __init__(self) -> None:
        super().__init__("Meow!", "yellow")
        
class Dog(Animal):
    def __init__(self) -> None:
        super().__init__("Bark", "black") # ANIMAL IS SUUUUUUUUUPERRRRRRR it will ask from the animal and not anywhere else. 
    def makeSound(self) -> None:
        print("Who let the dogs out!?")

Cat().makeSound() # Meow!
Dog().makeSound() # Who let the dogs out!?

Dog().showcolor()
Cat().showcolor()