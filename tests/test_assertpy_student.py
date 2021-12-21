import unittest
from assertpy import *
from src.sample.student import Student
import re
import csv
from os.path import exists


class StudentAssertpyTest(unittest.TestCase):
    def setUp(self):
        self.temp = Student("Jan", "Nowak", 10)

    # Testy do dodawania przedmiotu do ucznia
    def test_add_student_lecture(self):
        assert_that(self.temp.addStudentLecture("Matematyka")).is_equal_to("Dodano nowy przedmiot - Matematyka!")

    # W przypadku, kiedy chcemy drugi raz dodać ten sam przedmiot
    def test_add_student_repeat_lecture(self):
        self.temp.addStudentLecture("Matematyka")
        assert_that(
            self.temp.addStudentLecture) \
            .raises(Exception) \
            .when_called_with("Matematyka") \
            .contains("Podany przedmiot już istnieje!")

    # W przypadku, kiedy dodamy niepoprawną nazwę przedmiotu
    def test_add_student_lecture_empty_str(self):
        assert_that(
            self.temp.addStudentLecture) \
            .raises(ValueError) \
            .when_called_with("") \
            .contains("Nazwa przedmiotu musi być typu string!")

    def test_add_student_lecture_int(self):
        assert_that(
            self.temp.addStudentLecture) \
            .raises(ValueError) \
            .when_called_with(12) \
            .contains("Nazwa przedmiotu musi być typu string!")

    def test_add_student_lecture_float(self):
        assert_that(
            self.temp.addStudentLecture) \
            .raises(ValueError) \
            .when_called_with(1.23) \
            .contains("Nazwa przedmiotu musi być typu string!")

    def test_add_student_lecture_empty_bool(self):
        assert_that(
            self.temp.addStudentLecture) \
            .raises(ValueError) \
            .when_called_with(True) \
            .contains("Nazwa przedmiotu musi być typu string!")

    def test_add_student_lecture_none(self):
        assert_that(
            self.temp.addStudentLecture) \
            .raises(ValueError) \
            .when_called_with(None) \
            .contains("Nazwa przedmiotu musi być typu string!")

    def test_add_student_lecture_empty_array(self):
        assert_that(
            self.temp.addStudentLecture) \
            .raises(ValueError) \
            .when_called_with(["Angielski"]) \
            .contains("Nazwa przedmiotu musi być typu string!")

    # Testy do usuwania oceny z przedmiotu
    def test_delete_student_grade_correct(self):
        self.temp.addStudentLecture("Matematyka")
        self.temp.addStudentGrade("Matematyka", 5)
        assert_that(self.temp.deleteStudentGrade("Matematyka", 5)) \
            .is_equal_to("Usunięto ocenę 5 z przedmiotu Matematyka")

    def test_delete_student_grade_correct_contains(self):
        self.temp.addStudentLecture("Angielski")
        self.temp.addStudentGrade("Angielski", 2)
        assert_that(self.temp.deleteStudentGrade("Angielski", 2)).contains("2", "Angielski")

    # W przypadku, kiedy podany przedmiot nie istnieje
    def test_delete_student_grade_not_existing_lecture(self):
        assert_that(
            self.temp.deleteStudentGrade) \
            .raises(Exception) \
            .when_called_with("Angielski", 5) \
            .contains("Podany przedmiot nie istnieje!")

    # W przypradku, kiedy podana ocena nie istnieje
    def test_delete_student_grade_not_existing_grade(self):
        self.temp.addStudentLecture("Angielski")
        self.temp.addStudentGrade("Angielski", 2)
        assert_that(
            self.temp.deleteStudentGrade) \
            .raises(Exception) \
            .when_called_with("Angielski", 5) \
            .contains("Podana ocena nie istnieje!")

    # W przypadku, kiedy podamy nieprawidłową nazwę przemiotu
    def test_delete_student_grade_name_empty(self):
        assert_that(
            self.temp.deleteStudentGrade) \
            .raises(ValueError) \
            .when_called_with("", 4) \
            .contains("Nazwa przedmiotu musi być typu string!")

    def test_delete_student_grade_name_int(self):
        assert_that(
            self.temp.deleteStudentGrade) \
            .raises(ValueError) \
            .when_called_with(12, 4) \
            .contains("Nazwa przedmiotu musi być typu string!")

    def test_delete_student_grade_name_float(self):
        assert_that(
            self.temp.deleteStudentGrade) \
            .raises(ValueError) \
            .when_called_with(1.2, 4) \
            .contains("Nazwa przedmiotu musi być typu string!")

    def test_delete_student_grade_name_bool(self):
        assert_that(
            self.temp.deleteStudentGrade) \
            .raises(ValueError) \
            .when_called_with(True, 4) \
            .contains("Nazwa przedmiotu musi być typu string!")

    def test_delete_student_grade_name_none(self):
        assert_that(
            self.temp.deleteStudentGrade) \
            .raises(ValueError) \
            .when_called_with(None, 4) \
            .contains("Nazwa przedmiotu musi być typu string!")

    def test_delete_student_grade_name_array(self):
        assert_that(
            self.temp.deleteStudentGrade) \
            .raises(ValueError) \
            .when_called_with([], 4) \
            .contains("Nazwa przedmiotu musi być typu string!")

    # W przypadku, kiedy podamy nieprawidłową ocenę
    def test_delete_student_grade_too_small(self):
        assert_that(
            self.temp.deleteStudentGrade) \
            .raises(ValueError) \
            .when_called_with("Angielski", -1) \
            .contains("Ocena musi być liczbą cakowitą z przedziału od 1 do 6")

    def test_delete_student_grade_too_big(self):
        assert_that(
            self.temp.deleteStudentGrade) \
            .raises(ValueError) \
            .when_called_with("Angielski", 7) \
            .contains("Ocena musi być liczbą cakowitą z przedziału od 1 do 6")

    def test_delete_student_grade_str(self):
        assert_that(
            self.temp.deleteStudentGrade) \
            .raises(ValueError) \
            .when_called_with("Angielski", "ala") \
            .contains("Ocena musi być liczbą cakowitą z przedziału od 1 do 6")

    def test_delete_student_grade_empty_str(self):
        assert_that(
            self.temp.deleteStudentGrade) \
            .raises(ValueError) \
            .when_called_with("Angielski", "") \
            .contains("Ocena musi być liczbą cakowitą z przedziału od 1 do 6")

    def test_delete_student_grade_float(self):
        assert_that(
            self.temp.deleteStudentGrade) \
            .raises(ValueError) \
            .when_called_with("Angielski", 3.5) \
            .contains("Ocena musi być liczbą cakowitą z przedziału od 1 do 6")

    def test_delete_student_grade_bool(self):
        assert_that(
            self.temp.deleteStudentGrade) \
            .raises(ValueError) \
            .when_called_with("Angielski", False) \
            .contains("Ocena musi być liczbą cakowitą z przedziału od 1 do 6")

    def test_delete_student_grade_none(self):
        assert_that(
            self.temp.deleteStudentGrade) \
            .raises(ValueError) \
            .when_called_with("Angielski", None) \
            .contains("Ocena musi być liczbą cakowitą z przedziału od 1 do 6")

    def test_delete_student_grade_array(self):
        assert_that(
            self.temp.deleteStudentGrade) \
            .raises(ValueError) \
            .when_called_with("Angielski", []) \
            .contains("Ocena musi być liczbą cakowitą z przedziału od 1 do 6")

    # Testy do pobierania ocen z danego przedmiotu
    # W przypadku kiedy nie ma żadnych przypisanych ocen
    def test_get_student_grades_empty(self):
        self.temp.addStudentLecture("Angielski")
        assert_that(self.temp.getStudentGrades("Angielski")).is_empty()

    # Różne asercje
    def test_get_student_grades_length(self):
        self.temp.addStudentLecture("Angielski")
        self.temp.addStudentGrade("Angielski", 2)
        self.temp.addStudentGrade("Angielski", 4)
        self.temp.addStudentGrade("Angielski", 5)
        assert_that(self.temp.getStudentGrades("Angielski")).is_length(3)

    def test_get_student_grades_contains(self):
        self.temp.addStudentLecture("Angielski")
        self.temp.addStudentGrade("Angielski", 2)
        self.temp.addStudentGrade("Angielski", 4)
        assert_that(self.temp.getStudentGrades("Angielski")).contains(2)

    def test_get_student_grades_not_contains(self):
        self.temp.addStudentLecture("Angielski")
        self.temp.addStudentGrade("Angielski", 2)
        self.temp.addStudentGrade("Angielski", 4)
        assert_that(self.temp.getStudentGrades("Angielski")).does_not_contain(3)

    def test_get_student_grades_equality(self):
        self.temp.addStudentLecture("Angielski")
        self.temp.addStudentGrade("Angielski", 2)
        self.temp.addStudentGrade("Angielski", 4)
        self.temp.addStudentGrade("Angielski", 5)
        assert_that(self.temp.getStudentGrades("Angielski")).is_equal_to([2, 4, 5])

    def test_get_student_grades_not_empty(self):
        self.temp.addStudentLecture("Angielski")
        self.temp.addStudentGrade("Angielski", 2)
        assert_that(self.temp.getStudentGrades("Angielski")).is_not_empty()

    # W przypadku, kiedy podany przemiot nie istnieje
    def test_get_student_grades_not_existing_lecture(self):
        assert_that(
            self.temp.getStudentGrades) \
            .raises(Exception) \
            .when_called_with("Matematyka") \
            .contains("Podany przedmiot nie istnieje!")

    # W przypadku, kiedy podamy nieprawidłową nazwę przedmiotu
    def test_get_student_grades_name_int(self):
        assert_that(
            self.temp.getStudentGrades) \
            .raises(ValueError) \
            .when_called_with(34) \
            .contains("Nazwa przedmiotu musi być typu string!")

    def test_get_student_grades_name_float(self):
        assert_that(
            self.temp.getStudentGrades) \
            .raises(ValueError) \
            .when_called_with(3.5) \
            .contains("Nazwa przedmiotu musi być typu string!")

    def test_get_student_grades_name_empty_str(self):
        assert_that(
            self.temp.getStudentGrades) \
            .raises(ValueError) \
            .when_called_with("") \
            .contains("Nazwa przedmiotu musi być typu string!")

    def test_get_student_grades_name_bool(self):
        assert_that(
            self.temp.getStudentGrades) \
            .raises(ValueError) \
            .when_called_with(True) \
            .contains("Nazwa przedmiotu musi być typu string!")

    def test_get_student_grades_name_none(self):
        assert_that(
            self.temp.getStudentGrades) \
            .raises(ValueError) \
            .when_called_with(None) \
            .contains("Nazwa przedmiotu musi być typu string!")

    def test_get_student_grades_name_array(self):
        assert_that(
            self.temp.getStudentGrades) \
            .raises(ValueError) \
            .when_called_with([]) \
            .contains("Nazwa przedmiotu musi być typu string!")

    # Własny matcher, sprawdzający, czy wynik jest liczbą dziesiętną z dwoma miejscami po przecinku
    def is_formatted_correctly(self):
        pattern = re.compile("^(0|[1-9]+[0-9]*)\.[0-9]{2}$")
        if not (bool(pattern.match(str(self.val)))):
            return self.error(
                f'Wynik {self.val} nie jest poprawnie sformatowany. Powinien byc liczbą dziesiętną z dwoma '
                f'miejscami po przecinku!')
        return self

    add_extension(is_formatted_correctly)

    # Drugi matcher, sprawdzający, czy wynik jest typu float
    def is_float(self):
        if type(self.val) != float:
            return self.error(
                f'{self.val} nie jest typu float.')
        return self

    add_extension(is_float)

    # Testy do średniej z danego przedmiotu
    # Z użyciem własnych matcherów
    def test_get_student_average_type(self):
        self.temp.addStudentLecture("Angielski")
        self.temp.addStudentGrade("Angielski", 2)
        self.temp.addStudentGrade("Angielski", 4)
        assert_that(self.temp.getStudentAverage("Angielski")).is_float()

    def test_get_student_average_format(self):
        self.temp.addStudentLecture("Angielski")
        self.temp.addStudentGrade("Angielski", 2)
        self.temp.addStudentGrade("Angielski", 4)
        self.temp.addStudentGrade("Angielski", 5)
        assert_that(self.temp.getStudentAverage("Angielski")).is_formatted_correctly()

    # Z użyciem różnych innych asercji
    def test_get_student_average_correct(self):
        self.temp.addStudentLecture("Angielski")
        self.temp.addStudentGrade("Angielski", 4)
        self.temp.addStudentGrade("Angielski", 5)
        self.temp.addStudentGrade("Angielski", 5)
        assert_that(self.temp.getStudentAverage("Angielski")).is_close_to(5, 0.4)

    def test_get_student_average_correct2(self):
        self.temp.addStudentLecture("Angielski")
        self.temp.addStudentGrade("Angielski", 4)
        self.temp.addStudentGrade("Angielski", 5)
        self.temp.addStudentGrade("Angielski", 5)
        assert_that(self.temp.getStudentAverage("Angielski")).is_between(4.5, 5)

    def test_get_student_average_correct3(self):
        self.temp.addStudentLecture("Angielski")
        self.temp.addStudentGrade("Angielski", 4)
        self.temp.addStudentGrade("Angielski", 5)
        self.temp.addStudentGrade("Angielski", 5)
        assert_that(self.temp.getStudentAverage("Angielski")).is_less_than(4.7)

    # W przypadku, kiedy nie ma żadnych ocen dodanych do przedmiotu
    def test_get_student_average_empty_grades(self):
        self.temp.addStudentLecture("Angielski")
        assert_that(
            self.temp.getStudentAverage) \
            .raises(Exception) \
            .when_called_with("Angielski") \
            .contains("Nie dodano żadnych ocen do tego przedmiotu.")

    # Testy do dodawania uwagi do ucznia
    def test_add_student_comment_correct(self):
        assert_that(self.temp.addStudentComment("Spóźnienie na lekcję.")) \
            .is_equal_to("Dodano uwagę: 1. Spóźnienie na lekcję.")

    # W przypadku kiedy podamy nieprawidłową treść
    def test_add_student_comment_content_empty(self):
        assert_that(
            self.temp.addStudentComment) \
            .raises(ValueError) \
            .when_called_with("") \
            .contains("Treść uwagi musi być typu string!")

    def test_add_student_comment_content_int(self):
        assert_that(
            self.temp.addStudentComment) \
            .raises(ValueError) \
            .when_called_with(2) \
            .contains("Treść uwagi musi być typu string!")

    def test_add_student_comment_content_float(self):
        assert_that(
            self.temp.addStudentComment) \
            .raises(ValueError) \
            .when_called_with(2.3) \
            .contains("Treść uwagi musi być typu string!")

    def test_add_student_comment_content_none(self):
        assert_that(
            self.temp.addStudentComment) \
            .raises(ValueError) \
            .when_called_with(None) \
            .contains("Treść uwagi musi być typu string!")

    def test_add_student_comment_content_true(self):
        assert_that(
            self.temp.addStudentComment) \
            .raises(ValueError) \
            .when_called_with(True) \
            .contains("Treść uwagi musi być typu string!")

    def test_add_student_comment_content_array(self):
        assert_that(
            self.temp.addStudentComment) \
            .raises(ValueError) \
            .when_called_with([]) \
            .contains("Treść uwagi musi być typu string!")

    # Testy do pobierania wszytskich uwag
    def test_get_all_student_comments(self):
        self.temp.addStudentComment("Spóżnienie na lekcję.")
        self.temp.addStudentComment("Brak pracy domowej.")
        assert_that(self.temp.getAllStudentComments()).contains("Spóżnienie na lekcję.", "Brak pracy domowej.")

    # W przypadku, kiedy nie ma żadnych uwag
    def test_get_all_student_comments_empty(self):
        assert_that(self.temp.getAllStudentComments()).is_empty()

    # Testy do pobierania uwag po id
    def test_get_student_comment_by_id_correct(self):
        self.temp.addStudentComment("Spóżnienie na lekcję.")
        assert_that(self.temp.getStudentCommentById(1)).contains(1, "Spóżnienie na lekcję.")

    # W przypadku, kiedy uwaga o danym id nie istnieje
    def test_get_student_comment_by_id_not_existing(self):
        self.temp.addStudentComment("Spóżnienie na lekcję.")
        assert_that(
            self.temp.getStudentCommentById) \
            .raises(Exception) \
            .when_called_with(2) \
            .contains("Uwaga o podanym id nie istnieje!")

    # W przypadku, kiedy nie dodano żadnych uwag.
    def test_get_student_comment_by_id_empty_comments(self):
        assert_that(
            self.temp.getStudentCommentById) \
            .raises(Exception) \
            .when_called_with(1) \
            .contains("Uwaga o podanym id nie istnieje!")

    # W przypadku, kiedy podamy nieprawidłowe id
    def test_get_student_comment_by_id_empty_str(self):
        assert_that(
            self.temp.getStudentCommentById) \
            .raises(ValueError) \
            .when_called_with("") \
            .contains("Id uwagi musi być dodatnią liczbą całkowitą!")

    def test_get_student_comment_by_id_negative(self):
        assert_that(
            self.temp.getStudentCommentById) \
            .raises(ValueError) \
            .when_called_with(-3) \
            .contains("Id uwagi musi być dodatnią liczbą całkowitą!")

    def test_get_student_comment_by_id_string(self):
        assert_that(
            self.temp.getStudentCommentById) \
            .raises(ValueError) \
            .when_called_with("ala") \
            .contains("Id uwagi musi być dodatnią liczbą całkowitą!")

    def test_get_student_comment_by_id_float(self):
        assert_that(
            self.temp.getStudentCommentById) \
            .raises(ValueError) \
            .when_called_with(0.1) \
            .contains("Id uwagi musi być dodatnią liczbą całkowitą!")

    def test_get_student_comment_by_id_bool(self):
        assert_that(
            self.temp.getStudentCommentById) \
            .raises(ValueError) \
            .when_called_with(True) \
            .contains("Id uwagi musi być dodatnią liczbą całkowitą!")

    def test_get_student_comment_by_id_none(self):
        assert_that(
            self.temp.getStudentCommentById) \
            .raises(ValueError) \
            .when_called_with(None) \
            .contains("Id uwagi musi być dodatnią liczbą całkowitą!")

    def test_get_student_comment_by_id_array(self):
        assert_that(
            self.temp.getStudentCommentById) \
            .raises(ValueError) \
            .when_called_with([]) \
            .contains("Id uwagi musi być dodatnią liczbą całkowitą!")

    # Testy do funkcji zapisującej oceny ucznia do csv
    # Sprawdzamy, czy zapis się powiódł
    def test_write_to_csv_grades_correct_ouput(self):
        self.temp.addStudentLecture("Angielski")
        self.temp.addStudentGrade("Angielski", 2)
        self.temp.addStudentGrade("Angielski", 4)
        self.temp.addStudentGrade("Angielski", 5)
        self.temp.addStudentLecture("Matematyka")
        self.temp.addStudentGrade("Matematyka", 5)
        self.temp.addStudentGrade("Matematyka", 5)
        self.temp.addStudentGrade("Matematyka", 3)
        assert_that(self.temp.writeToCsvStudentGrades('testCsv')).is_equal_to("Zapisano dane do pliku csv!")

    # Otwieramy plik i sprawdzamy czy nagłówek jest poprawny
    def test_write_to_csv_grades_correct_header(self):
        if exists('./testCsv/studentList.csv'):
            csvFile = open('./testCsv/student10grades.csv')
            csvreader = csv.reader(csvFile)
            header = next(csvreader)
            assert_that(header).contains("Przedmiot", "Oceny", "Średnia")
        pass

    # Otwieramy plik i sprawdzamy czy wartości są poprawne
    def test_write_to_csv_grades_records(self):
        if exists('./testCsv/studentList.csv'):
            csvFile = open('./testCsv/student10grades.csv')
            csvreader = csv.reader(csvFile)
            rows = []
            for row in csvreader:
                for el in row:
                    rows.append(el)
            assert_that(rows).contains('Angielski', '[2, 4, 5]', '3.67', 'Matematyka', '[5, 5, 3]', '4.33')
        pass

    # Sprawdzamy przypadek, kiedy nie ma żadnych przedmiotów
    def test_write_to_csv_grades_with_any_lectures(self):
        assert_that(
            self.temp.writeToCsvStudentGrades) \
            .raises(Exception) \
            .when_called_with('testCsv') \
            .contains("Nie dodano żadnych przedmiotów do tego ucznia.")

    # Sprawdzamy przypadek, kiedy do przedmiotu nie ma dodanych ocen
    def test_write_to_csv_grades_with_any_grades(self):
        self.temp.addStudentLecture("Angielski")
        self.temp.addStudentGrade("Angielski", 2)
        self.temp.addStudentGrade("Angielski", 4)
        self.temp.addStudentGrade("Angielski", 5)
        self.temp.addStudentLecture("Matematyka")
        self.temp.writeToCsvStudentGrades('testCsv')
        csvFile = open('testCsv/student10grades.csv')
        csvreader = csv.reader(csvFile)
        rows = []
        for row in csvreader:
            for el in row:
                rows.append(el)
        assert_that(rows).contains('Angielski', '[2, 4, 5]', '3.67', 'Matematyka', 'Brak', 'Brak')

    # Przypadki, kiedy podamy nieprawidłową nazwę katalogu
    def test_write_to_csv_grades_dir_empty_str(self):
        assert_that(
            self.temp.writeToCsvStudentGrades) \
            .raises(ValueError) \
            .when_called_with("") \
            .contains("Nazwa katalogu musi być typu string!")

    def test_write_to_csv_grades_dir_int(self):
        assert_that(
            self.temp.writeToCsvStudentGrades) \
            .raises(ValueError) \
            .when_called_with(3) \
            .contains("Nazwa katalogu musi być typu string!")

    def test_write_to_csv_grades_dir_float(self):
        assert_that(
            self.temp.writeToCsvStudentGrades) \
            .raises(ValueError) \
            .when_called_with(-1.4) \
            .contains("Nazwa katalogu musi być typu string!")

    def test_write_to_csv_grades_dir_bool(self):
        assert_that(
            self.temp.writeToCsvStudentGrades) \
            .raises(ValueError) \
            .when_called_with(False) \
            .contains("Nazwa katalogu musi być typu string!")

    def test_write_to_csv_grades_dir_none(self):
        assert_that(
            self.temp.writeToCsvStudentGrades) \
            .raises(ValueError) \
            .when_called_with(None) \
            .contains("Nazwa katalogu musi być typu string!")

    def test_write_to_csv_grades_dir_array(self):
        assert_that(
            self.temp.writeToCsvStudentGrades) \
            .raises(ValueError) \
            .when_called_with([]) \
            .contains("Nazwa katalogu musi być typu string!")

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
