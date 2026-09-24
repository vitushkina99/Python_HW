def is_year_leap(year):
    return "True" if year % 4 == 0 else "False"


yep = int(input("Введите год: "))
res = is_year_leap(yep)
print(f"Год {yep}: {res}")
