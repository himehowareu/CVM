from filters import passes
from func import runs
from stack import CodeStack, FrameStack

compileText :bool = False
debug :bool = False


with open("example.cvm", "r") as file:
    code :str = file.read()

for filter in passes:
    if compileText:
        print(filter[1])
    code = filter[0](code)

CodeStack.extend(code[::-1])

while len(CodeStack):
    token=CodeStack.pop()
    if debug:
        print("token: ", token)
    if not runs(token):
        FrameStack.append(token)
    if debug:
        print("stack:", FrameStack)
