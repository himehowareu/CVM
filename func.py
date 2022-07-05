from tempfile import TemporaryDirectory
from typing import Callable
from frames import *
import Data
from helper import command
import helper

functions: list[tuple[str, int, Callable]] = []


def runs(token: str) -> bool:
    for fun in functions:
        if token == fun[0]:
            if len(Data.FrameStack) >= fun[1]:
                if fun[2]():
                    exit("Error while parsestring tokens")
                return True
            else:
                print("Error on token: " + token)
                exit("FrameStack was not sett up correctly")
    return False


def addCommand(name, args):
    def dec(func):
        global functions
        command = (name, args, func)
        functions.append(command)
        return func

    return dec


@addCommand("print", 1)
def print_():
    print(Data.FrameStack.pop(), end="")


@addCommand("println", 1)
def print_newline():
    print(Data.FrameStack.pop())


@addCommand("input", 0)
def input_():
    Data.FrameStack.push(F_String(input()))


@addCommand("add", 2)
def add_():
    a = Data.FrameStack.pop()
    b = Data.FrameStack.pop()
    if a.type == b.type:
        Data.FrameStack.push(a.__class__(a.value + b.value))


@addCommand("min", 2)
def min_():
    a = Data.FrameStack.pop()
    b = Data.FrameStack.pop()
    if a.type == b.type:
        Data.FrameStack.push(a.__class__(a.value - b.value))


@addCommand("clone", 1)
def clone():
    a = Data.FrameStack.pop()
    Data.FrameStack.push(a)
    Data.FrameStack.push(a)


@addCommand("swap", 1)
def swap():
    a = Data.FrameStack.pop()
    if a.type == "Integer":
        b = Data.FrameStack.pop()
        c = Data.FrameStack[-a.value]
        Data.FrameStack[-a.value] = b
        Data.FrameStack.push(c)
    else:
        return True


@addCommand("EQ", 2)
def EQ():
    a = Data.FrameStack.pop()
    b = Data.FrameStack.pop()
    Data.FrameStack.push(a.__class__(a.value == b.value))


@addCommand("LT", 2)
def LT():
    a = Data.FrameStack.pop()
    b = Data.FrameStack.pop()
    Data.FrameStack.push(a.__class__(a.value < b.value))


@addCommand("GT", 2)
def GT():
    a = Data.FrameStack.pop()
    b = Data.FrameStack.pop()
    Data.FrameStack.push(a.__class__(a.value > b.value))


@addCommand("NT", 2)
def NT():
    a = Data.FrameStack.pop()
    b = Data.FrameStack.pop()
    Data.FrameStack.push(a.__class__(a.value != b.value))


@addCommand("True", 0)
def True_():
    Data.FrameStack.push(F_Integer(1))


@addCommand("False", 0)
def False_():
    Data.FrameStack.push(F_Integer(0))


@addCommand("drop", 0)
def drop():
    Data.FrameStack.pop()


@addCommand("dropx", 1)
def dropx():
    x: int = Data.FrameStack.pop().value
    Data.FrameStack = Data.FrameStack[:x]


@addCommand("if", 1)
def if_():
    helper.getTokensTill("endIf")

    if Data.FrameStack.pop().value > 0:
        Data.CodeStack.extend(Data.FunctionStack)
    Data.FunctionStack = []


@addCommand("stackSize", 0)
def stackSize():
    Data.FrameStack.append(str(len(Data.FrameStack)))


@addCommand("def", 0)
def FuncDef():
    name: str = Data.CodeStack.pop()
    helper.getTokensTill("endDef")
    Data.CallData[name] = Data.FunctionStack.copy()
    Data.FunctionStack = []


@addCommand("func", 0)
def runFunc():
    name: str = Data.CodeStack.pop()
    code: list[str] = Data.CallData[name]
    Data.CodeStack.extend(code)


@addCommand("loop", 0)
def loop():
    helper.getTokensTill("do")
    setup: list[str] = Data.FunctionStack[::-1]
    Data.FunctionStack = []
    helper.getTokensTill("endLoop")
    code: list[str] = Data.FunctionStack[::-1]
    Data.FunctionStack = []
    temp = (
        [
            "def",
            "loop",
        ]
        + setup
        + [
            "if",
        ]
        + code
        + ["func", "loop", "endIf", "endDef", "func", "loop"]
    )
    Data.CodeStack.extend(temp[::-1])
