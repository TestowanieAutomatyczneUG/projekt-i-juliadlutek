import unittest
import json
from src.sample.student import Student


class TestFizzBuzz(unittest.TestCase):
    def setUp(self):
        self.temp = Student("Jan", "Nowak", 10)
        self.temp.addStudentLecture("Matematyka")
        self.temp.addStudentGrade(4)

    def test_from_file(self):
        file = open("../data/data.json")
        testData = json.load(file)
        file.close()
        for [name, grade, expected] in testData:
            if expected == 1:
                self.assertRaises(ValueError, self.temp.deleteStudentGrade, name, grade)
            elif expected == 2:
                self.assertRaises(Exception, self.temp.deleteStudentGrade, name, grade)


if __name__ == "__main__":
    unittest.main()