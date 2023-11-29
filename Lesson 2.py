class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_age(self):
        print(self.age)

    def print_name(self):
        print(self.name)

first_cat = Cat("Orange", 5)
second_cat = Cat("Gray", 6)
third_cat = Cat("Rare", 8)
fourth_cat = Cat("Ricky", 7)
fifth_cat = Cat("Shadow", 9)

first_cat.print_age()
second_cat.print_age()
third_cat.print_age()
fourth_cat.print_age()
fifth_cat.print_age()

first_cat.print_name()
second_cat.print_name()
third_cat.print_name()
fourth_cat.print_name()
fifth_cat.print_name()
