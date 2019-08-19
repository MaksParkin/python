import math


# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

class triangle:
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C
    def side_lenght(self, x, y):
        side_lenght = math.sqrt(math.pow((x[0] - y[0]), 2) + math.pow((x[1] - y[1]), 2))
        return side_lenght
    def sides(self, A, B, C):
        AB = triangle.side_lenght(self, A, B)
        BC = triangle.side_lenght(self, B, C)
        AC = triangle.side_lenght(self, A, C)
        return AB, BC, AC
    def Per(self, A, B, C):
        AB, BC, AC = triangle.sides(self, A, B, C)
        P = AB + AC + BC
        return P
    def Sq(self, A, B, C):
        P = triangle.Per(self, A, B, C)
        p = P / 2
        S = sqrt(p(p - AB)(p - BC)(p - AC))
        return S
    def height(self, A, B, C):
        S = triangle.Sq(self, A, B, C)
        AB = triangle.sides(self, A, B)
        BC = triangle.sides(self, B, C)
        AC = triangle.sides(self, A, C)
        h1 = (2 * S) / AB
        h2 = (2 * S) / BC
        h3 = (2 * S0 / AC)
        return h1, h2, h3


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class trapezium:
    def __init__(self, A, B, C, D):
        self.A = A
        self.B = B
        self.C = C
        self.D = D
    def side_lenght(self, x, y):
        side_lenght = math.sqrt(math.pow((x[0] - y[0]), 2) + math.pow((x[1] - y[1]), 2))
        return side_lenght
    def sides(self, A, B, C, D):
        AB = trapezium.side_lenght(self, A, B)
        BC = trapezium.side_lenght(self, B, C)
        CD = trapezium.side_lenght(self, C, D)
        AD = trapezium.side_lenght(self, A, D)
        return AB, BC, CD, AD
    def check_2_sides_eq(self):
        if AB == CD or BC == AD:
            print("Трапеция равнобедренная")
            return True
        else:
            print("Трапеция не равнобедренная")
            return False
    def Per(self, A, B, C, D):
        AB, BC, CD, AD = trapezium.sides(self, A, B, C, D)
        P = AB + AD + BC + CD
        return P
    def Sq(self, A, B, C, D):
        AB, BC, CD, AD = trapezium.sides(self, A, B, C, D)
        S = (AB + CD) / 2 * math.sqrt((math.pow(BC, 2) - (math.pow((AB - AD), 2) + math.pow(BC, 2) - math.pow(CD, 2)) / (2 *(AB - AD))))
        return S