import unittest
from assertpy import *
from src.sample.studentList import StudentList
from src.sample.student import Student


class StudentListAssertpyTest(unittest.TestCase):
    def setUp(self):
        self.temp = StudentList()

    def test_add_student(self):
        assert_that(self.temp.addStudent("Maria", "Kowalska"), "Dodano nowego ucznia: Maria Kowalska")

    def test_add_student_number_name(self):
        assert_that(
            self.temp.addStudent) \
            .raises(ValueError) \
            .when_called_with(65, "Kowalska") \
            .contains("Student's name must be string!")

    def test_add_student_number_surname(self):
        assert_that(
            self.temp.addStudent) \
            .raises(ValueError) \
            .when_called_with("Maria", 0) \
            .contains("Student's surname must be string!")

    def test_add_student_empty_string_name(self):
        assert_that(
            self.temp.addStudent) \
            .raises(ValueError) \
            .when_called_with("", "Kowalska") \
            .contains("Student's name must be string!")

    def test_add_student_empty_string_surname(self):
        assert_that(
            self.temp.addStudent) \
            .raises(ValueError) \
            .when_called_with("Maria", "") \
            .contains("Student's surname must be string!")

    def test_add_student_array_name(self):
        assert_that(
            self.temp.addStudent) \
            .raises(ValueError) \
            .when_called_with(["Maria"], "Kowalska") \
            .contains("Student's name must be string!")

    def test_add_student_array_surname(self):
        assert_that(
            self.temp.addStudent) \
            .raises(ValueError) \
            .when_called_with("Maria", ["Kowalska"]) \
            .contains("Student's surname must be string!")

    def test_add_student_boolean_name(self):
        assert_that(
            self.temp.addStudent) \
            .raises(ValueError) \
            .when_called_with(True, "Kowalska") \
            .contains("Student's name must be string!")

    def test_add_student_boolean_surname(self):
        assert_that(
            self.temp.addStudent) \
            .raises(ValueError) \
            .when_called_with("Maria", False) \
            .contains("Student's surname must be string!")

    def test_add_student_none_name(self):
        assert_that(
            self.temp.addStudent) \
            .raises(ValueError) \
            .when_called_with(None, "Kowalska") \
            .contains("Student's name must be string!")

    def test_add_student_none_surname(self):
        assert_that(
            self.temp.addStudent) \
            .raises(ValueError) \
            .when_called_with("Maria", None) \
            .contains("Student's surname must be string!")

    def test_add_student_float_name(self):
        assert_that(
            self.temp.addStudent) \
            .raises(ValueError) \
            .when_called_with(65.267, "Kowalska") \
            .contains("Student's name must be string!")

    def test_add_student_float_surname(self):
        assert_that(
            self.temp.addStudent) \
            .raises(ValueError) \
            .when_called_with("Maria", 0.1) \
            .contains("Student's surname must be string!")

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
