from filters import passes
from func import runs
from stack import CodeStack, FrameStack
from helper import debuging,log

# debuging = True


def main(programFile: str = "example.cvm"):
    with open(programFile, "r") as file:
        code: str = file.read()

    for filter in passes:
        log(filter[1])
        code = filter[0](code)

    CodeStack.extend(code[::-1])

    while len(CodeStack):
        token = CodeStack.pop()
        log("token: ", token)
        if not runs(token):
            FrameStack.append(token)
        log("stack:", FrameStack)
