from pprint import pprint


debuging: bool = False


def log(info: str, data: object = None):
    if debuging:
        print(info, data)


def command(token: str) -> bool:
    from Data import CodeStack, FrameStack, FunctionStack

    com: str = token[1:]
    if com == "dump":
        print("CodeStack")
        pprint(CodeStack)
        print("FunctionStack")
        pprint(FunctionStack)
        print("FrameStack")
        pprint(FrameStack)
        exit("memory has been dumped")
    if com == "func":
        pprint(FunctionStack)
    return False


def getTokensTill(token: str):
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
    import Data

    Data.CodeStack = []
    Data.FrameStack = Data.Stack()
    Data.FunctionStack = []
    Data.CallData = {}
