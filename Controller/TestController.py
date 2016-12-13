import unittest
from Lab3.Controller.studentController import *
from Lab3.Repository.StudentRepo import *
from Lab3.Controller.StudentControllerWithUndo import *
from Lab3.Controller.UndoRedoController import *

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.__repo = StudRepo()
        self.__repo1 = DisRepo()
        self.__repo2 = GradeRepo()
        self._undo=UndoController()
        self._controller = StudentControllerWithUndo(self._undo,self.__repo,self.__repo1,self.__repo2)

    def testGetAllStudents(self):
        self.__repo.removeAll()
        assert len(self._controller.getAllStudents())==0
        g = [1, 2, 3]
        s = student(8, "Andrei", g)
        self.__repo.add(s)
        assert self.__repo.get(8)==s
        assert len(self._controller.getAllStudents()) == 1

    def testGetAllDisciplines(self):
        self.__repo1.removeAll()
        assert len(self._controller.getAllDisciplines())==0
        s = discipline(10, "math")
        self.__repo1.add(s)
        assert self.__repo1.get(10)==s
        assert len(self._controller.getAllDisciplines()) == 1

    def testAddGrade(self):
         self.__repo2.removeAll()
         gradeList = [10, 2, 9]
         disList = [1, 2, 3, 10]
         s = student(11, "Andrei", disList)
         self.__repo.add(s)
         d = discipline(10, "Math")
         self.__repo1.add(d)
         g = grade(s, d, gradeList)
         self.__repo2.addGrade(g)
         assert len(self.__repo2.getAll()) == 1
         self.__repo2.removeAll()

    def testRemoveAllGrades(self):

        gradeList = [10, 2, 9]
        disList = [1, 2, 3, 10]

        s = student(11, "Andrei", disList)
        self.__repo.add(s)
        d = discipline(10, "Math")
        self.__repo1.add(d)
        g = grade(s, d, gradeList)
        self.__repo2.addGrade(g)
        assert len(self.__repo2.getAll()) == 1
        self.__repo2.removeAll()
        assert len(self.__repo2.getAll()) == 0

    def testUndo(self):
        self.__repo.removeAll()
        s = discipline(1, "math")
        self.__repo1.add(s)
        g = [1]
        s = student(8, "Andrei", g)
        self._controller.addStudent(s)
        assert len(self._controller.getAllStudents()) == 1
        self._undo.undo()
        assert len(self._controller.getAllStudents()) == 0
        self.__repo2.removeAll()

    def testRedo(self):
        self.__repo.removeAll()
        s = discipline(1, "math")
        self.__repo1.add(s)
        g = [1]
        s = student(8, "Andrei", g)
        self._controller.addStudent(s)
        assert len(self._controller.getAllStudents()) == 1
        self._undo.undo()
        assert len(self._controller.getAllStudents()) == 0
        self._undo.redo()
        assert len(self._controller.getAllStudents()) == 1
        self.__repo2.removeAll()

if __name__ == '__main__':
    unittest.main()
