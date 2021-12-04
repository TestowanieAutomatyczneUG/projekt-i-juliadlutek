class Student:
    def __init__(self, name, surname):
        if type(name) != str or len(name) == 0:
            raise ValueError("Student's name must be string!")
        elif type(surname) != str or len(surname) == 0:
            raise ValueError("Student's surname must be string!")
        self.name = name
        self.surname = surname
