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
