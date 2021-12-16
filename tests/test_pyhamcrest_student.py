import unittest
from hamcrest import *
from src.sample.student import Student


class StudentPyHamcrestTest(unittest.TestCase):
    def setUp(self):
        self.temp = Student("Jan", "Nowak", 10)
        self.temp.addStudentLecture("Matematyka")

    def test_delete_student_lecture(self):
        assert_that(self.temp.deleteStudentLecture("Matematyka"), equal_to("Usunięto przedmiot - Matematyka!"))

    def test_delete_not_existing_student_lecture(self):
        assert_that(calling(self.temp.deleteStudentLecture).with_args("Angielski"), raises(Exception))

    def test_delete_student_lecture_empty_str(self):
        assert_that(calling(self.temp.deleteStudentLecture).with_args(""), raises(ValueError))

    def test_delete_student_lecture_int(self):
        assert_that(calling(self.temp.deleteStudentLecture).with_args(123), raises(ValueError))

    def test_delete_student_lecture_float(self):
        assert_that(calling(self.temp.deleteStudentLecture).with_args(0.1), raises(ValueError))

    def test_delete_student_lecture_empty_bool(self):
        assert_that(calling(self.temp.deleteStudentLecture).with_args(False), raises(ValueError))

    def test_delete_student_lecture_none(self):
        assert_that(calling(self.temp.deleteStudentLecture).with_args(None), raises(ValueError))

    def test_delete_student_lecture_empty_array(self):
        assert_that(calling(self.temp.deleteStudentLecture).with_args([]), raises(ValueError))

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()