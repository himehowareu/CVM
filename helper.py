from pprint import pprint


debugging: bool = False


def log(info: str, data: object = None):
    """
    It prints the info and data if debugging is True

    :param info: The information you want to print
    :type info: str
    :param data: the data to be sent to the server
    :type data: object
    """
    if debugging:
        print(info, data)


def help():
    """
    It prints the name and arguments of each function and what each function does
    """
    from func import functions

    out = "|functions | args|description |"
    out += "\n"
    out += "|---|---|"
    for func in functions:
        args = []
        for x in func.args:
            args.append(x.type)
        if not args:
            args = "None"

        out += "\n|%s|%s|%s|" % (func.name, args, func.doc)
    return out


def debugCommand(token: str) -> bool:
    """
    Dumps all the stacks for debugging

    :param token: str - The token that is being processed
    :type token: str
    :return: A boolean value.
    """
    import Data

    com: str = token[1:]
    if com == "dump":
        print(":::::::::::dumping memory:::::::::::")
        for memStack in Data.Stack:
            print("%s:" % (memStack.name), Data.stacks[memStack])
        print("call", Data.CallData)
        # exit("memory has been dumped")
    if com == "func":
        pprint(Data.FunctionStack)
    if com == "help":
        help()
    if com == "debug":
        global debugging
        debugging = not debugging

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
        temp = Data.stacks[Data.Stack.Code].pop()
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

    for memStack in Data.Stack:
        Data.stacks[memStack] = []
