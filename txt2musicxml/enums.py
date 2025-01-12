from enum import Enum


class Barline(str, Enum):
    REGULAR = "REGULAR"
    DOUBLE = "DOUBLE"
    REPEAT = "REPEAT"
    FORWARD_REPEAT = "FORWARD_REPEAT"
    DOUBLE_SIDED_REPEAT = "DOUBLE_SIDED_REPEAT"


TOKEN_TO_BARLINE_MAP = {
    "|": Barline.REGULAR,
    "||": Barline.DOUBLE,
    ":||": Barline.REPEAT,
    "||:": Barline.FORWARD_REPEAT,
    ":||:": Barline.DOUBLE_SIDED_REPEAT,
}


def get_barline_from_text(text: str) -> Barline:
    return TOKEN_TO_BARLINE_MAP.get(text, Barline.REGULAR)
