# Generate an example of monkey patching in python class methods
class Example:
    def __init__(self, name):
        self.name = name
        self.message = "Hello"

    def greet(self):
        return f"{self.message}, {self.name}"

# Original behavior
obj = Example("Alice")
print(obj.greet())  # Output: Hello

# Monkey patching the greet method
def new_greet(self):
    return f"Hi, {self.name}"

Example.greet = new_greet
print(obj.greet())  # Output: Hi, Alice

obj.city = "New York"
print(obj.city)  # Output: New York

# Class is a dict behind the scenes
print(obj.__dict__)
