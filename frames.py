from typing import Type
from helper import log


class Frame(object):
    type = "Frame"

    def __init__(self, token):
        self.value = token
        log("created ", type(self))

    @classmethod
    def matches(self, other: "Frame") -> bool:
        return self.type == other.type

    def __repr__(self) -> str:
        return str(self.type)


class F_Integer(Frame):
    type = "Integer"

    def __init__(self, token):
        value = int(token)
        super().__init__(value)


class F_String(Frame):
    type = "String"

    def __init__(self, token):
        value = token.strip('"')
        super().__init__(value)


class F_Command(Frame):
    type = "Command"

    def __init__(self, token):
        value = token
        super().__init__(value)


class F_Boolean(Frame):
    type = "Boolean"

    def __init__(self, token: bool):
        super().__init__(int(token))

    @classmethod
    def matches(self, other: "Frame") -> bool:
        return other.type in [self.type, F_Integer.type, F_String.type]


class F_any(Frame):
    type = "any"

    @classmethod
    def matches(self, other: "Frame") -> bool:
        return True


class F_Unknown(Frame):
    def __init__(self, token):
        exit("##### ran into unknown frame  [%s] #####" % (token))
        super().__init__("unknown", token)


def __codeCheck__(token: str) -> bool:
    from func import functions

    for fun in functions:
        if fun.name == token:
            return True
    return False


def frameData(token: str) -> Frame:
    log("token", token)
    if token.isnumeric():
        return F_Integer(token)

    if token.startswith('"') and token.endswith('"'):
        return F_String(token)

    if __codeCheck__(token):
        return F_Command(token)
    return F_Unknown(token)
