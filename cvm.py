from pprint import pprint
from filters import passes
from func import runs
import Data
from helper import debuging, log, command

# debuging = True


def main(programFile: str = "example.cvm"):
    with open(programFile, "r") as file:
        code: str = file.read()

    for filter in passes:
        log(filter[1])
        code = filter[0](code)

    Data.CodeStack.extend(code[::-1])
    Data.FunctionStack = []

    while len(Data.CodeStack):
        token = Data.CodeStack.pop()
        log("token: ", token)
        if token.startswith("!"):
            command(token)
            continue
        if not runs(token):
            Data.FrameStack.append(token)
        log("stack:", Data.FrameStack)

    if len(Data.FrameStack):
        print("Stack not empty: unused value")


if __name__ == "__main__":
    main("test.cvm")
