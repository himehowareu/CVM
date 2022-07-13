import argparse
from filters import passes
from frames import frameData
from func import runs
import Data
from helper import log, debugCommand


def runToken(token: str):
    if token.startswith("!"):
        debugCommand(token)
    elif not runs(token):
        data = frameData(token)
        Data.FrameStack.append(data)


def loadFile(fileName: str):
    """
    Takes a file to parse, filters and load to the stack

    :param fileName: The file to load
    :type fileName: str (optional)
    """
    with open(fileName, "r") as file:
        code: str = file.read()

    for filter in passes:
        log(filter[1])
        code = filter[0](code)

    Data.CodeStack.extend(code[::-1])


def runFile(programFile: str = "example.cvm"):
    """
    Takes a file to parse, filters and then runs the code

    :param programFile: The file to run, defaults to example.cvm
    :type programFile: str (optional)
    """
    loadFile(programFile)

    Data.FunctionStack = []

    while len(Data.CodeStack):
        token = Data.CodeStack.pop()
        log("token: ", token)
        runToken(token)

    if len(Data.FrameStack):
        print("Stack not empty: unused value")


parser = argparse.ArgumentParser(prog="CVM", description="CVM programing language")
parser.add_argument("file", help="the program you want to run", default="test.cvm")
# parser.add_argument(
#     "-command", metavar="c", nargs="+", help="run some commands from a string"
# )
args = parser.parse_args()

if __name__ == "__main__":
    runFile(args.file)
