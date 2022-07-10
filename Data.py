from frames import Frame
from helper import log

CodeStack: list[str] = []
FrameStack: list[Frame] = []
FunctionStack: list[str] = []
CallData: dict[str, list[str]] = {}


def matchArgs(args: list[Frame]) -> bool:
    for x, arg in enumerate(args[::-1]):
        fData = FrameStack[-(x + 1)]
        if not arg.matches(fData):
            log("argument type %s deosnt match stack type %s" % (arg, fData))
            return False
    return True
