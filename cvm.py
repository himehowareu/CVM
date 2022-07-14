import argparse
from filters import passes
from frames import frameData
from func import runToken
import Data
from helper import log, debugCommand


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

    Data.stacks[Data.Stack.Code].extend(code[::-1])


def runFile(programFile: str = "example.cvm"):
    """
    Takes a file to parse, filters and then runs the code

    :param programFile: The file to run, defaults to example.cvm
    :type programFile: str (optional)
    """
    loadFile(programFile)

    Data.FrameStack = []

    while len(Data.stacks[Data.Stack.Code]):
        token = Data.stacks[Data.Stack.Code].pop()
        log("token: ", token)
        runToken(token)

    if len(Data.stacks[Data.Stack.Frame]):
        print("Stack not empty: unused value")


parser = argparse.ArgumentParser(prog="CVM", description="CVM programing language")
parser.add_argument("file", help="the program you want to run", default="test.cvm")
# parser.add_argument(
#     "-command", metavar="c", nargs="+", help="run some commands from a string"
# )
args = parser.parse_args()

if __name__ == "__main__":
    # debugCommand("!help")
    runFile(args.file)
