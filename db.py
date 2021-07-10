# SingleTone


class Person:
    name = ""
    age = 0
    gender = ""

    def data_setter(self, p1, p2, p3):
        self.name = p1
        self.age = p2
        self.gender = p3

    # java에서는 toString / python에서는 __str__
    # python의 첫 번째 파라미터는 무조건! self

    def __str__(self):
        return f"{self.name} | {self.age} | {self.gender}"

    def add_age(self):
        self.age = self.age + 1
