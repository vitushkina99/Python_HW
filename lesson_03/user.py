class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def Print_Name(self):
        return self.first_name

    def Print_First_Name(self):
        return self.last_name

    def Print_First_Last_Name(self):
        return f"{self.first_name} {self.last_name}"
