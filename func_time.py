import time

def time_taken(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        resp = func(*args, **kwargs)
        end = time.time()
        return (end - start)

    return wrapper


def timeit(cls):
    for key, val in vars(cls).items():
        if callable(val):
            setattr(cls, key, time_taken(val))
    return cls

class TimeMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        obj = super().__new__(cls, clsname, bases, clsdict)
        obj = timeit(obj)
        return obj


class Animal(metaclass=TimeMeta):
    def talk(self):
        time.sleep(1)
        print("Animal talk")

class Cow(Animal):
    def talk(self):
        time.sleep(1)
        print("Moo")

class Dog(Animal):
    def talk(self):
        time.sleep(1)
        print("Bark")


animal = Animal()
cow = Cow()
dog = Dog()

print(animal.talk())
print(cow.talk())
print(dog.talk())


