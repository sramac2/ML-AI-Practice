class Vehicle:
    def __init__(self) -> None:
        self.wheels = 3

    def gen_usage(self):
        print('general use: transport')


class Car(Vehicle):
    def __init__(self):
        print('im car')
        self.wheels = 4


class Motorcycle(Vehicle):
    def __init__(self) -> None:
        super().__init__()


c = Car()
print(c.wheels)

# Multiple inheritance


class Father():
    def hobby(self):
        print('running... in Father')


class Mother():
    def hobby(self):
        print('running... in Mother')


class Combine(Father, Mother):
    def hobby(self):
        super().hobby()


c = Combine()
c.hobby()
