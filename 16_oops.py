# Create a class with an example for demonstration of private attributes in Python
class Example:
    def __init__(self, value):
        self.__private_attribute = value

    def get_private_attribute(self):
        return self.__private_attribute

    def set_private_attribute(self, value):
        self.__private_attribute = value

# Example usage
obj = Example(10)
print(obj.get_private_attribute())  # Output: 10
obj.set_private_attribute(20)
print(obj.get_private_attribute())  # Output: 20
#print(obj.__private_attribute)  # This will raise an AttributeError because __private_attribute is private