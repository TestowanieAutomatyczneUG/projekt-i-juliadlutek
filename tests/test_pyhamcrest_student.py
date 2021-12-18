import unittest
from hamcrest import *
from src.sample.student import Student
from hamcrest.core.base_matcher import BaseMatcher


class IsFloat(BaseMatcher):
    def _matches(self, item):
        if type(item) != float:
            return False
        return item

    def describe_to(self, description):
        description.append_text("Result is float")


def is_float():
    return IsFloat()


class StudentPyHamcrestTest(unittest.TestCase):
    def setUp(self):
        self.temp = Student("Jan", "Nowak", 10)

    def test_delete_student_lecture(self):
        self.temp.addStudentLecture("Matematyka")
        assert_that(self.temp.deleteStudentLecture("Matematyka"), equal_to("Usunięto przedmiot - Matematyka!"))

    def test_delete_not_existing_student_lecture(self):
        self.temp.addStudentLecture("Matematyka")
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

    def test_get_student_final_average_correct(self):
        self.temp.addStudentLecture("Matematyka")
        self.temp.addStudentLecture("Angielski")
        self.temp.addStudentGrade("Angielski", 4)
        self.temp.addStudentGrade("Angielski", 3)
        self.temp.addStudentGrade("Matematyka", 5)
        self.temp.addStudentGrade("Matematyka", 4)
        self.temp.addStudentGrade("Matematyka", 4)
        assert_that(self.temp.getStudentFinalAverage(), close_to(4, 0.1))

    def test_get_student_final_average_type(self):
        self.temp.addStudentLecture("Matematyka")
        self.temp.addStudentLecture("Angielski")
        self.temp.addStudentGrade("Angielski", 4)
        self.temp.addStudentGrade("Angielski", 3)
        self.temp.addStudentGrade("Matematyka", 5)
        self.temp.addStudentGrade("Matematyka", 4)
        assert_that(self.temp.getStudentFinalAverage(), is_float())

    def test_get_student_final_average_any_lectures(self):
        assert_that(calling(self.temp.getStudentFinalAverage).with_args(), raises(Exception))

    def test_get_student_final_average_lecture_without_grades(self):
        self.temp.addStudentLecture("Matematyka")
        self.temp.addStudentLecture("Angielski")
        self.temp.addStudentGrade("Angielski", 4)
        self.temp.addStudentGrade("Angielski", 3)
        assert_that(self.temp.getStudentFinalAverage(), greater_than(3))

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
