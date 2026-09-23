class Person:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def get_city(self):
        return self.city

    def __str__(self):
        return f"Person(Name={self.name},City={self.city})"

class User(Person):
    def __init__(self, name, city, email):
        super().__init__(name, city)
        self.email = email

    def get_city(self):
        return self.city

    def __str__(self):
        return f"User(Name={self.name},City={self.city},Email={self.email})"

if __name__ == '__main__':
    p1 = Person("Vishwas", "Pune")
    # print(p1.get_city())

    # print(p1.city)
    # print(p1.name)
    print(p1)

    u1 = User("Riya","Pune","riya.p@gmail.com")
    # print(u1.get_city())
    # print(u1.name)
    print(u1)