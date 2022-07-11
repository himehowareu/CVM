from pprint import pprint


debuging: bool = False
remind:bool = False

def log(info: str, data: object = None):
    """
    It prints the info and data if debuging is True

    :param info: The information you want to print
    :type info: str
    :param data: the data to be sent to the server
    :type data: object
    """
    if debuging:
        print(info, data)


def help():
    """
    It prints the name and arguments of each function and what each function does
    """
    from func import functions

    for func in functions:
        args = []
        for x in func.args:
            args.append(x.type)
        print(func.name, args)
        print("\t", func.doc)


def debugCommand(token: str) -> bool:
    """
    Dumps all the stacks for debuging

    :param token: str - The token that is being processed
    :type token: str
    :return: A boolean value.
    """
    from Data import CodeStack, FrameStack, FunctionStack

    com: str = token[1:]
    if com == "dump":
        print(":::::::::::dumping memory:::::::::::")
        print("CodeStack")
        pprint(CodeStack)
        print("FunctionStack")
        pprint(FunctionStack)
        print("FrameStack")
        pprint(FrameStack)
        exit("memory has been dumped")
    if com == "func":
        pprint(FunctionStack)
    if com == "help":
        help()
    if com == "debug":
        global debuging
        debuging = not debuging

    return False


def getTokensTill(token: str):
    """
    It takes a token, and then it pops tokens off of the stack until it finds the token it was given

    :param token: str = The token to stop at
    :type token: str
    """
    import Data

    temp: str = ""
    while True:
        temp = Data.CodeStack.pop()
        if temp == token:
            break
        else:
            if len(Data.FunctionStack) > 0:
                Data.FunctionStack = [temp] + Data.FunctionStack
            else:
                Data.FunctionStack = [temp]


def reset():
    """
    It resets all the stacks
    """

    import Data

    Data.CodeStack = []
    Data.FrameStack = Data.Stack()
    Data.FunctionStack = []
    Data.CallData = {}

def todo(reminder:str):
    if remind:
        print(reminder)