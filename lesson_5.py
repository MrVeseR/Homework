class Fraction:

    def __init__(self, top, down):
        self.__top = self.validate_top(top)
        self.__down = self.validate_down(down)  

    def __str__(self):
        return f"{self.__top}/{self.__down}"
    def __repr__(self):
        return self.__str__()
        
    @property
    def value(self): return round(self.__top/self.__down, 3)

    @staticmethod
    def validate_top(top):
        if isinstance(top, int):
            return top
        else:
            print("wrong num, set default 1")
            return 1
    
    @staticmethod
    def validate_down(down):
        if down == 0:
            print("wrong num, set default 1")
            return 1
        elif isinstance(down, int):
            return down
        else:
            print("wrong num, set default 1")
            return 1
        
    def __add__(self, other):
        if isinstance(other, Fraction):
            down = self.__down * other.__down
            top = other.__down * self.__top + other.__top * self.__down
            return Fraction(top, down)
    def __radd__(self, other):
        return self.__add__(other)
    
    def __sub__(self, other):
        if isinstance(other, Fraction):
            down = self.__down * other.__down
            top = other.__down * self.__top - other.__top * self.__down
            return Fraction(top, down)
        
    def __mul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.__top * other.__top, self.__down * other.__down)
        
    def __truediv__(self, other):
        if isinstance(other, Fraction):
            num = Fraction(other.__down, other.__top)
            return self.__mul__(num)
        
class FractionMatrix:
    
    def __init__(self, data):
        self.__data = self.validate(data)
        self.__strs = len(self.__data)
        self.__cols = len(self.__data[0])
        
    @classmethod
    def validate(self, data):
        flag = True
        if isinstance(data, list):
            for matrixString in data:
                if not isinstance(matrixString, list):
                    flag = False
                    print("not my inst")
                elif len(matrixString) != len(data[0]):
                    flag = False
                    print("not my str")
                else:
                    for frac in matrixString:
                        if not isinstance(frac, Fraction):
                            flag = False
                            print("not my frac")
        if flag:
            return data
        else:
            print("no")
            return [[Fraction(1, 1), Fraction(0, 1)], [Fraction(0, 1), Fraction(1, 1)]]
        
    def __str__(self):
        s = ""
        for i in range(len(self.__data)):
            for j in range(len(self.__data[i])):
                s += str(self.__data[i][j].value) + "\t"      #value
            s += "\n"
        return s

    def get_data(self):
        return self.__data
    
    def __add__(self, other):
        if isinstance(other, FractionMatrix):
            if self.__strs == other.__strs and self.__cols == other.__cols:
                m = list()
                for i in range(len(self.__data)):
                    m.append([])
                    for j in range(len(self.__data[i])):
                        m[i].append(self.__data[i][j] + other.__data[i][j])
                return FractionMatrix(m)
            else: raise ValueError("only same size")
        else: raise TypeError("only matrix")
        
    def __sub__(self, other):
        if isinstance(other, FractionMatrix):
            if self.__strs == other.__strs and self.__cols == other.__cols:
                m = list()
                for i in range(len(self.__data)):
                    m.append([])
                    for j in range(len(self.__data[i])):
                        m[i].append(self.__data[i][j] - other.__data[i][j])
                return FractionMatrix(m)
            else: raise ValueError("only same size")
        else: raise TypeError("only matrix")
    
    def __mul__(self, other):
        if isinstance(other, FractionMatrix):
            if self.__cols == other.__strs:
                m = [[Fraction(0, 1) for i in range(other.__cols)] for j in range(self.__strs)]
                for i in range(self.__strs):
                    for j in range(other.__cols):
                        for k in range(self.__cols):
                            m[i][j] += self.__data[i][k] * other.__data[k][j]
                return FractionMatrix(m)
            else: raise ValueError("only same size")
        else: raise TypeError("only matrix")
    
    @property
    def transponate(self):
        m = list()
        for i in range(len(self.__data)):
            m.append([])
            for j in range(len(self.__data[i])):
                m[i].append(self.__data[j][i])
        return  FractionMatrix(m)
    
    @staticmethod
    def minor(matr):
        return matr[0][0] * matr[1][1] - matr[0][1] * matr[1][0]
    
    def det(self, matr):
        if len(matr[0]) > 2:
            res = 0
            for i in range(len(matr[0])):
                m = list()
                for j in range(len(matr[0])):
                    if j != i:
                        m.append([self.__data[j][k] for k in range(1, len(matr[0]))])
                res += self.determinant(m) * matr[i][0] * (-1 + 2 * ((i + 1) % 2))
            return res
        else: return self.minor(matr)

    @property
    def determinant(self):
        if self.__cols == self.__strs:
            return self.det(self.__data)
        else: raise ValueError("only quadro")
        
m1 = FractionMatrix([[Fraction(1, 2), Fraction(1, 3)], [Fraction(2, 5), Fraction(3, 4)], [Fraction(1, 3), Fraction(22, 15)]])
m2 = FractionMatrix([[Fraction(1, 3), Fraction(2, 3)], [Fraction(1, 2), Fraction(2, 5)]])
m3 = m1 * m2
print(m2.determinant)

