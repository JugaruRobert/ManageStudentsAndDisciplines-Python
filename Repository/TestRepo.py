import unittest
from Lab3.Repository.StudentRepo import *

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.__repo = StudRepo()
        self.__repo1 = DisRepo()
        self.__repo2 = GradeRepo()

    def testAddStudent(self):
        self.__repo.removeAll()
        g = [1, 2, 3]
        s = student(8, "Andrei", g)
        self.__repo.add(s)
        assert len(self.__repo.getAll()) == 1

        s = student(10, "Andrei", g)
        self.__repo.add(s)
        assert len(self.__repo.getAll()) == 2

    def testUpdateStudent(self):
        self.__repo.removeAll()

        g = [1, 2, 3]
        s = student(8, "Andrei", g)
        d = student(8, "Marius", g)
        self.__repo.add(s)
        self.__repo.updateStudent(8, d)
        assert self.__repo.get(8).getID() == 8
        assert self.__repo.get(8).getName() == "Marius"
        assert len(self.__repo.getAll()) == 1

        s = student(12, "Marius", g)
        d = student(13, "Rex", g)
        self.__repo.add(s)
        self.__repo.updateStudent(12, d)
        assert self.__repo.get(13).getID() == 13
        assert self.__repo.get(13).getName() == "Rex"
        assert len(self.__repo.getAll()) == 2

    def testRemoveStudentID(self):
        self.__repo.removeAll()
        g = [1, 2, 3]
        s = student(8, "Andrei", g)
        self.__repo.add(s)
        assert len(self.__repo.getAll()) == 1
        self.__repo.removeStudentID(8)
        assert len(self.__repo.getAll()) == 0
        s = student(8, "Andrei", g)
        self.__repo.add(s)
        s = student(9, "Marius", g)
        self.__repo.add(s)
        self.__repo.removeStudentID(8)
        assert len(self.__repo.getAll()) == 1

    def testAddDiscipline(self):
        self.__repo1.removeAll()

        s = discipline(10, "math")
        self.__repo1.add(s)
        assert len(self.__repo1.getAll()) == 1

        s = discipline(12, "hsitory")
        self.__repo1.add(s)
        assert len(self.__repo1.getAll()) == 2

    def testUpdateDiscipline(self):
        self.__repo1.removeAll()

        s = discipline(10, "math")
        d = discipline(11, "algebra")
        self.__repo1.add(s)
        self.__repo1.updateDiscipline(10, d)
        assert self.__repo1.get(11).getID() == 11
        assert self.__repo1.get(11).getName() == "algebra"
        assert len(self.__repo1.getAll()) == 1

        s = discipline(12, "history")
        d = discipline(13, "math")
        self.__repo1.add(s)
        self.__repo1.updateDiscipline(12, d)
        assert self.__repo1.get(13).getID() == 13
        assert self.__repo1.get(13).getName() == "math"
        assert len(self.__repo1.getAll()) == 2

    def testRemoveDisciplineID(self):
        self.__repo1.removeAll()

        s = discipline(1, "math")
        self.__repo1.add(s)
        assert len(self.__repo1.getAll()) == 1
        self.__repo1.removeDisciplineID(1)
        assert len(self.__repo.getAll()) == 0

        s = discipline(1, "math")
        self.__repo1.add(s)
        s = discipline(2, "history")
        self.__repo1.add(s)
        self.__repo1.removeDisciplineID(1)
        assert len(self.__repo1.getAll()) == 1
        self.__repo1.removeDisciplineID(2)
        assert len(self.__repo1.getAll()) == 0

    def testRemoveAllStudents(self):
        g = [1, 2, 3]
        s = student(8, "Andrei", g)
        self.__repo.add(s)
        assert len(self.__repo.getAll()) == 1

        s = student(10, "Andrei", g)
        self.__repo.add(s)
        assert len(self.__repo.getAll()) == 2

        self.__repo.removeAll()
        assert len(self.__repo.getAll()) == 0

    def testRemoveAllDisciplines(self):
        s = discipline(10, "math")
        self.__repo1.add(s)
        assert len(self.__repo1.getAll()) == 1

        s = discipline(12, "hsitory")
        self.__repo1.add(s)
        assert len(self.__repo1.getAll()) == 2

        self.__repo1.removeAll()
        assert len(self.__repo1.getAll()) == 0

if __name__ == '__main__':
    unittest.main()
