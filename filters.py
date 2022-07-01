
passes = []


def addPass(comment):
    def dec(func):
        global passes
        pass_ = (func, comment)
        passes.append(pass_)
        return func

    return dec


@addPass("removing comments")
def removeComments(source:str) -> str:
    out = ""
    comment = False
    for letter in source:
        if letter == "#":
            comment = True
        elif not comment:
            out += letter
        if letter == "\n":
            out += "\n"
            comment = False
    return out


@addPass("Padding new lines")
def padNewLines(source:str)-> str:
    return source.replace("\n", " \n ")


@addPass("Splitting commands and joining strings")
def splitCode(source:str) -> list[str]:
    out = []
    string = False
    current = ""
    for token in source.split(" "):
        if string:
            if token.endswith('"') and not token.endswith('\\"'):
                out.append(current + " " + token)
                current = ""
                string = False
            else:
                current += " " + token

        elif token.startswith('"'):
            string = True
            current = token
        else:
            out.append(token)
    return out

@addPass("removing whitespace and stuff")
def removeJunk(source:list[str])->list[str]:
    return [out for out in source if out not in ["", "\n", "\t"]]
