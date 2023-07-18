class Animals():
    def __init__(self, name, age):

        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.name

class Dog(Animals):
    def __init__(self, color, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = color

    def talk(self):
        return 'Гав-гав'

class Cat(Animals):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def talk(self):
        return 'мяу-мяу'

class Pets:
    typeOfAnimals = ["Dog", "Cat"]
    def __init__(self, animalType, *args, **kwargs):
        self.animalType = animalType
        if self.animalType == "Dog":
            self.animal = Dog(*args,**kwargs)
        elif self.animalType == "Cat":
            self.animal = Cat(*args, **kwargs)

    def talk(self):
        typeOfAnimal = self.animal.getType()
        print(typeOfAnimal)

if __name__=="__main__":
    pes = Pets("Dog","White", "Sharik", 4)
    print(pes.animal.getName())
    print(pes.animal.talk())

    kot = Pets("Cat", "Barsik", 2)
    print(kot.animal.getName())
    print(kot.animal.talk())