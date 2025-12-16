class Person:
    def __init__(self):
        self.name = "abc"
        self.age = 35

    def display(self):
        print(f"name = {self.name},age = {self.age}")

p1=Person()
p1.display()

p2 = Person()
p2.name = 'xyz'
p2.age = 17
p2.display()