class Animal:
    race: str
    color: str
    age: int 

    def __init__(self,race,color,age):
        self.race = race
        self.color = color
        self.age = age
    
    def __str__(self):
        return self.race

    def walk(self): # method
        return "i'm walking"

    def eat(self):
        return "i'm eating"
    
    def smash(self):
        raise NotImplementedError()
    
    def run(self):
        return "i'm running"

class HeavyAnimal:
    def smash(self):
        return "i'm smashing"

    def run(self):
        return super().run() + " slow"

class Rhino(HeavyAnimal,Animal): # mixing - a class that inherits from more than one parent class. Order is important - first parameter will overwrite a given attribute of parent(s) class. Executed from right to left.
    pass

class Snake(Animal):
    race: str = "snake"

class Elephant(Animal):
    race: str = "elephant"

    def __init__(self,color,age): # overwriting: redefining parent behaviors
        self.color = color
        self.age = age

    def walk(self):
        message = self._breath()
        return "i'm slow walking " + message
    
    def eat(self): # overloading: complementing a parent method with new additional attributes
        message = super().eat() # call parent method
        return message + " something else"

    def _breath(self): # private/local scope
        return "i'm breathing as well"

elephant = Elephant(
    color = "gray",
    age = 15)

rhino = Rhino(race="rhino",color="black",age=11)
snake = Snake(race="snake",color="yellow",age=1)

# print(elephant.__dict__)
# print(elephant.walk())

# print(rhino.smash())
# print(snake.smash())

print(rhino.run())