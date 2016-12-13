
class student:
    """
    The class for students
    """
    def __init__(self,studentID,studentName,disciplines):
        """
        -constructor-
        studentID = the id of the student
        studentName =the name of the student
        disciplines = the disciplines at which the stuident IS enrolled
        """
        self.__ID=studentID
        self.__name = studentName
        self.__dis = disciplines

    def __lt__(self,stud):
        """
        overwriting the comparison operand
        Comparing two objects of the type student
        """
        return self.getName() < stud.getName()

    def getID(self):
        """
        -getter-
        returning the student's ID
        """
        return self.__ID

    def getName(self):
        """
        -getter-
        returning the student's name
        """
        return self.__name

    def getDisciplines(self):
        """
        -getter-
        returning all the disciplines at which the student is enrolled
        """
        return self.__dis

    def setID(self,id):
        """
        -setter-
        setting the student's ID
        """
        self.__ID = id

    def setName(self,name):
        """
        -setter-
        setting the student's name
        """
        self.__name = name

    def __len__(self):
        """
        Function used for returning the lenght of the list of grades
        input:-
        output:the lenght of the list of grades
        """
        return len(self.__dis)

    def __str__(self):
        """
        printing the ID ,Name and discipline list for a discipline
        """
        self.msg = "ID: " + str(self.__ID) + "\nName: " + str(self.__name)+ "\nDisciplines: "
        x=len(self.__dis)
        for c in self.__dis:
            if x!=1:
                self.msg+=str(c)+","
            else:
                self.msg += str(c)+"\n"
            x=x-1
        return self.msg

class discipline:
    """
    The class for disciplines
    """
    def __init__(self,disID,disName):
        """
        -constructor-
        disID = the id of the discipline
        disName =the name of the discipline
        """
        self.__ID=disID
        self.__name = disName

    def getID(self):
        """
        -getter-
        returning the discipline's ID
        """
        return self.__ID

    def getName(self):
        """
        -getter-
        returning the discipline's name
        """
        return self.__name

    def setID(self,id):
        """
        -setter-
        setting the discipline's ID
        """
        self.__ID = id

    def setName(self,name):
        """
        -setter-
        setting the discipline's name
        """
        self.__name = name

    def __str__(self):
        """
        printing the ID and Name of a discipline
        """
        return "ID: " + str(self.__ID) + "\nName of the discipline: " + str(self.__name)+"\n"

class grade:
    """
    The class for grades
    """
    def __init__(self,student,discipline,grade):
        """
        -constructor-
        student = an object from the student class
        discipline = an object from the discipline class
        grade = a list of grades for one student
        """
        self.__student= student
        self.__discipline = discipline
        self.__grade_value=grade


    #def __len__(self):
        """
        returning the lenght of the list with grades

        """
        #return len(self.__grade_value)

    def getStudent(self):
        """
        -getter-
        returning the student object which contains an object from class student.
        """
        return self.__student

    def getDiscipline(self):
        """
        -getter-
        returning the discipline object which contains an object from class discipline.
        """
        return self.__discipline

    def getGrade(self):
        """
        -getter-
        returning all the grades in the grade list fro a student.
        """

        return self.__grade_value

    #def appendGrades(self,g):
        """
        Function used fro appendind some grades from a list to the grade list of a student.
        input:g-a list containing the grades that must be appended to the list of grades.
        """
        #self.__grade_value.append(g)

    #def __str__(self):
        #msg=""
        #msg+=str(self.__student)+" "+str(self.__discipline)+" "
        #for i in self.__grade_value:
            #msg +=i
        #return msg






