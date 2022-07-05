from frames import frame


class Stack(list):
    def append(self, __object):
        super().append(frame(__object))

    def push(self, Frame):
        super().append(Frame)


CodeStack: list[str] = []
FrameStack = Stack()
FunctionStack: list[str] = []
CallData: dict[str, list[str]] = {}
