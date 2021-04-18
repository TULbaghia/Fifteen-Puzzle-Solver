from puzzle.enum.Move import Move


from puzzle.model.Result import Result


class FileWriter(object):

    @staticmethod
    def saveSolution(filePath, result: Result):
        state = result.finalState
        if state is None:
            FileWriter.writeUnsolvedPuzzles(filePath, '-1')
            return
        arr = []
        arr = FileWriter.getPreviousStepsFromFinalState(state, arr)
        with open(filePath, mode='w') as file:
            file.write(str(state.epoch) + "\n")
            file.write(FileWriter.listToString(arr[::-1]))

    @staticmethod
    def saveStats(filePath, result: Result, timeInMillis):
        state = result.finalState
        if state is None:
            FileWriter.writeUnsolvedPuzzles(filePath, '-1')
        else:
            FileWriter.writeUnsolvedPuzzles(filePath, str(state.epoch))
        with open(filePath, mode='a') as file:
            file.write(str(result.numberOfVisitedStates) + "\n")
            file.write(str(result.getNumberOfProcessedStates()) + "\n")
            file.write(str(result.maxDepth) + "\n")
            file.write(str(timeInMillis))

    @staticmethod
    def writeUnsolvedPuzzles(filePath: str, contentToWrite: str):
        with open(filePath, mode='w') as file:
            file.write(contentToWrite + "\n")

    @staticmethod
    def getPreviousStepsFromFinalState(state, arr: list) -> list:
        if state.parent is not None:
            arr.append(FileWriter.getAcronymFromEnum(state.previousStep))
            FileWriter.getPreviousStepsFromFinalState(state.parent, arr)
        return arr

    @staticmethod
    def getAcronymFromEnum(enum: Move) -> str:
        return {
            enum.UP: 'U',
            enum.DOWN: 'D',
            enum.LEFT: 'L',
            enum.RIGHT: 'R'
        }[enum]

    @staticmethod
    def listToString(s) -> str:
        str1 = ""
        return str1.join(s)
