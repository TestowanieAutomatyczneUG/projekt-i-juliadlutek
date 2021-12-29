from itertools import count
import os
import csv


class Student:
    def __init__(self, name, surname, studentId, lectures='', comments=''):
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
        if lectures:
            for lecture in lectures:
                self.lectures[lecture] = lectures[lecture]
        if comments:
            for comment in comments:
                self.comments.append([next(self.__comment_id), comment])

    # Funkcja, która edytuje imię ucznia z testami w DocTest
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

    # Funkcja, która edytuje nazwisko ucznia z testami w DocTest
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
        elif not surname:
            raise ValueError("Nazwisko ucznia nie może być puste!")
        self.surname = surname
        return f"Zmieniono nazwisko ucznia na {surname}!"

    # Funkcja która dodaje nowy przemiot do ucznia.
    # Dodaje do słownika lectures klucz o podanej nazwie i jako wartość przypisuje mu pustą tablicę.
    def addStudentLecture(self, name):
        if type(name) != str or not name:
            raise ValueError("Nazwa przedmiotu musi być typu string!")
        elif name not in self.lectures:
            self.lectures[name] = []
            return f"Dodano nowy przedmiot - {name}!"
        raise Exception("Podany przedmiot już istnieje!")

    # Funkcja, która usuwa przedmiot ucznia.
    # Usuwa ze słownika lectures klucz o podanej nazwie.
    def deleteStudentLecture(self, name):
        if type(name) != str or not name:
            raise ValueError("Nazwa przedmiotu musi być typu string!")
        elif name not in self.lectures:
            raise Exception("Podany przedmiot nie istnieje!")
        del self.lectures[name]
        return f"Usunięto przedmiot - {name}!"

    # Funkcja, która zmienia nazwę podanego przedmiotu.
    def editStudentLectureName(self, name, newName):
        if type(name) != str or not name:
            raise ValueError("Nazwa przedmiotu musi być typu string!")
        elif type(newName) != str or not newName:
            raise ValueError("Nowa nazwa przedmiotu musi być typu string!")
        elif name not in self.lectures:
            raise Exception("Podany przedmiot nie istnieje!")
        self.lectures[newName] = self.lectures.pop(name)
        return f"Zmieniono nazwę przedmiotu {name} na {newName}."

    # Funkcja, która dodaję nową ocenę do podanego przemiotu
    # Do tablicy pod kluczem name dodaje nową ocenę.
    def addStudentGrade(self, name, grade):
        if type(grade) != int or grade < 1 or grade > 6:
            raise ValueError("Ocena musi być liczbą cakowitą z przedziału od 1 do 6")
        elif type(name) != str or not name:
            raise ValueError("Nazwa przedmiotu musi być typu string!")
        elif name not in self.lectures:
            raise Exception("Podany przedmiot nie istnieje!")
        self.lectures[name].append(grade)
        return f"Dodano ocenę {grade} do przedmiotu {name}"

    # Funkcja, która usuwa ocenę z podanego przedmiotu.
    # Znajduje pierwszy element o danej wartości i usuwa go.
    def deleteStudentGrade(self, name, grade):
        if type(grade) != int or grade < 1 or grade > 6:
            raise ValueError("Ocena musi być liczbą cakowitą z przedziału od 1 do 6")
        elif type(name) != str or not name:
            raise ValueError("Nazwa przedmiotu musi być typu string!")
        elif name not in self.lectures:
            raise Exception("Podany przedmiot nie istnieje!")
        elif grade not in self.lectures[name]:
            raise Exception("Podana ocena nie istnieje!")
        self.lectures[name].remove(grade)
        return f"Usunięto ocenę {grade} z przedmiotu {name}"

    # Funkcja, która zwraca oceny ucznia z podanego przedmiotu
    def getStudentGrades(self, name):
        if type(name) != str or not name:
            raise ValueError("Nazwa przedmiotu musi być typu string!")
        elif name not in self.lectures:
            raise Exception("Podany przedmiot nie istnieje!")
        return self.lectures[name]

    # Funkcja, która edytuje ocenę ucznia z podanego przemiotu
    # Znajduje pierwszą ocenę równą podanej, a następnie usuwa ją i dodaje do listy nową ocenę.
    def editStudentGrade(self, name, grade, newGrade):
        if type(grade) != int or grade < 1 or grade > 6:
            raise ValueError("Ocena musi być liczbą cakowitą z przedziału od 1 do 6")
        elif type(newGrade) != int or newGrade < 1 or newGrade > 6:
            raise ValueError("Nowa ocena musi być liczbą cakowitą z przedziału od 1 do 6")
        elif type(name) != str or not name:
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

    # Funkcja, która zwraca średnią ucznia z podanego przedmiotu.
    def getStudentAverage(self, name):
        grades = self.getStudentGrades(name)
        if not grades:
            raise Exception("Nie dodano żadnych ocen do tego przedmiotu.")
        amount = 0
        for grade in grades:
            amount += grade
        result = float("%.2f" % (amount / len(grades)))
        return result

    # Funkcja, która zwraca średnią ucznia ze wszystkich przedmiotów
    def getStudentFinalAverage(self):
        if not self.lectures:
            raise Exception("Nie dodano żadnych przedmiotów do tego ucznia.")
        amount = 0
        i = 0
        for lecture in self.lectures:
            if self.getStudentGrades(lecture):
                i += 1
                amount += self.getStudentAverage(lecture)
        result = float("%.2f" % (amount / i))
        return result

    # Funkcja, która dodaje uwagę do ucznia
    # Uwagi są przechowywane w formie tablic [id, wartość]
    def addStudentComment(self, content):
        if type(content) != str or not content:
            raise ValueError("Treść uwagi musi być typu string!")
        commentId = next(self.__comment_id)
        self.comments.append([commentId, content])
        return f"Dodano uwagę: {commentId}. {content}"

    # Funkcja, która zwraca wszystkie uwagi ucznia i ich id
    def getAllStudentComments(self):
        result = ""
        for comment in self.comments:
            result += str(comment[0]) + ". " + str(comment[1]) + "\n"
        return result

    # Funkcja, która zwraca uwagę po id
    def getStudentCommentById(self, commentId):
        if type(commentId) != int or commentId <= 0:
            raise ValueError("Id uwagi musi być dodatnią liczbą całkowitą!")
        for comment in self.comments:
            if comment[0] == commentId:
                return comment
        raise Exception("Uwaga o podanym id nie istnieje!")

    # Funkcja, która usuwa uwagę po id
    def deleteStudentCommentById(self, commentId):
        comment = self.getStudentCommentById(commentId)
        self.comments.remove(comment)
        return f"Usunięto uwagę \"{comment[1]}\""

    # Funkcja, która edytuje uwagę po id
    # Pobiera uwagę o danym id, a następnie usuwa ją i wstawia nową z tym samym id
    def editStudentCommentById(self, commentId, content):
        if type(content) != str or not content:
            raise ValueError("Treść uwagi musi być typu string!")
        comment = self.getStudentCommentById(commentId)
        self.comments.remove(comment)
        self.comments.append([commentId, content])
        return f"Zmieniono treść uwagi z \"{comment[1]}\" na \"{content}\""

    # Funkcja, która zapisuje przedmioty i oceny ucznia w formacie csv w podanym katalogu.
    # Plik z listą przedmiotów zawiera kolumny przedmiot, oceny, średnia z przedmiotu
    # Jeśli uczeń nie ma przypisanych ocen z jakiegoś przedmiotu, w kolumnach oceny i średnia zostaje wpisane "Brak"
    def writeToCsvStudentGrades(self, dirName):
        if type(dirName) != str or not dirName:
            raise ValueError("Nazwa katalogu musi być typu string!")
        header = ['Przedmiot', 'Oceny', 'Średnia']
        try:
            os.mkdir(f"./{dirName}")
        except OSError as e:
            pass
        with open(f"./{dirName}/student{self.id}grades.csv", 'w', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            if not self.lectures:
                raise Exception("Nie dodano żadnych przedmiotów do tego ucznia.")
            for lecture in self.lectures:
                if not self.getStudentGrades(lecture):
                    data = [lecture, "Brak", "Brak"]
                    writer.writerow(data)
                else:
                    data = [lecture, self.getStudentGrades(lecture), self.getStudentAverage(lecture)]
                    writer.writerow(data)
        return "Zapisano dane do pliku csv!"


if __name__ == "__main__":
    import doctest
