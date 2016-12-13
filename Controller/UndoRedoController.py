from Lab3.Repository.ExceptionRepo import *
class UndoController:
    """
    class used for undo/redo
    """
    def __init__(self):
        """
        constructor
        """
        self._operations = []
        self._index = -1
        self._recorded = True

    def recordOperation(self, operation):
        """
        funsction used for recording an operation in the list of operations
        """
        if self.isRecorded() == True:
            self._operations[-1].append(operation)

    def newOperation(self):
        if self.isRecorded() == False:
            return

        self._operations = self._operations[0:self._index + 1]
        self._operations.append([])
        self._index += 1

    def isRecorded(self):
        return self._recorded

    def undo(self):
        """
        function used for undo
        :return:
        """
        if self._index < 0:
            return False

        self._recorded = False

        for oper in self._operations[self._index]:
            oper.undo()

        self._recorded = True

        self._index -= 1
        return True

    def redo(self):
        """
        function used for undo
        :return:
        """
        if self._index >= (len(self._operations)-1):
            return False

        self._index += 1
        self._recorded = False

        for oper in self._operations[self._index]:
            oper.redo()

        self._recorded = True
        return True

class FunctionCall:
    """
    class used for calling a function
    """
    def __init__(self, functionRef, *parameters):
        """
        constructor
        """
        self._functionRef = functionRef
        self._parameters = parameters

    def call(self):
        """
        calling a function
        :return:
        """
        self._functionRef(*self._parameters)

class Operation:
    """
    class used for an operation
    """
    def __init__(self, functionDo, functionUndo):
        """
        constructor
        :param functionDo:
        :param functionUndo:
        """
        self._functionDo = functionDo
        self._functionUndo = functionUndo

    def undo(self):
        """
        calling the function for undo
        :return:
        """
        self._functionUndo.call()

    def redo(self):
        """
        calling the function for redo
        :return:
        """
        self._functionDo.call()
