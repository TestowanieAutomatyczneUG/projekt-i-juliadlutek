import unittest
from assertpy import *
from src.sample.student import Student


class StudentAssertpyTest(unittest.TestCase):
    def setUp(self):
        self.temp = Student("Jan", "Nowak", 10)

    def test_add_student_lecture(self):
        assert_that(self.temp.addStudentLecture("Matematyka"), "Dodano nowy przedmiot - Matematyka!")

    def test_add_student_repeat_lecture(self):
        self.temp.addStudentLecture("Matematyka")
        assert_that(
            self.temp.addStudentLecture) \
            .raises(Exception) \
            .when_called_with("Matematyka") \
            .contains("Podany przedmiot już istnieje!")

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

    def test_delete_student_grade_correct(self):
        self.temp.addStudentLecture("Matematyka")
        self.temp.addStudentGrade("Matematyka", 5)
        assert_that(self.temp.deleteStudentGrade("Matematyka", 5))\
            .is_equal_to("Usunięto ocenę 5 z przedmiotu Matematyka")

    def test_delete_student_grade_correct_contains(self):
        self.temp.addStudentLecture("Angielski")
        self.temp.addStudentGrade("Angielski", 2)
        assert_that(self.temp.deleteStudentGrade("Angielski", 2)).contains("2", "Angielski")

    def test_get_student_grades_empty(self):
        self.temp.addStudentLecture("Angielski")
        assert_that(self.temp.getStudentGrades("Angielski")).is_empty()

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



    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
