class Argument:
    name: str
    atype: type
    default: type
    dest: str

    def __init__(self, name: str, atype=str, default: type = None, dest: str = ''):
        self.name = name
        self.atype = atype
        self.default = default
        self.dest = dest
