class Animals():
    def __init__(self, name, age, *args, **kwargs):
        self.name = name
        self.age = age


class Dog(Animals):
    def __init__(self, color, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = color

class Cat(Animals):
    def __init__(self, kind, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.kind = kind

class Bird(Animals):
    def __init__(self, wings, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.wings = wings

class Fabric():
    dictAnimal = {"Cat": Cat,
                  "Dog": Dog,
                  "Bird": Bird}

    def __init__(self, typeAnimal, *args, **kwargs):
        self.animal = self.dictAnimal[typeAnimal](*args, **kwargs)

# при сложении объектов одного класса создается копия
# если объекты разные то кто-то, кого-то скушает
    def __add__(self, other):
        typeOfobj1 = type(self.animal)
        typeOfobj2 = type(other.animal)

        if typeOfobj2==typeOfobj1 :
            CloneDict = self.animal.__dict__
            CloneDict["age"] = 0
            CloneDict["name"] = "copy"
            newObj = CloneDict
            return newObj
        elif typeOfobj1 == Dog or typeOfobj2 == Dog:
            return "Dog say's Ням ням"
        elif typeOfobj1 == Cat or typeOfobj2 == Cat:
            return "Cat say's Ням ням"


if __name__=="__main__":
    pes =Fabric("Dog", "Red", "Sharik", 3)
    kot =Fabric("Cat", "Russian","Pooshok", 2)
    pes2 = Fabric("Dog", "Blue", "Sobaka", 4)
    ptaha = Fabric("Bird", 120, "Opel", 5)
    pes3 = Dog("White", "Sharik", 3)
    print(kot.animal.__dict__)
    # print(pes.animal.__dict__)
    # print(pes2.animal.__dict__)
    # print(ptaha.animal.__dict__)

    # print(type(pes))
    # print(type(kot))
    #
    print(pes + kot)
    print(pes + ptaha)
    print(pes + pes2)
    print(kot + ptaha)
