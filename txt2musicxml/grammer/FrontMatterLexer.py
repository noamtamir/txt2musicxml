# Generated from txt2musicxml/grammer/FrontMatter.g4 by ANTLR 4.13.2
import sys
from io import StringIO

from antlr4 import *

if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,
        0,
        2,
        12,
        6,
        -1,
        2,
        0,
        7,
        0,
        2,
        1,
        7,
        1,
        1,
        0,
        1,
        0,
        1,
        1,
        4,
        1,
        9,
        8,
        1,
        11,
        1,
        12,
        1,
        10,
        0,
        0,
        2,
        1,
        1,
        3,
        2,
        1,
        0,
        1,
        3,
        0,
        10,
        10,
        13,
        13,
        45,
        45,
        12,
        0,
        1,
        1,
        0,
        0,
        0,
        0,
        3,
        1,
        0,
        0,
        0,
        1,
        5,
        1,
        0,
        0,
        0,
        3,
        8,
        1,
        0,
        0,
        0,
        5,
        6,
        5,
        45,
        0,
        0,
        6,
        2,
        1,
        0,
        0,
        0,
        7,
        9,
        8,
        0,
        0,
        0,
        8,
        7,
        1,
        0,
        0,
        0,
        9,
        10,
        1,
        0,
        0,
        0,
        10,
        8,
        1,
        0,
        0,
        0,
        10,
        11,
        1,
        0,
        0,
        0,
        11,
        4,
        1,
        0,
        0,
        0,
        2,
        0,
        10,
        0,
    ]


class FrontMatterLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    T__0 = 1
    ANY_STRING = 2

    channelNames = ["DEFAULT_TOKEN_CHANNEL", "HIDDEN"]

    modeNames = ["DEFAULT_MODE"]

    literalNames = ["<INVALID>", "'-'"]

    symbolicNames = ["<INVALID>", "ANY_STRING"]

    ruleNames = ["T__0", "ANY_STRING"]

    grammarFileName = "FrontMatter.g4"

    def __init__(self, input=None, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(
            self, self.atn, self.decisionsToDFA, PredictionContextCache()
        )
        self._actions = None
        self._predicates = None
