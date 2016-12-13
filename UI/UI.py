import sys


from Lab3.Domain.Classes import *
from Lab3.Controller.UndoRedoController import *

class UI:
    """
    Class for UI.
    """
    def __init__(self, controller,undoController):
        """
        -constructor -
        Dependency injection.
        controller - the controller module.
        """
        self._controller = controller
        self._undo= undoController

    def printMenu():
        """
        Function used for printing the menu with all the available commands in the console
        input:-
        output:The menu is printed
        """
        msg ="\nThis is a list with all the available commands:"
        msg += "\n• Students:"
        msg += "\n\tPress 1 to add a new student"
        msg += "\n\tPress 2 to update the information of a student"
        msg += "\n\tPress 3 to remove a student by id"
        msg += "\n\tPress 4 to remove all the students in the list"
        msg += "\n\tPress 5 to search a student by ID."
        msg += "\n\tPress 6 to search all the students with a specific name(partial string matching,not case sensitive)"
        msg += "\n\tPress 7 list all the students\n"
        msg += "\n• Disciplines:"
        msg += "\n\tPress 8 to add a new discipline"
        msg += "\n\tPress 9 to update the information of a discipline"
        msg += "\n\tPress 10 to remove a discipline by ID"
        msg += "\n\tPress 11 remove all the disciplines in the list"
        msg += "\n\tPress 12 to search a discipline by ID."
        msg += "\n\tPress 13 to search all the disciplines with a specific name(partial string matching,not case sensitive)"
        msg += "\n\tPress 14 list all the disciplines\n"

        msg += "\n• Grades:"
        msg += "\n\tPress 15 to grade a student"
        msg += "\n\tPress 16 to remove the last grade given to a student"
        msg += "\n\tPress 17 to show the list of students with grades\n"
        msg += "\n• Statistics:"
        msg += "\n\tPress 18 to show all students enrolled at a given discipline, sorted alphabetically or by descending order of average grade."
        msg += "\n\tPress 19 to show all students failing at one or more disciplines."
        msg += "\n\tPress 20 to show students with the best school situation, sorted in descending order of their aggregated average."
        msg += "\n\tPress 21 to show all disciplines at which there is at least one grade, sorted in descending order of the average grade received by all students enrolled at that discipline.\n"
        msg += "\n• Undo/Redo:"
        msg += "\n\tPress 22 to undo the last made operaion."
        msg += "\n\tPress 23 to redo the last made operaion.\n"

        msg += "\nPress -1 to see the menu with commands"
        msg += "\nPress 0 to exit the application"

        print(msg)

    def execute(self):
        """
        Function used for reading the command from the user and calling the function from the controller module
        to do that specific command.If the command is not valid, a message is printed.Otherwise, the user is asked to
        introduce the information that is needed for applying the changes.
        """
        UI.printMenu()
        i=0
        while True:
            try:
                command = input("\nEnter command: ")
                if len(command) == 0:
                    print("\nInvalid Command!")

                elif command == "0":
                    print("\n\tGoodbye! :)\n")
                    sys.exit()

                elif command == "-1":
                    UI.printMenu()

                elif command == "1":
                    s = UI.readStudent()
                    self._controller.addStudent(s)

                elif command == "2":
                    while True:
                        try:
                            oldID = int(input("Enter the ID of the student whose information you want to modify:"))
                            break
                        except ValueError:
                            print("Student's ID must be a natural number!")

                    print("\tNew student:")
                    s = UI.readStudent()
                    self._controller.updateStudent(oldID, s)

                elif command == "3":
                    while True:
                        try:
                            id = int(input("Student's ID:"))
                            break
                        except ValueError:
                            print("Student's ID must be a natural number!")
                    self._controller.removeStudentByID(id)
                    self._controller.removeStudFromGrades(id)

                elif command == "4":
                    self._controller.removeAllStudents()

                elif command == "5":
                    while True:
                        try:
                            id = int(input("\nID of the student you want to find:"))
                            if id >= 0:
                                break
                            else:
                                print("\tStudent's ID must be a natural number!\n")
                        except ValueError:
                            print("\tStudent's ID must be a natural number!\n")

                    print(self._controller.printStudByID(id))

                elif command == "6":
                    name = str(input("Student's name:"))
                    while len(name) == 0:
                        print("\tNo name introduced\n")
                        name = str(input("Student's name:"))
                    name = name.lower()
                    print(self._controller.printStudByName(name))

                elif command == "7":
                    print(self._controller.printAll())


                    # ---------------------------------------------------------------

                elif command == "8":
                    d = UI.readDiscipline()
                    self._controller.addDiscipline(d)

                elif command == "9":
                    while True:
                        try:
                            oldID = int(
                                input("Enter the ID of the dsicipline whose information you want to modify:"))
                            break
                        except ValueError:
                            print("ID of the discipline must be a natural number!")

                    print("\tNew discipline:")
                    s = UI.readDiscipline()
                    self._controller.updateDiscipline(oldID, s)

                elif command == "10":
                    while True:
                        try:
                            id = int(input("Discipline's ID:"))
                            break
                        except ValueError:
                            print("Discipline's ID must be a natural number!")
                    self._controller.removeDisciplineByID(id)

                elif command == "11":
                    self._controller.removeAllDisciplines()



                elif command == "12":
                    while True:
                        try:
                            id = int(input("ID of the discipline:"))
                            if id >= 0:
                                break
                            else:
                                print("\tStudent's ID must be a natural number!\n")
                        except ValueError:
                            print("\tID of the discipline must be a natural number!\n")
                    print(self._controller.printDisByID(id))

                elif command == "13":
                    name = str(input("Name of the discipline:"))
                    while len(name) == 0:
                        print("\tNo name introduced\n")
                        name = str(input("Name of the discipline:"))
                    name = name.lower()
                    print(self._controller.printDisByName(name))


                elif command == "14":
                    print(self._controller.printAllDis())

                    # ---------------------------------------------------------------

                elif command == "15":
                    grade=UI.readGrade(self._controller)
                    self._controller.addGrade(grade)

                elif command == "16":
                    while True:
                        try:
                            id = int(input("\nStudent's ID:"))
                            if id >= 0:
                                break
                            else:
                                print("\tStudent's ID must be a natural number!\n")
                        except ValueError:
                            print("\tStudent's ID must be a natural number!\n")


                    while True:
                        try:
                            id1 = int(input("ID of the discipline:"))
                            if id1 >= 0:
                                break
                            else:
                                print("\tStudent's ID must be a natural number!\n")
                        except ValueError:
                            print("\tID of the discipline must be a natural number!\n")

                    self._controller.removeGrade(id,id1)

                elif command == "17":
                    #x = self._controller.getAllStudents()
                    #y = self._controller.getAllDisciplines()
                    print(self._controller.printGrades())

                elif command == "18":

                    while True:
                        try:
                            id = int(input("ID of the discipline:"))
                            if id >= 0:
                                break
                            else:
                                print("\tStudent's ID must be a natural number!\n")
                        except ValueError:
                            print("\tID of the discipline must be a natural number!\n")
                    print()
                    while True:
                        try:
                            printMode = int(input(
                                "\t 1-to print the students alphabetically\n\t 2-to print the students sorted by average grade \n Please choose between 1 and 2:"))
                            if printMode != 1 and printMode != 2:
                                print("Invalid option.Please choose between 1 and 2\n")
                            else:
                                break
                        except:
                            print("Invalid option.Please choose between 1 and 2\n")

                    lista=self._controller.printEnrolled(id, printMode)
                    print("Discipline: "+str(lista[0][0]),end="")
                    for cr in self._controller.printEnrolled(id, printMode):
                        print("\t"+str(cr[1]))

                elif command == "19":
                    print("Students:\n")
                    for cr in self._controller.fail():
                        print(cr)
                    #print(self._controller.fail())

                elif command == "20":
                    print("Students:\n")
                    for cr in self._controller.bestStud():
                        print(cr)

                elif command == "21":
                    if len(self._controller.allDisciplines())!=0:
                        print("Disciplines:\n")
                        for cr in self._controller.allDisciplines():
                            print(cr)
                    else:
                        print("\n\tThere are no grades!")

                    #print(self._controller.allDisciplines())

                elif command=="22":
                    ok=self._undo.undo()
                    if ok==False:
                        print("\n\tNothing to undo!")
                    else:
                        print("\n\tUndo done successfully!")

                elif command=="23":
                    ok=self._undo.redo()
                    if ok==False:
                        print("\n\tNothing to redo!")
                    else:
                        print("\n\tRedo done successfully!")

                else:
                    print("\tInvalid command!")

            except Exception as exc:
                print("Error encountered - " + str(exc))

    def readStudent():
        """
        Reads a student.(ID, NAME , LIST WITH THE DISCIPLINES AT WHICH THE STUDENT IS ENROLLED)
        The final information of a student is always correct.The user is asked to introduce a correct information, it the previous one was invalid.
        Input:  -
        Output: The student object.
        """
        while True:
            try:
                id = int(input("\nStudent's ID:"))
                if id >=0:
                    break
                else:
                    print("\tStudent's ID must be a natural number!\n")
            except ValueError:
                print("\tStudent's ID must be a natural number!\n")

        name = str(input("Student's name:"))
        while len(name)==0:
            print("\tNo name introduced\n")
            name = str(input("Student's name:"))


        print("\nType -1 to see the available disciplines.Type 0 to confirm.")
        grades = []
        g=1
        while g!=0:
            try:
                g = int(input("Enter the id of the discipline:"))
                if g in grades:
                    print("\tDiscipline ID already added!\n")
                elif g!=0 :
                    grades.append(g)
            except ValueError:
                print("\tThe ID of a discipline must be a natural number\n")

        s = student(id, name, grades)
        return s

    def readDiscipline():
        """
        Reads a discipline.(ID, NAME)
        The final information of a discipline is always correct.The user is asked to introduce a correct information, it the previous one was invalid.
        Input:  -
        Output: The discipline object.
        """
        while True:
            try:
                id = int(input("ID of the discipline:"))
                if id >=0:
                    break
                else:
                    print("\tStudent's ID must be a natural number!\n")
            except ValueError:
                print("\tID of the discipline must be a natural number!\n")

        name = str(input("Name of the discipline:"))
        while len(name)==0:
            print("\tNo name introduced\n")
            name = str(input("Name of the discipline:"))


        d = discipline(id, name)
        return d

    def readGrade(controller):
        """
        Reads a grade.(student id, discipline id , list of grades)
        The final information of a grade is always correct.The user is asked to introduce a correct information, it the previous one was invalid.
        Input:  -
        Output: The grade object.
        """
        print()
        while True:
            try:
                id = int(input("Student's ID:"))
                if id >=0:
                    break
                else:
                    print("\tStudent's ID must be a natural number!\n")
            except ValueError:
                print("\tStudent's ID must be a natural number!\n")

        while True:
            try:
                id1 = int(input("ID of the discipline:"))
                if id1 >=0:
                    break
                else:
                    print("\tID of the discipline must be a natural number!\n")
            except ValueError:
                print("\tID of the discipline must be a natural number!\n")

        while True:
            try:
                studGrade = int(input("Enter a grade:"))
                if studGrade<1 or studGrade>10:
                    print("\tThe grade must be natural number between 1 and 10!\n")
                else:
                    break
            except ValueError:
                print("\tThe grade discipline must be a natural number between 1 and 10\n")

        g=grade(controller.getStud(id),controller.getDis(id1),studGrade)
        return g

