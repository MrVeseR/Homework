# 3

class Car:
    
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __getattr__(self, item):
        print(f"attribute {item} not found")
    
# c = Car("toyota", "corolla")
# print(c.make)
# print(c.model)
# print(c.color)

# 4
class Rctangle:

    def __init__(self, width, height):
        self.__dict__["width"] = width
        self.__dict__["height"] = height

    def __setattr__(self, name, value):
        if name not in self.__dict__:
            raise AttributeError("Local attributes are not allowed")
        else:
            self.__dict__[name] = value

# r = Rctangle(10, 20)
# print(r.width)
# r.height = 122
# print(r.height)
# r.color = "jojo"