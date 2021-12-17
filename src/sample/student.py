class Student:
    def __init__(self, name, surname, studentId):
        if type(name) != str or len(name) == 0:
            raise ValueError("Imię ucznia musi być typu string!")
        elif type(surname) != str or len(surname) == 0:
            raise ValueError("Nazwisko ucznia musi być typu string!")
        self.id = studentId
        self.name = name
        self.surname = surname
        self.lectures = {}
        self.comments = []

    def editStudentName(self, name):
        """Changes the student's
        >>> s = Student("Maria", "Kowalska", 10)
        >>> s.editStudentName("Marysia")
        'Zmieniono imię ucznia na Marysia!'
        >>> s.editStudentName("")
        Traceback (most recent call last):
          ...
        ValueError: Imię ucznia nie może być puste!
        >>> s.editStudentName(10)
        Traceback (most recent call last):
          ...
        ValueError: Imię ucznia musi być typu string!
        >>> s.editStudentName(True)
        Traceback (most recent call last):
          ...
        ValueError: Imię ucznia musi być typu string!
        >>> s.editStudentName(None)
        Traceback (most recent call last):
          ...
        ValueError: Imię ucznia musi być typu string!
        >>> s.editStudentName(["Ala"])
        Traceback (most recent call last):
          ...
        ValueError: Imię ucznia musi być typu string!
        >>> s.editStudentName(-2.3)
        Traceback (most recent call last):
          ...
        ValueError: Imię ucznia musi być typu string!
        """
        if type(name) != str:
            raise ValueError("Imię ucznia musi być typu string!")
        elif len(name) == 0:
            raise ValueError("Imię ucznia nie może być puste!")
        self.name = name
        return f"Zmieniono imię ucznia na {name}!"

    def editStudentSurname(self, surname):
        """Changes the student's surname
        >>> s = Student("Maria", "Kowalska", 10)
        >>> s.editStudentSurname("Nowak")
        'Zmieniono nazwisko ucznia na Nowak!'
        >>> s.editStudentSurname("")
        Traceback (most recent call last):
          ...
        ValueError: Nazwisko ucznia nie może być puste!
        >>> s.editStudentSurname(10)
        Traceback (most recent call last):
          ...
        ValueError: Nazwisko ucznia musi być typu string!
        >>> s.editStudentSurname(True)
        Traceback (most recent call last):
          ...
        ValueError: Nazwisko ucznia musi być typu string!
        >>> s.editStudentSurname(None)
        Traceback (most recent call last):
          ...
        ValueError: Nazwisko ucznia musi być typu string!
        >>> s.editStudentSurname(["Ala"])
        Traceback (most recent call last):
          ...
        ValueError: Nazwisko ucznia musi być typu string!
        >>> s.editStudentSurname(-2.3)
        Traceback (most recent call last):
          ...
        ValueError: Nazwisko ucznia musi być typu string!
        """

        if type(surname) != str:
            raise ValueError("Nazwisko ucznia musi być typu string!")
        elif len(surname) == 0:
            raise ValueError("Nazwisko ucznia nie może być puste!")
        self.surname = surname
        return f"Zmieniono nazwisko ucznia na {surname}!"

    def addStudentLecture(self, name):
        if type(name) != str or name == '':
            raise ValueError("Nazwa przedmiotu musi być typu string!")
        elif name not in self.lectures:
            self.lectures[name] = []
            return f"Dodano nowy przedmiot - {name}!"
        raise Exception("Podany przedmiot już istnieje!")

    def deleteStudentLecture(self, name):
        if type(name) != str or name == '':
            raise ValueError("Nazwa przedmiotu musi być typu string!")
        elif name not in self.lectures:
            raise Exception("Podany przedmiot nie istnieje!")
        del self.lectures[name]
        return f"Usunięto przedmiot - {name}!"

    def addStudentGrade(self, name, grade):
        if type(grade) != int or grade < 1 or grade > 6:
            raise ValueError("Ocena musi być liczbą cakowitą z przedziau od 1 do 6")
        elif type(name) != str or name == "":
            raise ValueError("Nazwa przedmiotu musi być typu string!")
        elif name not in self.lectures:
            raise Exception("Podany przedmiot nie istnieje!")
        self.lectures[name].append(grade)
        return f"Dodano ocenę {grade} do przedmiotu {name}"


if __name__ == "__main__":
    import doctest
