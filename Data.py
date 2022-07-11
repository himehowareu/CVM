from frames import Frame
from helper import log

CodeStack: list[str] = []
FrameStack: list[Frame] = []
FunctionStack: list[str] = []
CallData: dict[str, list[str]] = {}


def matchArgs(args: list[Frame]) -> bool:
    """
    this takes the list of arguments of the function
    and checks if the type are the same as the ones
    on the top of the stack

    :param args: list[Frame]
    :type args: list[Frame]
    :return: The return value is a tuple of the function and the number of arguments.
    """
    for x, arg in enumerate(args[::-1]):
        fData: Frame = FrameStack[-(x + 1)]
        if not arg.matches(fData):
            log("argument type %s deosnt match stack type %s" % (arg, fData))
            return False
    return True
