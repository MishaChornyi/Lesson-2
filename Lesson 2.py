class Cat:
    def __init__(self, name, age, say):
        self.name = name
        self.age = age
        self.say = say

    def print_age(self):
        print(self.age)

    def print_name(self):
        print(self.name)

    def print_say(self):
        print(self.say)

first_cat = Cat("Orange", 5, "Мяв")
second_cat = Cat("Gray", 6, "Маяу")
third_cat = Cat("Rare", 8, "Мяяу")
fourth_cat = Cat("Ricky", 7, "Мау")
fifth_cat = Cat("Shadow", 9, "Мяу")

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

first_cat.print_say()
second_cat.print_say()
third_cat.print_say()
fourth_cat.print_say()
fifth_cat.print_say()
