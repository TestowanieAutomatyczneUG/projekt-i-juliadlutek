import unittest
from src.sample.student import Student
from parameterized import parameterized, parameterized_class


class StudentParametrizedPackageAddGrade(unittest.TestCase):
    def setUp(self):
        self.temp = Student("Jan", "Nowak", 10)
        self.temp.addStudentLecture("Angielski")

    @parameterized.expand([
        ("Angielski", 10, ValueError),
        ("Angielski", -1, ValueError),
        ("Angielski", "ala", ValueError),
        ("Angielski", "", ValueError),
        ("Angielski", [], ValueError),
        ("Angielski", True, ValueError),
        ("Angielski", None, ValueError),
        ("Angielski", 1.45, ValueError),
        ("", 5, ValueError),
        ("Polski", 5, Exception),
        (10, 5, ValueError),
        (1.23, 5, ValueError),
        ([], 5, ValueError),
        (False, 5, ValueError),
        (None, 5, ValueError)
    ])
    def test_add_student_grade_invalid_arguments_parameterized(self, name, grade, expected):
        self.assertRaises(expected, self.temp.addStudentGrade, name, grade)


@parameterized_class(('name', 'grade', 'expected'), [
    ("Angielski", 5, "Dodano ocenę 5 do przedmiotu Angielski"),
    ("Matematyka", 2, "Dodano ocenę 2 do przedmiotu Matematyka"),
    ("Angielski", 1, "Dodano ocenę 1 do przedmiotu Angielski")
])
class StudentParameterizedPackageAddGrade2(unittest.TestCase):
    def setUp(self):
        self.temp = Student("Jan", "Nowak", 10)
        self.temp.addStudentLecture("Angielski")
        self.temp.addStudentLecture("Matematyka")

    def test_add_student_grade_correct_parameterized(self):
        self.assertEqual(self.temp.addStudentGrade(self.name, self.grade), self.expected)


class StudentParametrizedPackageEditGrade(unittest.TestCase):
    def setUp(self):
        self.temp = Student("Jan", "Nowak", 10)
        self.temp.addStudentLecture("Angielski")
        self.temp.addStudentGrade("Angielski", 1)
        self.temp.addStudentGrade("Angielski", 3)

    @parameterized.expand([
        # niepoprawny argument grade
        ("Angielski", 12, 5, ValueError),
        ("Angielski", -2, 5, ValueError),
        ("Angielski", "", 5, ValueError),
        ("Angielski", "ala", 5, ValueError),
        ("Angielski", 3.4, 5, ValueError),
        ("Angielski", None, 5, ValueError),
        ("Angielski", True, 5, ValueError),
        ("Angielski", [], 5, ValueError),
        # niepoprawny argument newGrade
        ("Angielski", 3, 12, ValueError),
        ("Angielski", 3, -2, ValueError),
        ("Angielski", 3, "", ValueError),
        ("Angielski", 3, "ala", ValueError),
        ("Angielski", 3, 3.4, ValueError),
        ("Angielski", 3, None, ValueError),
        ("Angielski", 3, True, ValueError),
        ("Angielski", 3, [], ValueError),
        # niepoprawny argument name
        ("", 3, 5, ValueError),
        (10, 3, 5, ValueError),
        (1.23, 3, 5, ValueError),
        ([], 3, 5, ValueError),
        (False, 3, 5, ValueError),
        (None, 3, 5, ValueError),
        # przedmiot, który nie istnieje
        ("Polski", 3, 5, Exception),
        # ocena, która nie istnieje
        ("Angielski", 5, 2, Exception),
        # nowa ocena równa starej
        ("Angielski", 3, 3, Exception)
    ])
    def test_edit_student_grade_invalid_arguments_parameterized(self, name, grade, newGrade, expected):
        self.assertRaises(expected, self.temp.editStudentGrade, name, grade, newGrade)


if __name__ == '__main__':
    unittest.main()
