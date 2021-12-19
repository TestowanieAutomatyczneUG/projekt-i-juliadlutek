from itertools import count

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
        self.__comment_id = count(1, 1)

    def editStudentName(self, name):
        """Zmienia imię ucznia
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
        """Zmienia nazwisko ucznia
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

    def editStudentLectureName(self, name, newName):
        if type(name) != str or name == '':
            raise ValueError("Nazwa przedmiotu musi być typu string!")
        if type(newName) != str or newName == '':
            raise ValueError("Nowa nazwa przedmiotu musi być typu string!")
        elif name not in self.lectures:
            raise Exception("Podany przedmiot nie istnieje!")
        self.lectures[newName] = self.lectures.pop(name)
        return f"Zmieniono nazwę przedmiotu {name} na {newName}."

    def addStudentGrade(self, name, grade):
        if type(grade) != int or grade < 1 or grade > 6:
            raise ValueError("Ocena musi być liczbą cakowitą z przedziau od 1 do 6")
        elif type(name) != str or name == "":
            raise ValueError("Nazwa przedmiotu musi być typu string!")
        elif name not in self.lectures:
            raise Exception("Podany przedmiot nie istnieje!")
        self.lectures[name].append(grade)
        return f"Dodano ocenę {grade} do przedmiotu {name}"

    def deleteStudentGrade(self, name, grade):
        if type(grade) != int or grade < 1 or grade > 6:
            raise ValueError("Ocena musi być liczbą cakowitą z przedziau od 1 do 6")
        elif type(name) != str or name == "":
            raise ValueError("Nazwa przedmiotu musi być typu string!")
        elif name not in self.lectures:
            raise Exception("Podany przedmiot nie istnieje!")
        elif grade not in self.lectures[name]:
            raise Exception("Podana ocena nie istnieje!")
        self.lectures[name].remove(grade)
        return f"Usunięto ocenę {grade} z przedmiotu {name}"

    def getStudentGrades(self, name):
        if type(name) != str or name == "":
            raise ValueError("Nazwa przedmiotu musi być typu string!")
        elif name not in self.lectures:
            raise Exception("Podany przedmiot nie istnieje!")
        return self.lectures[name]

    def editStudentGrade(self, name, grade, newGrade):
        if type(grade) != int or grade < 1 or grade > 6:
            raise ValueError("Ocena musi być liczbą cakowitą z przedziau od 1 do 6")
        if type(newGrade) != int or newGrade < 1 or newGrade > 6:
            raise ValueError("Nowa ocena musi być liczbą cakowitą z przedziau od 1 do 6")
        elif type(name) != str or name == "":
            raise ValueError("Nazwa przedmiotu musi być typu string!")
        elif name not in self.lectures:
            raise Exception("Podany przedmiot nie istnieje!")
        elif grade not in self.lectures[name]:
            raise Exception("Podana ocena nie istnieje!")
        elif grade == newGrade:
            raise Exception("Nowa ocena musi różnić się od starej!")
        self.lectures[name].remove(grade)
        self.lectures[name].append(newGrade)
        return f"Zmieniono ocenę {grade} na ocenę {newGrade}"

    def getStudentAverage(self, name):
        grades = self.getStudentGrades(name)
        if not grades:
            raise Exception("Nie dodano żadnych ocen do tego przedmiotu.")
        amount = 0
        for grade in grades:
            amount += grade
        result = amount / len(grades)
        return float("%.2f" % result)

    def getStudentFinalAverage(self):
        if not self.lectures:
            raise Exception("Nie dodano żadnych przedmiotów do tego ucznia.")
        amount = 0
        i = 0
        for lecture in self.lectures:
            if self.getStudentGrades(lecture):
                i += 1
                amount += self.getStudentAverage(lecture)
        result = amount / i
        return float("%.2f" % result)

    def addStudentComment(self, content):
        if type(content) != str or content == "":
            raise ValueError("Treść uwagi musi być typu string!")
        commentId = next(self.__comment_id)
        self.comments.append([commentId, content])
        return f"Dodano uwagę: {commentId}. {content}"

    def getAllStudentComments(self):
        result = ""
        for comment in self.comments:
            result += str(comment[0]) + ". " + str(comment[1]) + "\n"
        return result

    def getStudentCommentById(self, commentId):
        if type(commentId) != int or commentId <= 0:
            raise ValueError("Id uwagi musi być dodatnią liczbą całkowitą!")
        for comment in self.comments:
            if comment[0] == commentId:
                return comment
        raise Exception("Uwaga o podanym id nie istnieje!")


if __name__ == "__main__":
    import doctest
