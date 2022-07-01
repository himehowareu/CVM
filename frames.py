from helper import log

class __frame__(object):
    def __init__(self,type_,token):
        self.value=token
        self.type=type_
        log("created ",type(self))
    def __repr__(self) -> str:
        return str(self.value)

class F_Float(__frame__):
    def __init__(self,token):
        value = float(token)
        super().__init__("Float",value)

class F_Integer(__frame__):
    def __init__(self,token):
        value = int(token)
        super().__init__("Integer", value)

class F_String(__frame__):
    def __init__(self,token):
        value = token.strip('"')
        super().__init__("String", value)

class F_Unknown(__frame__):
    def __init__(self,token):
        exit("##### ran into unknown frame #####")
        super().__init__("unknown", token)

def __is_float(element:str)->bool:
    try:
        float(element)
        return True
    except:
        return False


#types: string int float
def frame(token:str)->__frame__:
    log("token",token)
    if token.isnumeric():
        return F_Integer(token)
    if __is_float(token):
        return F_Float(token)
    if token.startswith('"') and token.endswith('"'):
        return F_String(token)
    return F_Unknown(token)
