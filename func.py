from typing import Callable
from stack import FrameStack
from frames import *


functions: list[tuple[str, int, Callable]] = []


def runs(token: str) -> bool:
    for fun in functions:
        if token == fun[0]:
            if len(FrameStack) >= fun[1]:
                if fun[2]():
                    exit("Error while parsestring tokens")
                return True
            else:
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
    print(FrameStack.pop(), end="")


@addCommand("println", 1)
def print_newline():
    print(FrameStack.pop())


@addCommand("input", 0)
def input_():
    FrameStack.push(F_String(input()))


@addCommand("add", 2)
def add_():
    a = FrameStack.pop()
    b = FrameStack.pop()
    if a.type == b.type:
        FrameStack.push(a.__class__(a.value + b.value))


@addCommand("min", 2)
def min_():
    a = FrameStack.pop()
    b = FrameStack.pop()
    if a.type == b.type:
        FrameStack.push(a.__class__(a.value - b.value))


@addCommand("clone", 1)
def clone():
    a = FrameStack.pop()
    FrameStack.push(a)
    FrameStack.push(a)


@addCommand("swap", 1)
def swap():
    a = FrameStack.pop()
    if a.type == "Integer":
        b = FrameStack.pop()
        c = FrameStack[-a.value]
        FrameStack[-a.value] = b
        FrameStack.push(c)
    else:
        return True


@addCommand("EQ", 2)
def EQ():
    a = FrameStack.pop()
    b = FrameStack.pop()
    FrameStack.push(a.__class__(a.value == b.value))


@addCommand("LT", 2)
def LT():
    a = FrameStack.pop()
    b = FrameStack.pop()
    FrameStack.push(a.__class__(a.value < b.value))


@addCommand("GT", 2)
def GT():
    a = FrameStack.pop()
    b = FrameStack.pop()
    FrameStack.push(a.__class__(a.value > b.value))


@addCommand("NT", 2)
def NT():
    a = FrameStack.pop()
    b = FrameStack.pop()
    FrameStack.push(a.__class__(a.value != b.value))


@addCommand("True", 0)
def True_():
    FrameStack.push(F_Integer(1))


@addCommand("False", 0)
def False_():
    FrameStack.push(F_Integer(0))


@addCommand("drop", 0)
def drop():
    FrameStack.pop()


@addCommand("dropx", 1)
def dropx():
    x: int = FrameStack.pop().value
    FrameStack = FrameStack[:x]
