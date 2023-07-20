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

    # def sumAB(self, other):
    #
    #     if typeOfobj2==typeOfobj1 : return typeOfobj2
    #     elif typeOfobj1 == "Dog": print(self +" Ням ням")

    # def __add__(self, other):
    #     typeOfobj1 =
    #     typeOfobj2 =
    #     if typeOfobj2==typeOfobj1 : return typeOfobj2
    #     elif typeOfobj1 == "Dog" or typeOfobj2 == "Dog": print("Dog say's " +" Ням ням")
    #     elif typeOfobj1 == "Cat" or typeOfobj2 == "Cat":
    #         print("Cat say's " + " Ням ням")
    # def __str__(self):
    #     return str(self.v)

if __name__=="__main__":
    pes =Fabric("Dog", "Red", "Sharik", 3)
    kot =Fabric("Cat", "Russian","Pooshok", 2)
    pes2 = Fabric("Dog", "Blue", "Sobaka", 4)
    ptaha = Fabric("Bird", 120, "Opel", 5)
    pes3 = Dog("White", "Sharik", 3)
    print(kot.animal.__dict__)
    print(pes.animal.__dict__)
    print(pes2.animal.__dict__)
    print(ptaha.animal.__dict__)

    print(type(pes))
    print(type(kot))