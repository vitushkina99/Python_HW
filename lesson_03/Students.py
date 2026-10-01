class Student:
    def __init__(self, name, sec_name, age, course):
        self.name = name
        self.sec_name = sec_name
        self.age = age
        self.course = course

    def __str__(self):
        return f"{self.name} {self.sec_name}, {self.age} лет, курс: {self.course}"
    