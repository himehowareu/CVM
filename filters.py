from typing import Callable


passes: list[tuple[Callable, str]] = []


def addPass(comment):
    def dec(func):
        global passes
        pass_ = (func, comment)
        passes.append(pass_)
        return func

    return dec


@addPass("removing comments")
def removeComments(source: str) -> str:
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
def padNewLines(source: str) -> str:
    return source.replace("\n", " \n ")


@addPass("Splitting commands and joining strings")
def splitCode(source: str) -> list[str]:
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
            if token.endswith('"'):
                string = False
                out.append(token)
                current = ""
        else:
            out.append(token)
    return out


@addPass("removing whitespace and stuff")
def removeJunk(source: list[str]) -> list[str]:
    out = []
    for line in source:
        if line not in ["", "\n", "\t"]:
            out.append(line)
    return out
