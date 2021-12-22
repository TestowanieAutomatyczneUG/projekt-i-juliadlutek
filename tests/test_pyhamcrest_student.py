import unittest
from hamcrest import *
from src.sample.student import Student
from hamcrest.core.base_matcher import BaseMatcher


# Własny matcher sprawdzający czy wynik jest typu float
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
        self.temp = Student("Jan", "Nowak", 1,
                            {"Matematyka": [5, 4, 4], "Angielski": [4, 3]},
                            ["Uwaga1", "Uwaga2", "Uwaga3"])
        # Uczeń bez przedmiotów, ocen i uwag
        self.temp2 = Student("Maria", "Kowalska", 2)

    # Testy do usuwania przedmiotu
    def test_delete_student_lecture(self):
        assert_that(self.temp.deleteStudentLecture("Matematyka"), equal_to("Usunięto przedmiot - Matematyka!"))

    # W przypadku, kiedy podany przedmiot nie istnieje
    def test_delete_not_existing_student_lecture(self):
        assert_that(calling(self.temp.deleteStudentLecture).with_args("Polski"), raises(Exception))

    # W przypadku, kiedy podamy nieprawidłową nazwę przemiotu
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

    # Testy do obliczania średniej ze wszystkich przedmiotów
    def test_get_student_final_average_correct(self):
        assert_that(self.temp.getStudentFinalAverage(), close_to(4, 0.1))

    # Z użyciem własnego matchera
    def test_get_student_final_average_type(self):
        assert_that(self.temp.getStudentFinalAverage(), is_float())

    # W przypadku, kiedy nie ma żadnych przedmiotów
    def test_get_student_final_average_any_lectures(self):
        assert_that(calling(self.temp2.getStudentFinalAverage).with_args(), raises(Exception))

    # W przypadku, kiedy do jakiegoś przedmiotu nie ma dodanych ocen
    def test_get_student_final_average_lecture_without_grades(self):
        assert_that(self.temp.getStudentFinalAverage(), greater_than(3))

    # Testy do edycji nazwy przdmiotu
    def test_edit_student_lecture_name_correct(self):
        assert_that(self.temp.editStudentLectureName("Matematyka", "matematyka"),
                    equal_to("Zmieniono nazwę przedmiotu Matematyka na matematyka."))

    def test_edit_student_lecture_name_correct_grades(self):
        self.temp.editStudentLectureName("Matematyka", "matematyka")
        assert_that(self.temp.getStudentGrades("matematyka"),
                    contains_inanyorder(4, 5, 4))

    # W przypadku, kiedy przedmiot, który chcemy edytować nie istnieje
    def test_edit_student_lecture_not_existing(self):
        assert_that(calling(self.temp.editStudentLectureName).with_args("matematyka", "Matematyka"), raises(Exception))

    # W przypadku, kiedy podamy nieprawidłową nazwę przedmiotu
    def test_edit_student_lecture_name_empty_str(self):
        assert_that(calling(self.temp.editStudentLectureName).with_args("", "Matematyka"), raises(ValueError))

    def test_edit_student_lecture_name_int(self):
        assert_that(calling(self.temp.editStudentLectureName).with_args(-2, "Matematyka"), raises(ValueError))

    def test_edit_student_lecture_name_float(self):
        assert_that(calling(self.temp.editStudentLectureName).with_args(1.3, "Matematyka"), raises(ValueError))

    def test_edit_student_lecture_name_array(self):
        assert_that(calling(self.temp.editStudentLectureName).with_args([], "Matematyka"), raises(ValueError))

    def test_edit_student_lecture_name_bool(self):
        assert_that(calling(self.temp.editStudentLectureName).with_args(True, "Matematyka"), raises(ValueError))

    def test_edit_student_lecture_name_none(self):
        assert_that(calling(self.temp.editStudentLectureName).with_args(None, "Matematyka"), raises(ValueError))

    def test_edit_student_lecture_new_name_empty_str(self):
        assert_that(calling(self.temp.editStudentLectureName).with_args("matematyka", ""), raises(ValueError))

    def test_edit_student_lecture_new_name_int(self):
        assert_that(calling(self.temp.editStudentLectureName).with_args("matematyka", 12), raises(ValueError))

    def test_edit_student_lecture_new_name_float(self):
        assert_that(calling(self.temp.editStudentLectureName).with_args("matematyka", 12.2), raises(ValueError))

    def test_edit_student_lecture_new_name_array(self):
        assert_that(calling(self.temp.editStudentLectureName).with_args("matematyka", []), raises(ValueError))

    def test_edit_student_lecture_new_name_bool(self):
        assert_that(calling(self.temp.editStudentLectureName).with_args("matematyka", False), raises(ValueError))

    def test_edit_student_lecture_new_name_none(self):
        assert_that(calling(self.temp.editStudentLectureName).with_args("matematyka", None), raises(ValueError))

    # Testy do edycji oceny do danego przedmiotu
    def test_edit_student_grade_correct_output(self):
        assert_that(self.temp.editStudentGrade("Matematyka", 5, 4), equal_to("Zmieniono ocenę 5 na ocenę 4"))

    def test_edit_student_grade_correct(self):
        assert_that(self.temp.getStudentGrades("Matematyka"), is_not(contains_exactly(3)))

    # Sprawdzający, czy zmienia się tylko jedna ocena o podanej watości
    def test_only_one_student_grade(self):
        self.temp.editStudentGrade("Matematyka", 4, 5)
        assert_that(self.temp.getStudentGrades("Matematyka"), contains_inanyorder(5, 5, 4))

    # Testy do usuwania uwagi
    def test_delete_student_comment_correct(self):
        assert_that(self.temp.deleteStudentCommentById(1), equal_to("Usunięto uwagę \"Uwaga1\""))

    # W przypadku, kiedy uwaga o podanym id nie istnieje
    def test_delete_student_comment_not_existing(self):
        assert_that(calling(self.temp.deleteStudentCommentById).with_args(5), raises(Exception))

    # W przypadku, kiedy podamy nieprawidłowe id uwagi
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
        self.temp.deleteStudentCommentById(2)
        assert_that(self.temp.getAllStudentComments(), is_not(contains_string("Brak pracy domowej.")))

    # Testy do edycji uwagi
    def test_edit_student_comment_not_contains_old(self):
        self.temp.editStudentCommentById(1, "Spóźnienie na wykład.")
        assert_that(self.temp.getAllStudentComments(), is_not(contains_string("Spóżnienie na lekcję.")))

    def test_edit_student_comment_correct_contains_new(self):
        self.temp.editStudentCommentById(1, "Spóźnienie na wykład.")
        assert_that(self.temp.getAllStudentComments(), contains_string("Spóźnienie na wykład."))

    def test_edit_student_comment_correct(self):
        assert_that(
            self.temp.editStudentCommentById(1, "Spóźnienie na wykład."),
            equal_to("Zmieniono treść uwagi z \"Uwaga1\" na \"Spóźnienie na wykład.\""))

    # W przypadku, kiedy uwaga o podanym id nie istnieje
    def test_edit_student_comment_not_existing(self):
        assert_that(
            calling(self.temp.editStudentCommentById)
                .with_args(4, "....."),
            raises(Exception)
        )

    # W przypadku, kiedy podamy nieprawidłowe id uwagi
    def test_edit_student_comment_id_negative(self):
        assert_that(
            calling(self.temp.editStudentCommentById)
                .with_args(-4, "....."),
            raises(ValueError)
        )

    def test_edit_student_comment_id_float(self):
        assert_that(
            calling(self.temp.editStudentCommentById)
                .with_args(1.2, "....."),
            raises(ValueError)
        )

    def test_edit_student_comment_id_str(self):
        assert_that(
            calling(self.temp.editStudentCommentById)
                .with_args("ala", "....."),
            raises(ValueError)
        )

    def test_edit_student_comment_id_empty_str(self):
        assert_that(
            calling(self.temp.editStudentCommentById)
                .with_args("", "....."),
            raises(ValueError)
        )

    def test_edit_student_comment_id_bool(self):
        assert_that(
            calling(self.temp.editStudentCommentById)
                .with_args(False, "....."),
            raises(ValueError)
        )

    def test_edit_student_comment_id_none(self):
        assert_that(
            calling(self.temp.editStudentCommentById)
                .with_args(None, "....."),
            raises(ValueError)
        )

    def test_edit_student_comment_id_array(self):
        assert_that(
            calling(self.temp.editStudentCommentById)
                .with_args([], "....."),
            raises(ValueError),
        )

    # W przypadku, kiedy podamy nieprawidłową treść uwagi
    def test_edit_student_comment_content_int(self):
        assert_that(
            calling(self.temp.editStudentCommentById)
                .with_args(1, 5),
            raises(ValueError),
        )

    def test_edit_student_comment_content_float(self):
        assert_that(
            calling(self.temp.editStudentCommentById)
                .with_args(1, 2.3),
            raises(ValueError)
        )

    def test_edit_student_comment_content_empty_str(self):
        assert_that(
            calling(self.temp.editStudentCommentById)
                .with_args(1, ""),
            raises(ValueError)
        )

    def test_edit_student_comment_content_bool(self):
        assert_that(
            calling(self.temp.editStudentCommentById)
                .with_args(1, False),
            raises(ValueError)
        )

    def test_edit_student_comment_content_none(self):
        assert_that(
            calling(self.temp.editStudentCommentById)
                .with_args(1, None),
            raises(ValueError)
        )

    def test_edit_student_comment_content_array(self):
        assert_that(
            calling(self.temp.editStudentCommentById)
                .with_args(1, []),
            raises(ValueError)
        )

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
