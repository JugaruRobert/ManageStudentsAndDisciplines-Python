
from Lab3.Repository.StudentRepo import *
from Lab3.Controller.StudentControllerWithUndo import *
from Lab3.Repository.ExceptionRepo import *
from Lab3.UI.UI import *
from Lab3.Domain.Classes import *
from Lab3.Controller.UndoRedoController import *

repo = StudRepo()
repo1 = DisRepo()
repo2= GradeRepo()

disList=repo1.getAll()
undoController = UndoController()
studentController = StudentControllerWithUndo(undoController,repo,repo1,repo2)

studentController.addDiscipline(discipline(1,"math"))
studentController.addDiscipline(discipline(2,"science"))
studentController.addDiscipline(discipline(3,"history"))
studentController.addDiscipline(discipline(4,"math"))
studentController.addDiscipline(discipline(5,"geography"))
studentController.addDiscipline(discipline(6,"linguistics"))
studentController.addDiscipline(discipline(7,"languages and literature"))
studentController.addDiscipline(discipline(8,"performing arts"))
studentController.addDiscipline(discipline(9,"history"))
studentController.addDiscipline(discipline(10,"philosophy"))
studentController.addDiscipline(discipline(11,"visual arts"))
studentController.addDiscipline(discipline(12,"economics"))
studentController.addDiscipline(discipline(13,"law"))
studentController.addDiscipline(discipline(14,"political science"))
studentController.addDiscipline(discipline(15,"psychology"))
studentController.addDiscipline(discipline(16,"sociology"))
studentController.addDiscipline(discipline(17,"biology"))
studentController.addDiscipline(discipline(18,"chemistry"))
studentController.addDiscipline(discipline(19,"earth and space sciences"))
studentController.addDiscipline(discipline(20,"physics"))
studentController.addDiscipline(discipline(21,"medicine"))
studentController.addDiscipline(discipline(22,"technology"))
studentController.addDiscipline(discipline(23,"agronomy"))
studentController.addDiscipline(discipline(24,"computer science"))
studentController.addDiscipline(discipline(25,"engineering"))
studentController.addDiscipline(discipline(26,"science2"))
studentController.addDiscipline(discipline(27,"history2"))
studentController.addDiscipline(discipline(28,"math2"))
studentController.addDiscipline(discipline(29,"science3"))
studentController.addDiscipline(discipline(30,"history3"))
studentController.addDiscipline(discipline(31,"math3"))

studentController.addStudent(student(1,"Robert",[1,2,3,4]))
studentController.addStudent(student(2,"Marius",[10,22]))
studentController.addStudent(student(3,"Rex",[30]))

studentController.addStudent(student(4,"Bogdan",[10,12,13]))
studentController.addStudent(student(5,"Marian",[21,22]))
studentController.addStudent(student(6,"Mihai",[31]))
studentController.addStudent(student(7,"Alex",[31,22,23]))
studentController.addStudent(student(8,"Mihalache",[23,26]))
studentController.addStudent(student(9,"Dogar",[18]))
studentController.addStudent(student(10,"Andrei",[15,21,29]))
studentController.addStudent(student(11,"Ana",[13,29]))
studentController.addStudent(student(12,"Maria",[10]))
studentController.addStudent(student(13,"Ioana",[5,6,7]))
studentController.addStudent(student(14,"Vlad",[1,22]))
studentController.addStudent(student(15,"Razvan",[11]))
studentController.addStudent(student(16,"Madalin",[3,7,9]))
studentController.addStudent(student(17,"Cosmin",[1,2,21]))
studentController.addStudent(student(18,"Alexandra",[18]))
studentController.addStudent(student(19,"Alin",[21,22,23]))
studentController.addStudent(student(20,"Rares",[24]))
studentController.addStudent(student(21,"Calin",[15]))
studentController.addStudent(student(22,"Laurentiu",[1,2,3]))
studentController.addStudent(student(23,"Beni",[11,12]))
studentController.addStudent(student(24,"Adi",[1]))
studentController.addStudent(student(25,"Gica",[21,22,23]))
studentController.addStudent(student(26,"Viorel",[1,2]))
studentController.addStudent(student(27,"Timotei",[1]))
studentController.addStudent(student(28,"Ruben",[10,12,13]))
studentController.addStudent(student(29,"Radu",[21,22]))
studentController.addStudent(student(30,"Adina",[17]))

