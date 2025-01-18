#import necessary packages
from abc import ABC
#create a base class 
class Animal(ABC):
    #abstract method
    #should be implemented by all sub classes
    def move(self):
        pass
    #sub class
class Human(Animal):
    def move(self):
        print("I can walk and run")
class snake(Animal):
    def move(self):
        print("I can crawl")
class Dog(Animal):
    def move(self):
        print("I can bark")
class lion(Animal):
    def move(self):
        print("I can roar")
#Driver code
R = Human()
R.move
k= snake()
k.move
R = Dog()
R.move
K = lion()
K.move