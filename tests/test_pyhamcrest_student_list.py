import unittest
from hamcrest import *
from src.sample.studentList import StudentList
from src.sample.student import Student


class StudentListPyHamcrestTest(unittest.TestCase):
    def setUp(self):
        self.temp = StudentList()

    def test_get_empty_student_list(self):
        assert_that(self.temp.getAllStudents(), equal_to(''))

    def test_get_student_list(self):
        self.temp.addStudent("Maria", "Kowalska")
        self.temp.addStudent("Jan", "Nowak")
        self.temp.addStudent("Anna", "Nowak")
        assert_that(
            self.temp.getAllStudents(),
            equal_to_ignoring_whitespace("1. Maria Kowalska 2. Jan Nowak 3. Anna Nowak"))

    def test_get_student_by_number(self):
        self.temp.addStudent("Maria", "Kowalska")
        self.temp.addStudent("Jan", "Nowak")
        assert_that(
            self.temp.getStudentByNumber(1),
            instance_of(Student))

    def test_get_student_by_number_correct_name(self):
        self.temp.addStudent("Maria", "Kowalska")
        self.temp.addStudent("Jan", "Nowak")
        assert_that(
            self.temp.getStudentByNumber(1).name,
            equal_to("Maria"))

    def test_get_not_existing_student_by_number(self):
        self.temp.addStudent("Maria", "Kowalska")
        assert_that(calling(self.temp.getStudentByNumber).with_args(5), raises(Exception))

    def test_get_student_by_number_with_str(self):
        assert_that(calling(self.temp.getStudentByNumber).with_args("maria"), raises(ValueError))

    def test_get_student_by_number_with_bool(self):
        assert_that(calling(self.temp.getStudentByNumber).with_args(True), raises(ValueError))

    def test_get_student_by_number_with_none(self):
        assert_that(calling(self.temp.getStudentByNumber).with_args(None), raises(ValueError))

    def test_get_student_by_number_with_array(self):
        assert_that(calling(self.temp.getStudentByNumber).with_args([1]), raises(ValueError))

    def test_get_student_by_number_with_float(self):
        assert_that(calling(self.temp.getStudentByNumber).with_args(2.34), raises(ValueError))

    def test_get_student_by_negative_number(self):
        assert_that(calling(self.temp.getStudentByNumber).with_args(-2), raises(ValueError))




    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()