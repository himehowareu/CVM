debuging: bool = False


def log(info: str, data: object = None):
    if debuging:
        print(info, data)
