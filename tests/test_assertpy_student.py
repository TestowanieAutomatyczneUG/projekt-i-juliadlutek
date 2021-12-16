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


    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
