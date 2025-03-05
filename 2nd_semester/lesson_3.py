import random

# 2
class User:

    __username = ""
    __password = ""

    def __init__(self, username, password):
        self.__username = username
        self.__password = password
    
    @classmethod
    def create_default_user(cls, username):
        password = str(random.randint(10**6, 10**12))
        return cls(username, password)
    
    @staticmethod
    def validate(password):
        return len(password) >= 6
    
    def set_password(self, password):
        if self.validate(password):
            self.__password = password
        else:
            print("dlinnee!")

    def get_password(self):
        return self.__password

# a = User.create_default_user("Alice")
# print(a.get_password())
# a.set_password("123")
# a.set_password("3280roi3h28")
# print(a.get_password())

# 3
class Book:
    __title = ""
    __author = ""
    __year = 0

    def __init__(self, title, author, year):
        self.__title = title
        self.__author = author
        self.__year = self.validate(year)
    
    @staticmethod
    def validate(year):
        if type(year) == int and year <= 2025:
            return year
        else:
            print("the year is not valide, default setted")
            return 2024

    @classmethod
    def create_default_year(cls, title, author):
        return cls(title, author, 2024)
    
    def get_info(self):
        return(f"output: {self.__title}, author: {self.__author}, year: {self.__year}")
    
# b1 = Book("mishk frede", "scottina", 1987)
# b2 = Book.create_default_year("Elden ring: Shadow of the Erdtree", "Ne Hidetaka miyadzaki")
# b3 = Book("gta shest", "take two, ne rokstar", 2026)

# print(b1.get_info())
# print(b2.get_info())
# print(b3.get_info())