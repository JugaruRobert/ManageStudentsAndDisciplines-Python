from Lab3.Controller.UndoRedoController import *
from Lab3.Controller.studentController import *


class StudentControllerWithUndo(StudentController):

    def __init__(self, undoController, repo,repo1,repo2): # rentalController,
        StudentController.__init__(self, repo,repo1,repo2)
        #self._rentalController = rentalController
        self._undoController = undoController

    def addStudent(self, student):
        """
        Function used for adding an object of type student to the student list.
        The object is placed on the student's id position in the dictionary
        input:stud - an onject belonging to the student class
        output:-
        """
        self._undoController.newOperation()
        redo = FunctionCall(StudentController.addStudent, self,student)
        undo = FunctionCall(StudentController.removeStudentByID,self,student.getID())
        StudentController.addStudent(self, student)
        operation = Operation(redo, undo)
        self._undoController.recordOperation(operation)

    def removeStudentByID(self,studID):
        """
        Remove the entry at the given index from the list of sudents.
        input: studID- A natural number ,the id of the student that must be removed.
        """
        self._undoController.newOperation()
        g=StudentController.filterStud(self, studID)
        redo=FunctionCall(StudentController.removeStudFromGrades,self,studID)
        undo = FunctionCall(StudentController.addFilterStud, self, g)
        StudentController.removeStudFromGrades(self,studID)
        operation = Operation(redo, undo)
        self._undoController.recordOperation(operation)

        redo = FunctionCall(StudentController.removeStudentByID,self,studID)
        undo = FunctionCall(StudentController.addStudent,self,StudentController.getStud(self,studID))
        StudentController.removeStudentByID(self,studID)
        operation = Operation(redo, undo)
        self._undoController.recordOperation(operation)

    def updateStudent(self, oldID,newStud):
        """
        Function used for updating the information of a student.The student is searched in the dictionary by the
        ID and if it is found, the entire object it is replaced with another object with updated information.
        input:oldID-the ID of the student whose information must be updated,newStudent - an object belonging to the student
        class with the updated information
        output:-
        """
        self._undoController.newOperation()
        redo = FunctionCall(StudentController.updateStudent, self, oldID,newStud)
        undo = FunctionCall(StudentController.updateStudent, self, newStud.getID(), StudentController.getStud(self,oldID))
        StudentController.updateStudent(self, oldID,newStud)
        operation = Operation(redo, undo)
        self._undoController.recordOperation(operation)

    def addDiscipline(self, discipline):
        """
        Function used for adding an object of type discipline to the disciplines list.
        The object is placed on the discipline's id position in the dictionary.
        input:dis - an onject belonging to the discipline class
        output:-
        """
        self._undoController.newOperation()
        redo = FunctionCall(StudentController.addDiscipline, self,discipline)
        undo = FunctionCall(StudentController.removeDisciplineByID,self,discipline.getID())
        StudentController.addDiscipline(self, discipline)
        operation = Operation(redo, undo)
        self._undoController.recordOperation(operation)

    def removeDisciplineByID(self,disID):
        """
        Remove the entry at the given index from the list of disciplines.
        index - A natural number ,the ID of the discipline.
        """
        self._undoController.newOperation()
        g=StudentController.filterDis(self, disID)
        redo=FunctionCall(StudentController.removeDisFromGrades,self,disID)
        undo = FunctionCall(StudentController.addFilterDis, self, g)
        StudentController.removeDisFromGrades(self,disID)
        operation = Operation(redo, undo)
        self._undoController.recordOperation(operation)

        redo = FunctionCall(StudentController.removeDisciplineByID,self,disID)
        undo = FunctionCall(StudentController.addDiscipline,self,StudentController.getDis(self,disID))
        StudentController.removeDisciplineByID(self,disID)
        operation = Operation(redo, undo)
        self._undoController.recordOperation(operation)

    def updateDiscipline(self, oldID, newDis):
        """
        Function used for updating the information of a discipline.The discipline is searched in the dictionary by the ID and if it is
        found, the entire object it is replaced with another object with updated information.
        input:oldID-the ID of the student whose information must be updated,newDis - an object belonging to the discipline.
        output:-
        """
        self._undoController.newOperation()
        redo = FunctionCall(StudentController.updateDiscipline, self, oldID,newDis)
        undo = FunctionCall(StudentController.updateDiscipline, self, newDis.getID(), StudentController.getDis(self,oldID))
        StudentController.updateDiscipline(self, oldID,newDis)
        operation = Operation(redo, undo)
        self._undoController.recordOperation(operation)

    def addGrade(self,grade):
        """
        function used for adding an object of type grade to the grade list.
        The object is placed on the student's id position in the dictionary, on the
        discipline id in the second dictionary which is inside the first one.
        input:grade - an object belonging to the student class
        output:-
        """
        self._undoController.newOperation()
        redo = FunctionCall(StudentController.addGrade, self, grade)
        undo = FunctionCall(StudentController.removeGrade, self, grade.getStudent().getID(),grade.getDiscipline().getID())
        StudentController.addGrade(self, grade)
        operation = Operation(redo, undo)
        self._undoController.recordOperation(operation)

    def removeGrade(self,studID,disID):
        """
        function used for removing the last grade given to a student.
        input:studID-id of a student, disID-id of a discipline.
        output:-
        """
        gr=StudentController.getGrade(self, studID, disID)
        self._undoController.newOperation()
        redo = FunctionCall(StudentController.removeGrade, self, studID,disID)
        undo = FunctionCall(StudentController.addGrade, self, gr)
        StudentController.removeGrade(self, studID, disID)
        operation = Operation(redo, undo)
        self._undoController.recordOperation(operation)
