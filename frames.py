from typing import Type
from helper import log


class Frame(object):
    type: str = "Frame"

    def __init__(self, token):
        self.value: object = token
        log("created %s with value %s" % (type(self), self.value))

    @classmethod
    def matches(self, other: "Frame") -> bool:
        return self.type == other.type

    def __repr__(self) -> str:
        return str(self.value)


class F_Integer(Frame):
    type: str = "Integer"

    def __init__(self, token):
        value: int = int(token)
        super().__init__(value)


class F_String(Frame):
    type: str = "String"

    def __init__(self, token):
        value: str = token.strip('"')
        super().__init__(value)

    def __repr__(self) -> str:
        match self.value:
            case " ":
                return "<Space>"
            case "":
                return "<None>"
            case default:
                return str(self.value)


class F_Command(Frame):
    type: str = "Command"

    def __init__(self, token):
        value: str = token
        super().__init__(value)


class F_Boolean(Frame):
    type: str = "Boolean"

    def __init__(self, token: bool):
        super().__init__(int(token))

    @classmethod
    def matches(self, other: "Frame") -> bool:
        return other.type in [self.type, F_Integer.type, F_String.type]


class F_any(Frame):
    type: str = "any"

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


def unFrame(frame_: Frame) -> object:
    return frame_.value
