import math
S = float(input("Введите сторону квадрата: "))


def sqare(S):
    return math.ceil(S*S)


print(f"Площадь квадрата: {sqare(S)}")
