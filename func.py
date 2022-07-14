from collections import namedtuple
from ipaddress import AddressValueError
from locale import DAY_1
import os
from typing import Callable
from typing_extensions import runtime
from frames import *
import Data
import helper

command: tuple[str, list[Frame], Callable, str] = namedtuple(
    "command", ["name", "args", "func", "doc"]
)

functions: list[command] = []


def runs(token: str) -> bool:
    for fun in functions:
        if token == fun.name:
            if len(Data.stacks[Data.Stack.Frame]) >= len(fun.args):
                if Data.matchArgs(fun.args):
                    fun.func()
                    return True
                else:
                    print("match error")
                    print(token)
                    exit("stack setup error")
            else:
                print("Error on token: " + token)
                exit("FrameStack was not sett up correctly")
    return False


def runToken(token: str):
    if token.startswith("!"):
        helper.debugCommand(token)
    elif not runs(token):
        data = frameData(token)
        Data.stacks[Data.Stack.Frame].append(data)


def addCommand(name, args=[]):
    def dec(func):
        global functions
        newCommand = command(name, args, func, func.__doc__)
        functions.append(newCommand)
        return func

    return dec


@addCommand("print", [F_String])
def print_():
    """prints out the top of the stack"""
    print(Data.stacks[Data.Stack.Frame].pop().value, end="")


@addCommand("println", [F_String])
def print_newline():
    """prints out the top of the stack with a new line"""
    print(Data.stacks[Data.Stack.Frame].pop().value)


@addCommand("string", [F_Integer])
def string_():
    """convert int to string on the top of the stack"""
    temp: F_Integer = Data.stacks[Data.Stack.Frame].pop()
    temp: str = str(temp.value)
    temp: F_String = F_String(temp)
    Data.stacks[Data.Stack.Frame].append(temp)


@addCommand("input", [])
def input_():
    """gets user input and stores it on top of the stack"""
    Data.stacks[Data.Stack.Frame].append(F_String(input()))


@addCommand("add", [F_Integer, F_Integer])
def add_():
    """adds the top two ints and stores on top of stack"""
    a: F_Integer = Data.stacks[Data.Stack.Frame].pop()
    b: F_Integer = Data.stacks[Data.Stack.Frame].pop()
    Data.stacks[Data.Stack.Frame].append(F_Integer(a.value + b.value))


@addCommand("min", [F_Integer, F_Integer])
def min_():
    """subtracts the top two numbers"""
    a: F_Integer = Data.stacks[Data.Stack.Frame].pop()
    b: F_Integer = Data.stacks[Data.Stack.Frame].pop()
    Data.stacks[Data.Stack.Frame].append(F_Integer(a.value - b.value))


@addCommand("clone", [F_any])
def clone():
    """duplicates the top of the stack"""
    a: Frame = Data.stacks[Data.Stack.Frame].pop()
    Data.stacks[Data.Stack.Frame].append(a)
    Data.stacks[Data.Stack.Frame].append(a)


@addCommand("clonex", [F_Integer])
def cloneX():
    """clone multiple items on the stack"""
    a: F_Integer = Data.stacks[Data.Stack.Frame].pop()
    temp: list[F_any] = Data.stacks[Data.Stack.Frame][-a.value :]
    Data.stacks[Data.Stack.Frame].extend(temp)


@addCommand("swap", [F_Integer])
def swap():
    """takes the second frame and swaps it with index from the top of the stack"""
    a: F_Integer = Data.stacks[Data.Stack.Frame].pop()
    b: Frame = Data.stacks[Data.Stack.Frame].pop()
    c: Frame = Data.stacks[Data.Stack.Frame][-a.value]
    Data.stacks[Data.Stack.Frame][-a.value] = b
    Data.stacks[Data.Stack.Frame].append(c)


@addCommand("EQ", [F_Integer, F_Integer])
def EQ():
    """tests that the top two values are equal puts a non zero value on the stack"""
    a: F_Integer = Data.stacks[Data.Stack.Frame].pop()
    b: F_Integer = Data.stacks[Data.Stack.Frame].pop()
    Data.stacks[Data.Stack.Frame].append(F_Boolean(a.value == b.value))


@addCommand("LT", [F_Integer, F_Integer])
def LT():
    """tests that the top two values are less then puts a non zero value on the stack"""
    a: F_Integer = Data.stacks[Data.Stack.Frame].pop()
    b: F_Integer = Data.stacks[Data.Stack.Frame].pop()
    Data.stacks[Data.Stack.Frame].append(F_Boolean(a.value < b.value))


@addCommand("GT", [F_Integer, F_Integer])
def GT():
    """tests that the top two values are grater then puts a non zero value on the stack"""
    a: F_Integer = Data.stacks[Data.Stack.Frame].pop()
    b: F_Integer = Data.stacks[Data.Stack.Frame].pop()
    Data.stacks[Data.Stack.Frame].append(F_Boolean(a.value > b.value))


@addCommand("NT", [F_Integer, F_Integer])
def NT():
    """tests that the top two values are not equal puts a non zero value on the stack"""
    a: F_Integer = Data.stacks[Data.Stack.Frame].pop()
    b: F_Integer = Data.stacks[Data.Stack.Frame].pop()
    Data.stacks[Data.Stack.Frame].append(F_Boolean(a.value != b.value))


