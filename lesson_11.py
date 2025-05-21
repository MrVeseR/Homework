# 3
class Student:
    __slots__ = {"name", "age", "grade"}

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = self.val(grade)

    @staticmethod
    def val(v):
        if not isinstance(v, int):
            raise TypeError("not int")
        elif v < 0: raise ValueError("menishe nulla")
        else: return v

s = [Student("vas", 11, 5), Student("vas", 11, 4), Student("vas", 11, 2)]

def srzn(sp):
    sm = 0
    for i in sp:
        sm += i.grade
    return sm/len(sp)

print(srzn(s))

# 4
class Product:
    __slots__ = {"name", "price", "quantity"}

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = self.val(price)
        self.quantity = quantity

    @staticmethod
    def val(v):
        if not isinstance(v, int) and not isinstance(v, float):
            raise TypeError("not int")
        elif v < 0: raise ValueError("menishe nulla")
        else: return v

a = Product("vasia", 15, 2)
b = Product("asdf", 20, 1)
c = Product("gag", 300, 1)

sl = {a.name: a, b.name: b, c.name: c}

def tov_s_porogom(s, porog):
    sp = []
    for i in s:
        if s[i].price > porog:
            sp.append(s[i].name)
    return sp

ag = tov_s_porogom(sl, 50)
print(ag)