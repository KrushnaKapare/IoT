
class Person:
    def __init__(self, pname='',page =0):
        self.__name = pname
        self.__age = page

    def display(self):
        print(f"person ={self.__name} [{self.__age}]")

    def can_vote(self):
        if self.__age >= 18:
            print(f"{self.__name} person can vote")
        else:
            print(f"{self.__name} person can not vote")

p1 = Person('abc', 35)
p1.display()
p1.can_vote()

p2 = Person('xyz',17)
p2.display()
p2.can_vote()