@addCommand("True")
def True_():
    """puts a non zerp ( True) value on the stack"""
    Data.stacks[Data.Stack.Frame].append(F_Boolean(True))


@addCommand("False")
def False_():
    """puts a zero value (false) on the stack"""
    Data.stacks[Data.Stack.Frame].append(F_Boolean(0))


@addCommand("drop")
def drop():
    """pops off the top of the stack"""
    Data.stacks[Data.Stack.Frame].pop()


@addCommand("dropx", [F_Integer])
def dropx():
    """pops off the x frames off the stack"""
    x: int = Data.stacks[Data.Stack.Frame].pop().value
    Data.stacks[Data.Stack.Frame] = Data.stacks[Data.Stack.Frame][:x]


@addCommand("if", [F_Boolean])
def if_():
    """if the top of the stack is a non zero number if true the code between the if and endif will run"""
    helper.getTokensTill("endIf")
    if Data.stacks[Data.Stack.Frame].pop().value > 0:
        Data.stacks[Data.Stack.Code].extend(Data.FunctionStack)
    Data.stacks[Data.Stack.Function] = []


@addCommand("stackSize")
def stackSize():
    """puts the size of the stack on top of the stack"""
    size: int = len(Data.stacks[Data.Stack.Frame])
    size: F_Integer = F_Integer(size)
    Data.stacks[Data.Stack.Frame].append(size)


@addCommand("sysCall", [F_String])
def sysCall():
    command: str = Data.stacks[Data.Stack.Frame].pop().value
    returnCode: int = os.system(command)


@addCommand("def")
def FuncDef():
    """defines a functions with the next token as the name and the following tokens till endDef as the code"""
    name: str = Data.stacks[Data.Stack.Code].pop()
    helper.getTokensTill("endDef")
    Data.CallData[name] = Data.FunctionStack.copy()
    Data.FunctionStack = []


@addCommand("func")
def runFunc():
    """runs the function that is named after it"""
    name: str = Data.stacks[Data.Stack.Code].pop()
    code: list[str] = Data.CallData[name]
    Data.stacks[Data.Stack.Code].extend(code)


@addCommand("loop")
def loop():
    """this will start a loop"""
    helper.getTokensTill("do")
    setup: list[str] = Data.FunctionStack[::-1]
    Data.FunctionStack = []
    helper.getTokensTill("endLoop")
    code: list[str] = Data.FunctionStack[::-1]
    Data.FunctionStack = []
    while True:
        for token in setup:
            runToken(token)
        if Data.stacks[Data.Stack.Frame].pop().value > 0:
            for token in code:
                runToken(token)
        else:
            break


@addCommand("endIf")
@addCommand("endDef")
@addCommand("endLoop")
def error():
    """These should never be called,they should be handled by the opening call"""
    exit("error")


@addCommand("swapStack", [F_Integer, F_Integer])
def swapStack():
    """swaps two stacks"""
    a: F_Integer = Data.stacks[Data.Stack.Frame].pop()
    b: F_Integer = Data.stacks[Data.Stack.Frame].pop()
    temp1 = Data.stacks[Data.Stack[a.value]]
    temp2 = Data.stacks[Data.Stack[b.value]]
    Data.stacks[Data.Stack[a.value]] = temp2
    Data.stacks[Data.Stack[b.value]] = temp1


@addCommand("cloneStack", [F_Integer, F_Integer])
def cloneStack():
    """clone one stack to another stacks (from to)"""
    a: F_Integer = Data.stacks[Data.Stack.Frame].pop()
    b: F_Integer = Data.stacks[Data.Stack.Frame].pop()
    Data.stacks[Data.Stack[a.value]] = Data.stacks[Data.Stack[b.value]]


@addCommand("peek", [F_Integer, F_Integer])
def peek():
    """looks at a stack and gets the vale from it index stack peek"""
    a: F_Integer = Data.stacks[Data.Stack.Frame].pop()
    b: F_Integer = Data.stacks[Data.Stack.Frame].pop()
    Data.stacks[Data.Stack.Frame].append(Data.stacks[Data.Stack(a.value)][b.value])


@addCommand("poke", [F_any, F_Integer, F_Integer])
def poke():
    """pushes a value into the given stack  value index stack"""
    a: F_Integer = Data.stacks[Data.Stack.Frame].pop()
    b: F_Integer = Data.stacks[Data.Stack.Frame].pop()
    c: F_any = Data.stacks[Data.Stack.Frame].pop()
    Data.stacks[Data.Stack(a.value)][b.value] = c


@addCommand("pop", [F_Integer])
def pop_():
    """takes the top of the stack and puts it on to the top of the frame stack"""
    a: F_Integer = Data.stacks[Data.Stack.Frame].pop()
    Data.stacks[Data.Stack.Frame].append(Data.stacks[Data.Stack(a.value)])


@addCommand("push", [F_any, F_Integer])
def push():
    """takes the top of the stack and pushes it to another stack"""
    a: F_Integer = Data.stacks[Data.Stack.Frame].pop()
    b: F_any = Data.stacks[Data.Stack.Frame].pop()
    Data.stacks[Data.Stack(a.value)].append(b)
