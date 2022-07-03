from pprint import pprint

debuging: bool = False


def log(info: str, data: object = None):
    if debuging:
        print(info, data)


def command(token: str) -> bool:
    from stack import CodeStack, FrameStack

    com: str = token[1:]
    if com == "dump":
        print("CodeStack")
        pprint(CodeStack)
        print("FrameStack")
        pprint(FrameStack)
        exit("memory has been dumped")
    return False
