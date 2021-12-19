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

    def test_edit_student_lecture_name_correct(self):
        self.temp.addStudentLecture("matematyka")
        assert_that(self.temp.editStudentLectureName("matematyka", "Matematyka"),
                    equal_to("Zmieniono nazwę przedmiotu matematyka na Matematyka."))

    def test_edit_student_lecture_name_correct_grades(self):
        self.temp.addStudentLecture("matematyka")
        self.temp.addStudentGrade("matematyka", 5)
        self.temp.addStudentGrade("matematyka", 4)
        self.temp.editStudentLectureName("matematyka", "Matematyka")
        assert_that(self.temp.getStudentGrades("Matematyka"),
                    contains_inanyorder(4, 5))

    def test_edit_student_lecture_not_existing(self):
        assert_that(calling(self.temp.editStudentLectureName).with_args("matematyka", "Matematyka"), raises(Exception))

    def test_edit_student_lecture_name_empty_str(self):
        self.temp.addStudentLecture("matematyka")
        assert_that(calling(self.temp.editStudentLectureName).with_args("", "Matematyka"), raises(ValueError))

    def test_edit_student_lecture_name_int(self):
        self.temp.addStudentLecture("matematyka")
        assert_that(calling(self.temp.editStudentLectureName).with_args(-2, "Matematyka"), raises(ValueError))

    def test_edit_student_lecture_name_float(self):
        self.temp.addStudentLecture("matematyka")
        assert_that(calling(self.temp.editStudentLectureName).with_args(1.3, "Matematyka"), raises(ValueError))

    def test_edit_student_lecture_name_array(self):
        self.temp.addStudentLecture("matematyka")
        assert_that(calling(self.temp.editStudentLectureName).with_args([], "Matematyka"), raises(ValueError))

    def test_edit_student_lecture_name_bool(self):
        self.temp.addStudentLecture("matematyka")
        assert_that(calling(self.temp.editStudentLectureName).with_args(True, "Matematyka"), raises(ValueError))

    def test_edit_student_lecture_name_none(self):
        self.temp.addStudentLecture("matematyka")
        assert_that(calling(self.temp.editStudentLectureName).with_args(None, "Matematyka"), raises(ValueError))

    def test_edit_student_lecture_new_name_empty_str(self):
        self.temp.addStudentLecture("matematyka")
        assert_that(calling(self.temp.editStudentLectureName).with_args("matematyka", ""), raises(ValueError))

    def test_edit_student_lecture_new_name_int(self):
        self.temp.addStudentLecture("matematyka")
        assert_that(calling(self.temp.editStudentLectureName).with_args("matematyka", 12), raises(ValueError))

    def test_edit_student_lecture_new_name_float(self):
        self.temp.addStudentLecture("matematyka")
        assert_that(calling(self.temp.editStudentLectureName).with_args("matematyka", 12.2), raises(ValueError))

    def test_edit_student_lecture_new_name_array(self):
        self.temp.addStudentLecture("matematyka")
        assert_that(calling(self.temp.editStudentLectureName).with_args("matematyka", []), raises(ValueError))

    def test_edit_student_lecture_new_name_bool(self):
        self.temp.addStudentLecture("matematyka")
        assert_that(calling(self.temp.editStudentLectureName).with_args("matematyka", False), raises(ValueError))

    def test_edit_student_lecture_new_name_none(self):
        self.temp.addStudentLecture("matematyka")
        assert_that(calling(self.temp.editStudentLectureName).with_args("matematyka", None), raises(ValueError))

    def test_edit_student_grade_correct_output(self):
        self.temp.addStudentLecture("Matematyka")
        self.temp.addStudentGrade("Matematyka", 5)
        assert_that(self.temp.editStudentGrade("Matematyka", 5, 4), equal_to("Zmieniono ocenę 5 na ocenę 4"))

    def test_edit_student_grade_correct(self):
        self.temp.addStudentLecture("Matematyka")
        self.temp.addStudentGrade("Matematyka", 5)
        self.temp.addStudentGrade("Matematyka", 4)
        self.temp.addStudentGrade("Matematyka", 3)
        self.temp.editStudentGrade("Matematyka", 3, 5)
        assert_that(self.temp.getStudentGrades("Matematyka"), is_not(contains_exactly(3)))

    def test_only_one_student_grade(self):
        self.temp.addStudentLecture("Matematyka")
        self.temp.addStudentGrade("Matematyka", 5)
        self.temp.addStudentGrade("Matematyka", 5)
        self.temp.addStudentGrade("Matematyka", 5)
        self.temp.editStudentGrade("Matematyka", 5, 4)
        assert_that(self.temp.getStudentGrades("Matematyka"), contains_inanyorder(5, 5, 4))

    def test_delete_student_comment_correct(self):
        self.temp.addStudentComment("Spóżnienie na lekcję.")
        assert_that(self.temp.deleteStudentCommentById(1), equal_to("Usunięto uwagę \"Spóżnienie na lekcję.\""))

    def test_delete_student_comment_not_existing(self):
        assert_that(calling(self.temp.deleteStudentCommentById).with_args(3), raises(Exception))

    def test_delete_student_comment_str(self):
        assert_that(calling(self.temp.deleteStudentCommentById).with_args("ala"), raises(ValueError))

    def test_delete_student_comment_empty_str(self):
        assert_that(calling(self.temp.deleteStudentCommentById).with_args(""), raises(ValueError))

    def test_delete_student_comment_float(self):
        assert_that(calling(self.temp.deleteStudentCommentById).with_args(2.3), raises(ValueError))

    def test_delete_student_comment_bool(self):
        assert_that(calling(self.temp.deleteStudentCommentById).with_args(True), raises(ValueError))

    def test_delete_student_comment_none(self):
        assert_that(calling(self.temp.deleteStudentCommentById).with_args(None), raises(ValueError))

    def test_delete_student_comment_array(self):
        assert_that(calling(self.temp.deleteStudentCommentById).with_args([]), raises(ValueError))

    def test_delete_student_comment_correct_list(self):
        self.temp.addStudentComment("Spóżnienie na lekcję.")
        self.temp.addStudentComment("Brak pracy domowej.")
        self.temp.deleteStudentCommentById(2)
        assert_that(self.temp.getAllStudentComments(), is_not(contains_string("Brak pracy domowej.")))

    def test_edit_student_comment_not_contains_old(self):
        self.temp.addStudentComment("Spóżnienie na lekcję.")
        self.temp.editStudentCommentById(1, "Spóźnienie na wykład.")
        assert_that(self.temp.getAllStudentComments(), is_not(contains_string("Spóżnienie na lekcję.")))

    def test_edit_student_comment_correct_contains_new(self):
        self.temp.addStudentComment("Spóżnienie na lekcję.")
        self.temp.editStudentCommentById(1, "Spóźnienie na wykład.")
        assert_that(self.temp.getAllStudentComments(), contains_string("Spóźnienie na wykład."))

    def test_edit_student_comment_correct(self):
        self.temp.addStudentComment("Spóżnienie na lekcję.")
        assert_that(
            self.temp.editStudentCommentById(1, "Spóźnienie na wykład."),
            equal_to("Zmieniono treść uwagi z \"Spóżnienie na lekcję.\" na \"Spóźnienie na wykład.\""))

    def test_edit_student_comment_not_existing(self):
        assert_that(
            self.temp.editStudentCommentById(4, "....."),
            raises(Exception)
        )

    def test_edit_student_comment_id_negative(self):
        self.temp.addStudentComment("Spóżnienie na lekcję.")
        assert_that(
            self.temp.editStudentCommentById(-4, "....."),
            raises(ValueError)
        )

    def test_edit_student_comment_id_float(self):
        self.temp.addStudentComment("Spóżnienie na lekcję.")
        assert_that(
            self.temp.editStudentCommentById(1.2, "....."),
            raises(ValueError)
        )

    def test_edit_student_comment_id_str(self):
        self.temp.addStudentComment("Spóżnienie na lekcję.")
        assert_that(
            self.temp.editStudentCommentById("ala", "....."),
            raises(ValueError)
        )

    def test_edit_student_comment_id_empty_str(self):
        self.temp.addStudentComment("Spóżnienie na lekcję.")
        assert_that(
            self.temp.editStudentCommentById("", "....."),
            raises(ValueError)
        )

    def test_edit_student_comment_id_bool(self):
        self.temp.addStudentComment("Spóżnienie na lekcję.")
        assert_that(
            self.temp.editStudentCommentById(False, "....."),
            raises(ValueError)
        )

    def test_edit_student_comment_id_none(self):
        self.temp.addStudentComment("Spóżnienie na lekcję.")
        assert_that(
            self.temp.editStudentCommentById(None, "....."),
            raises(ValueError)
        )

    def test_edit_student_comment_id_array(self):
        self.temp.addStudentComment("Spóżnienie na lekcję.")
        assert_that(
            self.temp.editStudentCommentById([], "....."),
            raises(ValueError)
        )

    def test_edit_student_comment_content_int(self):
        self.temp.addStudentComment("Spóżnienie na lekcję.")
        assert_that(
            self.temp.editStudentCommentById(1, 5),
            raises(ValueError)
        )

    def test_edit_student_comment_content_float(self):
        self.temp.addStudentComment("Spóżnienie na lekcję.")
        assert_that(
            self.temp.editStudentCommentById(1, 2.3),
            raises(ValueError)
        )

    def test_edit_student_comment_content_empty_str(self):
        self.temp.addStudentComment("Spóżnienie na lekcję.")
        assert_that(
            self.temp.editStudentCommentById(1, ""),
            raises(ValueError)
        )

    def test_edit_student_comment_content_bool(self):
        self.temp.addStudentComment("Spóżnienie na lekcję.")
        assert_that(
            self.temp.editStudentCommentById(1, False),
            raises(ValueError)
        )

    def test_edit_student_comment_content_none(self):
        self.temp.addStudentComment("Spóżnienie na lekcję.")
        assert_that(
            self.temp.editStudentCommentById(1, None),
            raises(ValueError)
        )

    def test_edit_student_comment_content_array(self):
        self.temp.addStudentComment("Spóżnienie na lekcję.")
        assert_that(
            self.temp.editStudentCommentById(1, []),
            raises(ValueError)
        )

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
