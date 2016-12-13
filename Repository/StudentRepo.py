from Lab3.Domain.Classes import *
from Lab3.Repository.ExceptionRepo import RepositoryException

class StudRepo:

    def __init__(self):
        """
        -constructor-
        __students = a dictionary of students
        """
        self.__students = {}

    #def setStudList(self,x):
        #self.__students=x

    def add(self,stud):
        """
        Function used for adding an object of type student to the student list.
        The object is placed on the student's id position in the dictionary
        RepositoryException if the provided ID is invalid.
        input:stud - an onject belonging to the student class
        output:-
        """
        if stud.getID() in self.__students:
            raise RepositoryException("There is already a student with this id!")
        else:
            self.__students[stud.getID()]=stud

    def updateStudent(self, oldID,newStudent):
        """
        Function used for updating the information of a student.The student is searched in the dictionary by the
        ID and if it is found, the entire object it is replaced with another object with updated information.
        RepositoryException if the provided information is invalid.
        input:oldID-the ID of the student whose information must be updated,newStudent - an object belonging to the student
        class with the updated information
        output:-
        """
        if oldID not in self.__students:
            raise RepositoryException("There is no student with this id!")
        elif newStudent.getID() in self.__students and oldID!=newStudent.getID():
            raise RepositoryException("New ID not valid! There is already a student with this ID!")
        else:
            temp={}
            for i in self.__students:
                if i != oldID:
                    temp[i]=self.get(i)
                else:
                    temp[newStudent.getID()]=newStudent
            self.__students = temp

    def removeStudentID(self, index):
        """
        Remove the entry at the given index from the list of sudents.
        RepositoryException if the provided index is invalid.
        input: index - A natural number ,the id of the student that must be removed.
        """
        if index not in self.__students:
            raise RepositoryException("There is no student with this id!")
        return self.__students.pop(index)

    def removeAll(self):
        """
        Remove all data from the list of students.
        """
        self.__students.clear()

    def __len__(self):
        """
        Function used for returning the lenght of the student list.
        input:-
        output:the lenght of the student list
        """
        return len(self.__students)

    def get(self, index):
        """
        Get a student from the list of students.
        RepositoryException - If an invalid position is given
        index - ID of the student.

        """
        if index not in self.__students:
            raise RepositoryException("There is no student with this ID!")
        return self.__students[index]

    def getAll(self):
        """
        Returns the entire list of students.
        """
        return self.__students

    def printAll(self):
        """
        Prints the entire list of students.All objects from the student class from the dictionary
        are printed in the console.
        """
        if len(self.__students)==0:
            raise RepositoryException("The list of students is empty!")
        else:
            msg = ""
            msg +="\n~Students~\n"
            for i in self.__students:
                msg += "\n"+str(self.__students.get(i))
        return msg

class DisRepo:

    def __init__(self):
        """
        -constructor-
        __disciplines = a dictionary of disciplines.
        """
        self.__disciplines = {}

    #def setDisList(self,x):
        #self.__disciplines=x

    def add(self, dis):
        """
        Function used for adding an object of type discipline to the disciplines list.
        The object is placed on the discipline's id position in the dictionary.
        RepositoryException if the provided ID is invalid.
        input:dis - an onject belonging to the discipline class
        output:-
        """
        if dis.getID() in self.__disciplines:
            raise RepositoryException("There is already a discipline with this id!")
        else:
            self.__disciplines[dis.getID()]=dis

    def updateDiscipline(self, oldID,newDis):
        """
        Function used for updating the information of a discipline.The discipline is searched in the dictionary by the ID and if it is
        found, the entire object it is replaced with another object with updated information.
        RepositoryException if the provided information is invalid.
        input:oldID-the ID of the student whose information must be updated,newDis - an object belonging to the discipline.
        output:-
        """
        if oldID not in self.__disciplines:
            raise RepositoryException("There is no discipline with this id!")
        elif newDis.getID() in self.__disciplines and oldID!=newDis.getID():
            raise RepositoryException("New ID not valid! There is already a discipline with this ID!")
        else:
            temp={}
            for i in self.__disciplines:
                if i != oldID:
                    temp[i]=self.get(i)
                else:
                    temp[newDis.getID()]=newDis
            self.__disciplines = temp

    def removeDisciplineID(self, index):
        """
        Remove the entry at the given index from the list of disciplines.
        index - A natural number ,the ID of the discipline.
        RepositoryException if the provided index is invalid
        """
        if index not in self.__disciplines:
            raise RepositoryException("There is no discipline with this id!")
        return self.__disciplines.pop(index)

    def removeAll(self):
        """
        Remove all data from the list of disciplines.
        """
        self.__disciplines.clear()

    def __len__(self):
        """
        Function used for returning the lenght of the discipline list.
        input:-
        output:the lenght of the discipline list
        """
        return len(self.__disciplines)

    def get(self, index):
        """
        Get a discipline object from the list of discipline.
        index - id of the discipline
        RepositoryException - If an invalid position is given
        """
        if index not in self.__disciplines:
            raise RepositoryException("There is no discipline with this ID.")
        return self.__disciplines[index]

    def getAll(self):
        """
        Returns the entire list of disciplines.
        """
        return self.__disciplines

    def printAll(self):
        """
        Prints the entire list of students.All objects from the student class from the dictionary are printed in the console.
        """
        if len(self.__disciplines)==0:
            raise RepositoryException("The list of disciplines is empty!")
        else:
            msg = ""
            msg+="\n~Disciplines~\n"
            for i in self.__disciplines:
                msg += "\n"+str(self.__disciplines.get(i))
        return msg

class GradeRepo:

    def __init__(self):
        """
        -constructor-
        __grades = a dictionary students with discipline and grades
        """
        self.__grades = {}

    def setGradeList(self,x):
        self.__grades=x

    def removeAll(self):
        """
        Remove all data from the list of disciplines.
        """
        self.__grades.clear()



    def removeStudent(self,index):
        """
        function used from removing a student by its it from the list of grades
        """
        if index in self.__grades:
            self.__grades.pop(index)

    def removeDiscipline(self, index):
        """
        function used from removing a discipline by its it from the list of grades
        """
        temp = {}
        for i in self.__grades:
            if index in self.__grades[i]:
                self.__grades[i].pop(index)

        for i in self.__grades:
            if len(self.__grades[i])!=0:
                temp[i]=self.__grades[i]

        self.__grades=temp

    def getAll(self):
        """
        Returns the entire list of disciplines.
        """
        return self.__grades

    def addGrade(self, grade):
        """
        function used for adding an object of type grade to the grade list.
        The object is placed on the student's id position in the dictionary, on the
        discipline id in the second dictionary which is inside the first one.
        input:grade - an object belonging to the student class,studList-the list of students
        RepositoryException if the provided grade is invalid.
        disList-the list of disciplines.
        output:-
        """

        studID = grade.getStudent().getID()
        disID  = grade.getDiscipline().getID()
        g=grade.getStudent().getDisciplines()
        gr=grade.getGrade()

        gList=[]
        gList.append(grade.getGrade())
        if disID not in g:
            raise RepositoryException("The student with this ID it is not enrolled at that discipline!")
        elif studID not in self.__grades :
            self.__grades[studID]={disID:gList}
        elif disID not in self.__grades[studID]:
            self.__grades[studID][disID]=gList
        else:
            self.__grades[studID][disID].append(grade.getGrade())



    def __len__(self):
        """
        Function used for returning the lenght of the grade list.
        input:-
        output:the lenght of the student list
        """
        return len(self.__grades)










