import unittest
from src.sample.student import Student
from parameterized import parameterized, parameterized_class


class StudentParametrizedPackage(unittest.TestCase):
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
    def test_invalid_arguments_parameterized(self, name, grade, expected):
        self.assertRaises(expected, self.temp.addStudentGrade, name, grade)


@parameterized_class(('name', 'grade', 'expected'), [
    ("Angielski", 5, "Dodano ocenę 5 do przedmiotu Angielski"),
    ("Matematyka", 2, "Dodano ocenę 2 do przedmiotu Matematyka"),
    ("Angielski", 1, "Dodano ocenę 1 do przedmiotu Angielski")
])
class StudentParameterizedPackage2(unittest.TestCase):
    def setUp(self):
        self.temp = Student("Jan", "Nowak", 10)
        self.temp.addStudentLecture("Angielski")
        self.temp.addStudentLecture("Matematyka")

    def test_correct_parameterized(self):
        self.assertEqual(self.temp.addStudentGrade(self.name, self.grade), self.expected)


if __name__ == '__main__':
    unittest.main()
