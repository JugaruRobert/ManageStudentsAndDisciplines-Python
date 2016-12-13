from Lab3.Repository.ExceptionRepo import RepositoryException
from Lab3.Domain.Classes import *
from operator import itemgetter, attrgetter
import copy

class StudentController:
    """
    Application Controller.
    """

    def __init__(self, repo,repo1,repo2):
        """
        ~ constructor ~
        Dependency injection.
        """
        self.__repo = repo
        self.__repo1 = repo1
        self.__repo2 = repo2

    def getAllStudents(self):
        """
        returning the entire list of students
        """
        return self.__repo.getAll()

    def getStud(self,id):
        """
        returning a student object from the list of students.
        id - natural number representing the id of the student.
        """
        return self.__repo.get(id)

    def addStudent(self, student):

        """
        calling the function from repository for adding a student in the student list ( repositoryStud class)
        student - an object of class student
        """
        g=student.getDisciplines()
        for i in g:
            if i not in self.getAllDisciplines():
                raise RepositoryException("The ID for one of the disciplines is invalid!")
        self.__repo.add(student)

    def updateStudent(self, oldID, newStud):
        """
        calling the function from repository for updating the information of a student.The student is searched in the dictionary by the
        ID and if it is found, the entire object it is replaced with another object with updated information.
        input:oldID-the ID of the student whose information must be updated,newStudent - an object belonging to the student
        class with the updated information
        output:-
        """
        self.__repo.updateStudent(oldID, newStud)

    def removeStudentByID(self, index):
        """
        calling the function from repository for removing a student from repository by id
        index- a natural number representing the student's id
        """
        self.__repo.removeStudentID(index)

    def removeStudFromGrades(self,index):
        self.__repo2.removeStudent(index)

    def filterStud(self, index):
        g = []
        gList=self.__repo2.getAll()
        if index in gList:
            for i in gList[index]:
                for k in gList[index][i]:
                    g.append(grade(self.getStud(index), self.getDis(i), k))
        return g

    def addFilterStud(self,g):
        for i in g:
            self.__repo2.addGrade(i)

    def removeAllStudents(self):
        """
        calling the function from repository for removing all the students from the list of students
        """
        self.__repo.removeAll()

    def printAll(self):
        """
        calling the function from repository for printing all the students.
        """
        return self.__repo.printAll()

    def getAll(self):
        """
        calling the function from repository for returning the entire list of students.
        """
        return self.__repo.getAll()

    def printStudByID(self,id):
        """
        calling the function from repository for printing a student with a specific id.
        input:id-a natural number representing the student's ID
        """
        return "\n"+str(self.__repo.get(id))

    def printStudByName(self,name):
        """
        calling the function from repository for printing all the students with a specific name.
        This is not case-sensitive and works for partial strings matching.
        input:name - a string
        """
        msg=""
        ok=False
        g=self.__repo.getAll()
        for i in g:
            studName=g[i].getName()
            studName=studName.lower()
            if studName == name or studName.find(name)!=-1:
                msg +="\n"+str(g[i])
                ok=True
        if ok==False:
            raise RepositoryException("No matching results were found!")
        return msg

    #-----------------------------------------

    def getAllDisciplines(self):
        """
        returning the entire list of students
        """
        return self.__repo1.getAll()

    def addDiscipline(self, discipline):
        """
        adding a student in the discipline list ( repositoryDis class)
        discipline - an object of class discipline
        """
        self.__repo1.add(discipline)

    def getDis(self,id):
        """
        returning a discipline object from the list of disciplines.
        id - natural number representing the id of the discipline.
        """
        return self.__repo1.get(id)

    def updateDiscipline(self, oldID, newDis):
        """
        calling the function from repository for updating the information of a discipline.The discipline is searched in the
        dictionary by the ID and if it is found, the entire object it is replaced with another object with updated information.
        input:oldID-the ID of the student whose information must be updated,newDis - an object belonging to the discipline
        class with the updated information.
        output:-
        """
        self.__repo1.updateDiscipline(oldID, newDis)

    def removeDisciplineByID(self, index):
        """
        calling the function from repository for removing a dsicipline from repository by id
        index- a natural number representing the discipline's id
        """
        self.__repo1.removeDisciplineID(index)

    def removeDisFromGrades(self,index):
        self.__repo2.removeDiscipline(index)

    def filterDis(self, index):
        g = []
        gList=self.__repo2.getAll()
        for i in gList:
            for j in gList[i]:
                if j==index:
                    for k in gList[i][j]:
                        g.append(grade(self.getStud(i), self.getDis(j), k))
        return g

    def addFilterDis(self,g):
        for i in g:
            self.__repo2.addGrade(i)

    def removeDisciplineByName(self, name):
        """
        calling the function from repository for removing all the discipline with a specific name from the repository
        name-string, discipline's name
        """
        self.__repo1.removeDisciplineName(name)

    def removeAllDisciplines(self):
        """
        calling the function from repository for removing all the disciplines from the list of dsicsiplines.
        """
        self.__repo1.removeAll()

    def printAllDis(self):
        """
        calling the function from repository for printing all the disciplines.
        """
        return self.__repo1.printAll()

    def printDisByID(self,id):
        """
        calling the function from repository for printing a discipline with a specific id.
        input:id-a natural number representing the discipline's ID
        """
        return "\n"+str(self.__repo1.get(id))

    def printDisByName(self,name):
        """
        calling the function from repository for printing all the disciplines with a specific name.
        This is not case-sensitive and works for partial strings matching.
        input:name - a string
        """
        msg = ""
        ok=False
        g=self.__repo1.getAll()
        for i in g:
            disName=g[i].getName()
            disName=disName.lower()
            if disName == name or disName.find(name)!=-1:
                msg += "\n"+ str(g[i])
                ok=True
        if ok==False:
            raise RepositoryException("No matching results were found!")
        return msg

    #------------------------------------------------------
    def getGrade(self,studID,disID):
        """
        function used for returning a grade object from a student's id and an id of the discipline
        input: studID-integer,id of a student,disID-integer,disciplineID
        output:g-an object belonging to the grade class
        """
        g=self.__repo2.getAll()
        student=self.getStud(studID)
        discipline=self.getDis(disID)
        gList=g[studID][disID]
        g=grade(student,discipline,gList[len(gList) - 1])
        return g

    def addGrade(self,grade):
        """
        adding a grade in the grade list ( StudRepo class)
        input:grade - an object of class grade,studList -the list of students,
        disList-the list of disciplines.
        """
        studID = grade.getStudent().getID()
        disID  = grade.getDiscipline().getID()

        if studID not in  self.getAllStudents():
            raise RepositoryException("There is no student with this ID!")
        elif disID not in self.getAllDisciplines():
            raise RepositoryException("There is no discipline with this ID!")
        else:
            self.__repo2.addGrade(grade)
        self.printGrades()

    def removeGrade(self,studID,disID):
        """
        removing the last grade given to a student from the grade list
        input: studID-integer,id of a student,disID-integer,disciplineID
        disList-the list of disciplines.
        """

        if studID not in  self.getAllStudents():
            raise RepositoryException("There is no student with this ID!")
        elif disID not in self.getAllDisciplines():
            raise RepositoryException("There is no discipline with this ID!")
        else:
            gList = self.__repo2.getAll()
            if studID not in gList:
                raise RepositoryException("The student with this ID has no grades!")
            elif disID not in gList[studID]:
                raise RepositoryException("The student with this ID has no grades at this discipline!")
            else:
                if len(gList[studID][disID]) == 1:
                    gList[studID].pop(disID)
                    if len(gList[studID]) == 0:
                        gList.pop(studID)
                else:
                    g = gList[studID][disID]
                    g.pop()
                    gList.pop(studID)
                    for i in g:
                        gr=grade(self.getStud(studID),self.getDis(disID), i)
                        StudentController.addGrade(self,gr)

        self.__repo2.setGradeList(gList)

    def fail(self):
        """
        Function used for printing all the students that fail at one or more disciplines.
        input:-
        output:the string containing all the students that fails
        """
        temp={}
        ok=False

        GradeList = self.averageGrades()
        for i in GradeList:
            for j in GradeList[i]:
                if GradeList[i][j]<5:
                    if i not in temp:
                        temp[i] = {j:GradeList[i][j]}
                    else:
                        temp[i][j] = GradeList[i][j]

        failList = []

        if len(temp)==0:
            raise RepositoryException("There is no student that fails at a discipline!")
        else:
            for i in temp:
                for j in temp[i]:
                    failList.append(ObjectPlusAverage(self.getStud(i), str(temp[i][j])))

        return failList


        """
        if len(temp)==0:
            raise RepositoryException("There is no student that fails at a discipline!")
        else:
            msg=""
            for i in temp:
                for j in temp[i]:
                    msg+="\n"+str(self.getStud(i))+"\tAverage:" + str(temp[i][j])+"\n"
            return msg
        """

    def bestStud(self):
        """
        Function used for printing all the students in descending order by their agregared grade
        input:-
        output:the string containing all the students
        """
        ts=0
        tnr=0
        temp=[]
        GradeList = self.averageGrades()

        for i in GradeList:
            for j in GradeList[i]:
                ts=ts+GradeList[i][j]
                tnr=tnr+1
            avg=float(ts/tnr)
            avg=round(avg,2)
            tup=(i,avg)
            temp.append(tup)

        temp=sorted(temp, key=lambda avg: temp[1],reverse=True)

        bestS=[]

        if len(temp)==0:
            raise RepositoryException("There is no students in the list!")
        else:
            for i in temp:
                bestS.append(ObjectPlusAverage(self.getStud(i[0]), str(i[1])))
        """
        msg=""
        for i in temp:
            msg+="\n"+str(self.getStud(i[0])) + " - Average:" + str(i[1]) + "\n"
        return msg
        """
        return bestS

    def averageGrades(self):
        """
        Function used for calculating the average grades for students at each discipline
        input:-
        output:the string containing all the students with their average grade at all disciplines
        """
        temp = {}
        GradeList = self.__repo2.getAll()
        for i in GradeList:
            for j in GradeList[i]:
                avg = 0
                nr = 0
                s = 0
                g = GradeList[i][j]
                for k in g:
                    nr = nr + 1
                    s = s + k
                avg = float(s / nr)
                avg=round(avg, 2)
                if i not in temp:
                    temp[i] = {j: avg}
                else:
                    temp[i][j] = avg
        return temp

    def printEnrolled(self,id,sort):
        """
        Function used for printing all the students that are enrolled at a given discipline
        input:id-id of the discipline,sort-sort method
        output:the string containing all the students enrolled
        """
        print()
        if id not in self.__repo1.getAll():
            raise RepositoryException("There is no discipline with this ID!")
        temp=self.__repo.getAll()
        #gList=self.__repo2.getAll()
        avg = self.averageGrades()
        if len(avg)==0:
            raise RepositoryException("The are no grades!")
        stud=[]
        for i in temp:
            g=temp[i].getDisciplines()
            for dis in g:
                if dis==id:
                    if i in avg:
                        if dis in avg[i]:
                            toup=(self.getStud(i),avg[i][id])
                            stud.append(toup)
                        else:
                            toup = (self.getStud(i), 0)
                            stud.append(toup)
                    else:
                        toup = (self.getStud(i), 0)
                        stud.append(toup)

        if len(stud)!=0:
            if sort==1:
                stud = sorted(stud, key=itemgetter(0))
            else:
                stud=sorted(stud, key=itemgetter(1))
                stud.reverse()

        disList=[]
        #msg=""
        #msg+="\n"+"Discipline:" + str(self.getDis(id).getName())+"\n"
        for i in stud:
            toup=(self.getDis(id).getName(),ObjectPlusAverage(i[0],i[1]))
            disList.append(toup)
            #msg+="\t- " + str(i[0].getID()) + " " + str(i[0].getName()) + " " + str(i[1])+"\n"
        return disList

    def allDisciplines(self):
        """
        Function used for printing all disciplines at which there is at least one grade in descending order
        by the average of all grades of all students at that discipline;.
        input:-
        output:the string containing the disciplines
        """
        GradeList = self.averageGrades()
        temp = []
        for i in self.getAllDisciplines():
            nr = 0
            s = 0
            for j in GradeList:
                for k in GradeList[j]:
                    if k == i:
                        if k not in temp:
                            s = s + GradeList[j][k]
                            nr = nr + 1
            if nr!=0:
                avg = float(s / nr)
                avg=round(avg,2)
                if avg != 0:
                    toup = (i, avg)
                    temp.append(toup)
                temp = sorted(temp, key=itemgetter(1))
                temp.reverse()

        disList=[]

        for i in temp:
            disList.append(ObjectPlusAverage(self.getDis(i[0]),str(i[1])))
            #msg+="\n"+str(self.getDis(i[0]))+"\t"+ " - Average:" + str(i[1]) + "\n"
        return disList

    def printGrades(self):
        """
        calling the function from repository for printing all the grades.
        input: studList -the list of students, disList - the list of disciplines.
        """
        gList=self.__repo2.getAll()
        studList=self.__repo.getAll()
        disList = self.__repo1.getAll()
        msg=""
        if len(gList)==0:
            msg+="\tThe list is empty!"
            return msg
        else:
            msg +="\n~Grades~ \n"
            for d in gList:
                msg +="\n• Student: " + "ID: " + str(studList[d].getID()) + " - " + "Name: " + str(studList[d].getName())+"\n"
                for s in gList[d]:
                    msg +="\n\t- Discipline: " + "ID: " + str(disList[s].getID()) + " - " + "Name: " + str(disList[s].getName())
                    msg +="\n\t\tGrades:"
                    g=gList[d][s]
                    for i in range(0,len(g)-1):
                        msg +=str(g[i])
                        msg+=","
                    msg += str(g[len(g)-1]) + "\n"
        return msg

class ObjectPlusAverage:
    """
    class used for creating an object tgether with an average grade
    """
    def __init__(self, object, average):
        """
        constroctor
        """
        self.__object = object
        self.__average = average

    def getObject(self):
        """
        returning the object
        """
        return self.__object

    def getAverage(self):
        """
        returning the average
        """
        return self.__average

    def __lt__(self, x):
        return self.__average < x

    def __str__(self):
        msg=""
        msg+="\n"+str(self.getObject())
        if self.__average!=0:
            msg+=" \tAverage: " + str(self.__average)
        return msg






