from collections import namedtuple
from typing import Callable
from frames import *
import Data
from helper import debugCommand
import helper

command: tuple[str, list[Frame], list[Frame], Callable, str] = namedtuple(
    "command", ["name", "args", "returns", "func", "doc"]
)

functions: list[command] = []


def runs(token: str) -> bool:
    for fun in functions:
        if token == fun.name:
            if len(Data.FrameStack) >= len(fun.args):
                if Data.matchArgs(fun.args):
                    if fun.func():
                        exit("Error while parsestring tokens")
                    return True
                else:
                    print("match error")
                    print(token)
                    exit("stack setup error")
            else:
                print("Error on token: " + token)
                exit("FrameStack was not sett up correctly")
    return False


def addCommand(name, args=[], returns=[]):
    def dec(func):
        global functions
        newCommand = command(name, args, returns, func, func.__doc__)
        functions.append(newCommand)
        return func

    return dec


@addCommand("print", [F_String])
def print_():
    """prints out the top of the stack"""
    print(Data.FrameStack.pop().value, end="")


@addCommand("println", [F_String])
def print_newline():
    """prints out the top of the stack with a new line"""
    print(Data.FrameStack.pop().value)


@addCommand("string", [F_Integer], [F_String])
def string_():
    """convert int to string on the top of the stack"""
    temp: F_Integer = Data.FrameStack.pop()
    temp: str = str(temp.value)
    temp: F_String = F_String(temp)
    Data.FrameStack.append(temp)


@addCommand("input", [])
def input_():
    """gets user input and stores it on top of the stack"""
    Data.FrameStack.append(F_String(input()))


@addCommand("add", [F_Integer, F_Integer], [F_Integer])
def add_():
    """adds the top two ints and stores on top of stack"""
    a = Data.FrameStack.pop()
    b = Data.FrameStack.pop()
    if a.type == b.type:
        Data.FrameStack.append(a.__class__(a.value + b.value))


@addCommand("min", [F_Integer, F_Integer], [F_Integer])
def min_():
    a = Data.FrameStack.pop()
    b = Data.FrameStack.pop()
    if a.type == b.type:
        Data.FrameStack.append(a.__class__(a.value - b.value))


@addCommand("clone", [F_any], [F_any])
def clone():
    a = Data.FrameStack.pop()
    Data.FrameStack.append(a)
    Data.FrameStack.append(a)


@addCommand("swap", [F_Integer])
def swap():
    a = Data.FrameStack.pop()
    if a.type == "Integer":
        b = Data.FrameStack.pop()
        c = Data.FrameStack[-a.value]
        Data.FrameStack[-a.value] = b
        Data.FrameStack.append(c)
    else:
        return True


@addCommand("EQ", [F_Integer, F_Integer], [F_any])
def EQ():
    a = Data.FrameStack.pop()
    b = Data.FrameStack.pop()
    Data.FrameStack.append(a.__class__(a.value == b.value))


@addCommand("LT", [F_Integer, F_Integer], [F_any])
def LT():
    a = Data.FrameStack.pop()
    b = Data.FrameStack.pop()
    Data.FrameStack.append(a.__class__(a.value < b.value))


@addCommand("GT", [F_Integer, F_Integer], [F_any])
def GT():
    a = Data.FrameStack.pop()
    b = Data.FrameStack.pop()
    Data.FrameStack.append(F_Boolean(a.value > b.value))


@addCommand("NT", [F_Integer, F_Integer], [F_any])
def NT():
    a = Data.FrameStack.pop()
    b = Data.FrameStack.pop()
    Data.FrameStack.append(a.__class__(a.value != b.value))


@addCommand("True", [], [F_any])
def True_():
    Data.FrameStack.append(F_Integer(1))


@addCommand("False", [], [F_any])
def False_():
    Data.FrameStack.append(F_Integer(0))


@addCommand("drop")
def drop():
    Data.FrameStack.pop()


@addCommand("dropx", [F_Integer])
def dropx():
    x: int = Data.FrameStack.pop().value
    Data.FrameStack = Data.FrameStack[:x]


@addCommand("if", [F_Boolean])
def if_():
    helper.getTokensTill("endIf")
    if Data.FrameStack.pop().value > 0:
        Data.CodeStack.extend(Data.FunctionStack)
    Data.FunctionStack = []


@addCommand("stackSize", [], [F_Integer])
def stackSize():
    size: int = len(Data.FrameStack)
    size: F_Integer = F_Integer(size)
    Data.FrameStack.append(size)


@addCommand("def")
def FuncDef():
    name: str = Data.CodeStack.pop()
    helper.getTokensTill("endDef")
    Data.CallData[name] = Data.FunctionStack.copy()
    Data.FunctionStack = []


@addCommand("func")
def runFunc():
    name: str = Data.CodeStack.pop()
    code: list[str] = Data.CallData[name]
    Data.CodeStack.extend(code)


@addCommand("loop")
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
