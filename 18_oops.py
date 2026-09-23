# Demonstration of Abstraction using abc
from abc import ABC, abstractmethod

class AbstractExample(ABC):
    @abstractmethod
    def do_something(self):
        pass

    @classmethod
    def class_method_example(cls):
        return "This is a class method in the abstract class"

class ConcreteExample(AbstractExample):
    def do_something(self):
        return "Doing something in the concrete class"

# Example usage
obj = ConcreteExample()
print(obj.do_something())  # Output: Doing something in the concrete class
print(ConcreteExample.class_method_example())  # Output: This is a class method in the abstract class