# Generated from txt2musicxml/grammer/Chords.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,8,61,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,1,0,1,0,1,1,4,1,21,8,1,11,1,12,1,22,1,1,4,1,26,8,1,
        11,1,12,1,27,3,1,30,8,1,1,2,1,2,1,2,3,2,35,8,2,1,2,5,2,38,8,2,10,
        2,12,2,41,9,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,3,6,50,8,6,1,6,4,6,53,
        8,6,11,6,12,6,54,1,7,4,7,58,8,7,11,7,12,7,59,0,0,8,1,1,3,2,5,3,7,
        4,9,5,11,6,13,7,15,8,1,0,4,1,0,65,71,12,0,43,43,45,45,49,49,53,55,
        57,57,94,94,97,97,100,100,109,109,111,111,115,115,248,248,13,0,35,
        35,43,45,48,57,94,94,97,98,100,100,103,103,105,106,109,109,111,111,
        115,115,117,117,248,248,2,0,9,9,32,32,68,0,1,1,0,0,0,0,3,1,0,0,0,
        0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,
        15,1,0,0,0,1,17,1,0,0,0,3,29,1,0,0,0,5,34,1,0,0,0,7,42,1,0,0,0,9,
        44,1,0,0,0,11,46,1,0,0,0,13,52,1,0,0,0,15,57,1,0,0,0,17,18,7,0,0,
        0,18,2,1,0,0,0,19,21,5,98,0,0,20,19,1,0,0,0,21,22,1,0,0,0,22,20,
        1,0,0,0,22,23,1,0,0,0,23,30,1,0,0,0,24,26,5,35,0,0,25,24,1,0,0,0,
        26,27,1,0,0,0,27,25,1,0,0,0,27,28,1,0,0,0,28,30,1,0,0,0,29,20,1,
        0,0,0,29,25,1,0,0,0,30,4,1,0,0,0,31,35,7,1,0,0,32,33,5,35,0,0,33,
        35,5,53,0,0,34,31,1,0,0,0,34,32,1,0,0,0,35,39,1,0,0,0,36,38,7,2,
        0,0,37,36,1,0,0,0,38,41,1,0,0,0,39,37,1,0,0,0,39,40,1,0,0,0,40,6,
        1,0,0,0,41,39,1,0,0,0,42,43,5,47,0,0,43,8,1,0,0,0,44,45,5,58,0,0,
        45,10,1,0,0,0,46,47,5,124,0,0,47,12,1,0,0,0,48,50,5,13,0,0,49,48,
        1,0,0,0,49,50,1,0,0,0,50,51,1,0,0,0,51,53,5,10,0,0,52,49,1,0,0,0,
        53,54,1,0,0,0,54,52,1,0,0,0,54,55,1,0,0,0,55,14,1,0,0,0,56,58,7,
        3,0,0,57,56,1,0,0,0,58,59,1,0,0,0,59,57,1,0,0,0,59,60,1,0,0,0,60,
        16,1,0,0,0,9,0,22,27,29,34,39,49,54,59,0
    ]

class ChordsLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    NOTE = 1
    ALTERATION = 2
    SUFFIX = 3
    SLASH = 4
    COLON = 5
    BARLINE = 6
    NEWLINE = 7
    WHITESPACE = 8

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'/'", "':'", "'|'" ]

    symbolicNames = [ "<INVALID>",
            "NOTE", "ALTERATION", "SUFFIX", "SLASH", "COLON", "BARLINE", 
            "NEWLINE", "WHITESPACE" ]

    ruleNames = [ "NOTE", "ALTERATION", "SUFFIX", "SLASH", "COLON", "BARLINE", 
                  "NEWLINE", "WHITESPACE" ]

    grammarFileName = "Chords.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


