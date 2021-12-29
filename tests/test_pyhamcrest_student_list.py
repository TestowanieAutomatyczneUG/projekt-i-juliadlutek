import unittest
from hamcrest import *
from src.sample.studentList import StudentList
from src.sample.student import Student


class StudentListPyHamcrestTest(unittest.TestCase):
    def setUp(self):
        mariaKowalska = Student("Maria", "Kowalska", 1,
                                {"Matematyka": [5, 3], "Angielski": [5]})
        janNowak = Student("Jan", "Nowak", 2)
        annaNowak = Student("Anna", "Nowak", 3)
        self.temp = StudentList([mariaKowalska, janNowak, annaNowak])
        #Lista z jednym studentem
        self.temp2 = StudentList([mariaKowalska])
        # Lista bez studentów
        self.temp3 = StudentList()

    # Testy do pobierania listy studentów
    # W przypadku, kiedy nie ma żadnych studentów
    def test_get_empty_student_list(self):
        assert_that(self.temp3.getAllStudents(), equal_to(''))

    def test_get_student_list(self):
        assert_that(
            self.temp.getAllStudents(),
            equal_to_ignoring_whitespace("1. Maria Kowalska 2. Jan Nowak 3. Anna Nowak"))

    # Testy do pobierania studenta po id
    def test_get_student_by_id(self):
        assert_that(
            self.temp.getStudentById(1),
            instance_of(Student))

    def test_get_student_by_id_correct_name(self):
        assert_that(
            self.temp.getStudentById(1).name,
            equal_to("Maria"))

    # W przypadku, kiedy nie istnieje student o podanym id
    def test_get_not_existing_student_by_id(self):
        assert_that(calling(self.temp.getStudentById).with_args(5), raises(Exception))

    # W przypadku, kiedy podamy nieprawidłowe id
    def test_get_student_by_id_with_str(self):
        assert_that(calling(self.temp.getStudentById).with_args("maria"), raises(ValueError))

    def test_get_student_by_id_with_bool(self):
        assert_that(calling(self.temp.getStudentById).with_args(True), raises(ValueError))

    def test_get_student_by_id_with_none(self):
        assert_that(calling(self.temp.getStudentById).with_args(None), raises(ValueError))

    def test_get_student_by_id_with_array(self):
        assert_that(calling(self.temp.getStudentById).with_args([1]), raises(ValueError))

    def test_get_student_by_id_with_float(self):
        assert_that(calling(self.temp.getStudentById).with_args(2.34), raises(ValueError))

    def test_get_student_by_negative_id(self):
        assert_that(calling(self.temp.getStudentById).with_args(-2), raises(ValueError))

    # Testy do usuwania studenta po id
    def test_student_delete_by_id(self):
        self.temp.deleteStudentById(2)
        assert_that(len(self.temp.students), equal_to(2))

    # W przypadku, kiedy usuwamy jedynego studenta
    def test_student_delete_by_id_only_student(self):
        self.temp2.deleteStudentById(1)
        assert_that(self.temp2.getAllStudents(), equal_to(""))

    # W przypadku, kiedy student o podanym id nie istnieje
    def test_delete_by_id_not_existing_student(self):
        self.temp.addStudent("Maria", "Kowalska")
        assert_that(calling(self.temp.deleteStudentById).with_args(5), raises(Exception))

    # W przypadku, kiedy podamy nieprawidłowe id
    def test_delete_student_by_id_with_str(self):
        assert_that(calling(self.temp.deleteStudentById).with_args("maria"), raises(ValueError))

    def test_delete_student_by_id_with_bool(self):
        assert_that(calling(self.temp.deleteStudentById).with_args(True), raises(ValueError))

    def test_delete_student_by_id_with_none(self):
        assert_that(calling(self.temp.deleteStudentById).with_args(None), raises(ValueError))

    def test_delete_student_by_id_with_array(self):
        assert_that(calling(self.temp.deleteStudentById).with_args([1]), raises(ValueError))

    def test_delete_student_by_id_with_float(self):
        assert_that(calling(self.temp.deleteStudentById).with_args(2.34), raises(ValueError))

    def test_delete_student_by_negative_id(self):
        assert_that(calling(self.temp.deleteStudentById).with_args(-2), raises(ValueError))

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
