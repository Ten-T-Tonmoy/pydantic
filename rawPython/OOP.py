## basically python OOP


class Dog:
    # contructor
    # it will always be self and __init__ bruh
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed  # self.breed instance var all accesible
        self._age = None  # protected
        self.__address = None  # private
        self.height = None  # optional

    def bark(self):
        print(f"{self.name} says woof woof !")

    def getBreed(self):
        print(f" {self.name} is a {self.breed} breed dog")

    @staticmethod  # decorator
    def lookUp(arr, x):  ## basically static method
        return x in arr


dog1 = Dog("charlie", "labrador")  # new keyword not needed
dog1.getBreed()
dog1.price = 1200  # custom attribute bruh


# inheritance


class Husky(Dog):
    # if not defined it auto uses parents
    def __init__(self, name, breed):
        super().__init__(name, breed)
        # basically directly call methods from parent

    def bark(self):
        print("Silence a wild husky is burking")

    def yap(self):
        print("Ofc he is a yapper")


# magic methods __method__
# __init__() ->constructor
# __str__()-> string version of  obj

husky1 = Husky("Lama", "husky")
husky1.bark()

# static method can use without instantiating
print(Dog.lookUp(["a", "b", "c"], "b"))
