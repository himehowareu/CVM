from filters import passes
from frames import frameData
from func import runs
import Data
from helper import log, debugCommand


def main(programFile: str = "example.cvm"):
    """
    Takes a file to parse, filters and then runs the code

    :param programFile: The file to run, defaults to example.cvm
    :type programFile: str (optional)
    """
    with open(programFile, "r") as file:
        code: str = file.read()

    for filter in passes:
        log(filter[1])
        code = filter[0](code)

    Data.CodeStack.extend(code[::-1])
    Data.FunctionStack = []

    while len(Data.CodeStack):
        # debugCommand("!dump")
        token = Data.CodeStack.pop()
        log("token: ", token)
        if token.startswith("!"):
            debugCommand(token)
            continue
        if not runs(token):
            data = frameData(token)
            Data.FrameStack.append(data)

        log("stack:", Data.FrameStack)

    if len(Data.FrameStack):
        print("Stack not empty: unused value")


if __name__ == "__main__":
    main("test.cvm")
