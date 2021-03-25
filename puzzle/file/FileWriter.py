from puzzle.enum.Move import Move


# TODO: ADD UNRESOLVED CASE

class FileWriter(object):

    @staticmethod
    def writeFile(filePath, state) -> list:
        arr = []
        arr = FileWriter.getPreviousStepsFromFinalState(state, arr)
        with open(filePath, mode='w') as file:
            file.write(state.getEpoch() + "\n")
            file.write(FileWriter.listToString(arr[::-1]))
        return arr

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
        str1 = " "
        return str1.join(s)
