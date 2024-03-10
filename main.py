class Animal:
    def __init__(self, animalName, jumpHeight):
        self.jumpHeight = jumpHeight
        self.animalName = animalName

    def Jump(self):
        print(f"{self.animalName} jumped {self.jumpHeight}m!")

class Dog(Animal):
    def Sound(self):
        print(f"{self.animalName} is barking!")

class Cat(Animal):
    def Sound(self):
        print(f"{self.animalName} is meowing!")

if __name__ == "__main__":
    zoo = []
    while True:
        animalType = input("Введите тип животного (Dog или Cat). Enter - закончить ввод:").lower()
        if animalType == "":
            break
        elif animalType == "dog" or animalType == "cat":
            animalName = input("Введите имя животного:")
            animalJumpHeight = input("Введите высоту, на которую может прыгать животное:")
            if animalType == "dog":
                zoo.append(Dog(animalName, animalJumpHeight))
            elif animalType == "cat":
                zoo.append(Cat(animalName, animalJumpHeight))

    for animal in zoo:
        animal.Sound()
        animal.Jump()

