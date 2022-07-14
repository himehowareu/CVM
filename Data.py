from frames import Frame
from helper import log
from enum import Enum

class Stack(Enum):
    Code=0
    Frame=1
    a=2
    b=3
    c=4
    d=5
    e=6
    f=7


CodeStack: list[str] = []
FrameStack: list[Frame] = []
FunctionStack: list[str] = []
CallData: dict[str, list[str]] = {}

stacks:dict[Stack,list]={
Stack.Code:CodeStack,
Stack.Frame:FrameStack,
Stack.a:[],
Stack.b:[],
Stack.c:[],
Stack.d:[],
Stack.e:[],
Stack.f:[]
}

def matchArgs(args: list[Frame]) -> bool:
    """
    this takes the list of arguments of the function
    and checks if the type are the same as the ones
    on the top of the stack

    :param args: list[Frame]
    :type args: list[Frame]
    :return: The return value is a tuple of the function and the number of arguments.
    """
    global stacks
    for x, arg in enumerate(args[::-1]):
        fData: Frame = stacks[Stack.Frame][-(x + 1)]
        if not arg.matches(fData):
            log("argument type %s doesn't match stack type %s" % (arg, fData))
            return False
    return True
