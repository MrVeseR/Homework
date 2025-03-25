#2
class Employee:

    def __init__(self, name, age, salary):
        self.__name = name
        self.__age = age
        self.__salary = salary
        self.__bonus = 0

    def get_name(self): return self.__name

    def get_age(self): return self.__age

    def get_salary(self): return self.__salary

    def set_bonus(self, bonus): self.__bonus = bonus

    def get_bonus(self): return self.__bonus

    def get_total_salary(self): return self.__salary + self.__bonus

# e = Employee("vasia", 162, 10000000)
# e.set_bonus(15)
# print(e.get_total_salary())

#3
class Recipe:

    def __init__(self, name: str, ingredients: list):
        self.__name = name
        self.__ingredients = ingredients

    def print_ingredients(self):
        print(f"ingrs for {self.__name}")
        for i in self.__ingredients:
            print("-", i)

    def cook(self):
        print(f"today we cook {self.__name}")
        print("Cecking the instruction...")
        print(f"{self.__name} is done!")

# spag = Recipe("spags", ["kartopla", "ris", "chesnok", "ktulhu", "nekonomikon(not cat at all)"])
# spag.print_ingredients()
# spag.cook()