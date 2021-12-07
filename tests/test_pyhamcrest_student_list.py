import unittest
from hamcrest import *
from src.sample.studentList import StudentList


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

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()