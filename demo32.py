class Person:
    def __init__(self, pname='',page=0):
        self.name = pname
        self.age = page

    def __del__(self):
        print("deinitializer is called")

    def display(self):
        print(f"name = {self.name},age = {self.age}")

p1 = Person()
p1.display()

p2= Person('abc',35)
p2.display()

