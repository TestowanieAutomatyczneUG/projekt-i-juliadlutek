import unittest
from assertpy import *
from src.sample.studentList import StudentList

class StudentListAssertpyTest(unittest.TestCase):
    def setUp(self):
        self.temp = StudentList()

    def test_add_student(self):
        assert_that(self.temp.addStudent("Maria", "Kowalska"), "Dodano nowego ucznia: Maria Kowalska")


    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()