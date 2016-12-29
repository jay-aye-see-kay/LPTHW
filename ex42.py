## Animal is-a object
class Animal(object):
    pass

## Dog is-a animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name
        self.name = name

## Cat is-a animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## Person has a name
        self.name = name

        ## Person has a pet of some kind
        self.pet = None

## Employee is-a person
class Employee(Person):

    def __init__(self, name, salary):
        ## runs the init of the class above (Person)
        super(Employee, self) __init__(name)
        ## Employee has-a salary
        self.salary = salary

 ## Fish is-a object
 class Fish(object):
     pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## Mary is-a Person
mary = Person("Mary")

## Mary has a pet Cat satan
mary.pet = satan

## Frank is-a employee making 120k
frank = Employee("Frank", 120000)

## Frank has-a pet dog, rover
frank.pet = rover

## Flipper is-a Fish
flipper = Fish()

## Crouse is a Salmon
crouse = Salmon()

## Harry is-a Halibut
harry = Halibut()
