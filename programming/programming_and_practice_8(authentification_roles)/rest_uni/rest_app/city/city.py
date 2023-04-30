from enum import Enum, auto
class City(Enum):
    NEW_YORK = auto()
    LOS_ANGELES = auto()
    KYIV = auto()
    LVIV = auto()
    LONDON = auto()
    BERLIN = auto()
    PARIS = auto()
    TORONTO = auto()
    BEIJING = auto()
    KHARKIV = auto()
    WARSAW = auto()
    ROME = auto()
    OSLO = auto()
    OTTAWA = auto()
    WASHINGTON = auto()

    def __lt__(self, other):
        return self.name < other.name

    def __str__(self):
        res= list(self.name.lower())
        res[0] = res[0].upper()
        for i, c in enumerate(res):
            if c=="_":
                res[i]=" "
                res[i+1]=res[i+1].upper()
        return "".join(res)

    @staticmethod
    def list_values():
        return [str(e) for e in City]