g=grade(student(1,"Robert",[1,2,3,4]),discipline(1,"math"),10)
studentController.addGrade(g)
g=grade(student(1,"Robert",[1,2,3,4]),discipline(4,"filosophy"),10)
studentController.addGrade(g)
g=grade(student(1,"Robert",[1,2,3,4]),discipline(1,"math"),10)
studentController.addGrade(g)
g=grade(student(2,"Marius",[10,22]),discipline(10,"philosophy"),2)
studentController.addGrade(g)
g=grade(student(3,"Rex",[30]),discipline(30,"history3"),5)
studentController.addGrade(g)
g=grade(student(4,"Bogdan",[10,12,13]),discipline(12,"economics"),9)
studentController.addGrade(g)
g=grade(student(5,"Marian",[21,22]),discipline(21,"medicine"),9)
studentController.addGrade(g)
g=grade(student(5,"Marian",[21,22]),discipline(22,"technology"),10)
studentController.addGrade(g)
g=grade(student(6,"Mihai",[31]),discipline(31,"math3"),1)
studentController.addGrade(g)
g=grade(student(6,"Mihai",[31]),discipline(31,"math3"),7)
studentController.addGrade(g)
g=grade(student(7,"Alex",[31,22,23]),discipline(23,"agronomy"),3)
studentController.addGrade(g)
g=grade(student(8,"Mihalache",[23,26]),discipline(26,"science2"),2)
studentController.addGrade(g)
g=grade(student(10,"Andrei",[15,21,29]),discipline(29,"science3"),8)
studentController.addGrade(g)
g=grade(student(11,"Ana",[13,29]),discipline(13,"law"),9)
studentController.addGrade(g)
g=grade(student(14,"Vlad",[1,22]),discipline(22,"technology"),4)
studentController.addGrade(g)
g=grade(student(16,"Madalin",[3,7,9]),discipline(7,"languages and literature"),2)
studentController.addGrade(g)
g=grade(student(16,"Madalin",[3,7,9]),discipline(9,"history"),10)
studentController.addGrade(g)
g=grade(student(18,"Alexandra",[18]),discipline(18,"chemistry"),3)
studentController.addGrade(g)
g=grade(student(18,"Alexandra",[18]),discipline(18,"chemistry"),4)
studentController.addGrade(g)
g=grade(student(19,"Alin",[21,22,23]),discipline(21,"medicine"),8)
studentController.addGrade(g)
g=grade(student(19,"Alin",[21,22,23]),discipline(22,"technology"),9)
studentController.addGrade(g)
g=grade(student(19,"Alin",[21,22,23]),discipline(23,"agronomy"),10)
studentController.addGrade(g)
g=grade(student(20,"Rares",[24]),discipline(24,"computer science"),9)
studentController.addGrade(g)
g=grade(student(20,"Rares",[24]),discipline(24,"computer science"),3)
studentController.addGrade(g)
g=grade(student(21,"Calin",[15]),discipline(15,"psychology"),5)
studentController.addGrade(g)
g=grade(student(21,"Calin",[15]),discipline(15,"psychology"),7)
studentController.addGrade(g)
g=grade(student(22,"Laurentiu",[1,2,3]),discipline(1,"math"),9)
studentController.addGrade(g)
g=grade(student(22,"Laurentiu",[1,2,3]),discipline(2,"science"),10)
studentController.addGrade(g)
g=grade(student(22,"Laurentiu",[1,2,3]),discipline(3,"history"),2)
studentController.addGrade(g)
g=grade(student(23,"Beni",[11,12]),discipline(11,"visual arts"),2)
studentController.addGrade(g)
g=grade(student(24,"Adi",[1]),discipline(1,"math"),3)
studentController.addGrade(g)
g=grade(student(24,"Adi",[1]),discipline(1,"math"),9)
studentController.addGrade(g)
g=grade(student(25,"Gica",[21,22,23]),discipline(21,"medicine"),2)
studentController.addGrade(g)
g=grade(student(25,"Gica",[21,22,23]),discipline(21,"medicine"),4)
studentController.addGrade(g)
g=grade(student(25,"Gica",[21,22,23]),discipline(23,"agronomy"),10)
studentController.addGrade(g)
g=grade(student(25,"Gica",[21,22,23]),discipline(23,"agronomy"),9)
studentController.addGrade(g)
g=grade(student(27,"Timotei",[1]),discipline(1,"math"),10)
studentController.addGrade(g)
g=grade(student(29,"Radu",[21,22]),discipline(22,"technology"),7)
studentController.addGrade(g)
g=grade(student(29,"Radu",[21,22]),discipline(21,"medicine"),8)
studentController.addGrade(g)
ui = UI(studentController,undoController)

ui.execute()
