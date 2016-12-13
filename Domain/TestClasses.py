import unittest
from Lab3.Domain.Classes import *

class MyTestCase(unittest.TestCase):
    def testStudClass(self):
        g=[1,2,3]
        s=student(1,"Andrei",g)
        assert len(s) == 3
        assert s.getDisciplines() == [1,2,3]
        assert s.getName() != ""
        assert s.getName() != "rex"
        assert s.getName() == "Andrei"
        assert s.getID() != "1"
        assert s.getID() != ""
        assert s.getID() != 2
        assert s.getID() == 1
        s.setID(2)
        s.setName("razvan")
        assert s.getID() == 2
        assert s.getName() == "razvan"

    def testDisClass(self):
        s=discipline(1,"math")
        assert s.getName() != ""
        assert s.getName() != "rex"
        assert s.getName() == "math"
        assert s.getID() != "1"
        assert s.getID() != ""
        assert s.getID() != 2
        assert s.getID() == 1
        s.setID(2)
        s.setName("science")
        assert s.getID() == 2
        assert s.getName() == "science"

    def testGradeClass(self):
        glist = [1, 2, 3]
        s=student(1,"Mihai",[1,2,3])
        d=discipline(2,"math")
        g=grade(s,d,glist)
        assert g.getStudent() == s
        assert g.getDiscipline() == d
        assert g.getGrades() == glist
        assert g.getGrades() != "1"
        assert g.getGrades() != 1
        assert g.getGrades() != ""
        assert g.getGrades() != ['1','2','3']
        assert g.getGrades() == [1,2,3]
        g.appendGrades([8,9,10])
        assert g.getGrades() == [1,2,3,8,9,10]

if __name__ == '__main__':
    unittest.main()
