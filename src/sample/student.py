class Student:
    def __init__(self, name, surname):
        if type(name) != str or len(name) == 0:
            raise ValueError("Imię ucznia musi być typu string!")
        elif type(surname) != str or len(surname) == 0:
            raise ValueError("Nazwisko ucznia musi być typu string!")
        self.name = name
        self.surname = surname

    def editStudentName(self, name):
        """Changes the student's name
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



if __name__ == "__main__":
    import doctest
    doctest.testmod(extraglobs={'s': Student("Maria", "Kowalska")})
