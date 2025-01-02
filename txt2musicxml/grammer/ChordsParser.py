# Generated from txt2musicxml/grammer/Chords.g4 by ANTLR 4.13.2
# encoding: utf-8
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
        1,
        11,
        91,
        2,
        0,
        7,
        0,
        2,
        1,
        7,
        1,
        2,
        2,
        7,
        2,
        2,
        3,
        7,
        3,
        2,
        4,
        7,
        4,
        2,
        5,
        7,
        5,
        2,
        6,
        7,
        6,
        2,
        7,
        7,
        7,
        2,
        8,
        7,
        8,
        2,
        9,
        7,
        9,
        1,
        0,
        4,
        0,
        22,
        8,
        0,
        11,
        0,
        12,
        0,
        23,
        1,
        0,
        1,
        0,
        1,
        1,
        3,
        1,
        29,
        8,
        1,
        1,
        1,
        4,
        1,
        32,
        8,
        1,
        11,
        1,
        12,
        1,
        33,
        1,
        2,
        3,
        2,
        37,
        8,
        2,
        1,
        2,
        1,
        2,
        1,
        2,
        5,
        2,
        42,
        8,
        2,
        10,
        2,
        12,
        2,
        45,
        9,
        2,
        1,
        2,
        3,
        2,
        48,
        8,
        2,
        1,
        2,
        3,
        2,
        51,
        8,
        2,
        1,
        2,
        1,
        2,
        3,
        2,
        55,
        8,
        2,
        3,
        2,
        57,
        8,
        2,
        1,
        2,
        1,
        2,
        1,
        3,
        1,
        3,
        1,
        3,
        1,
        3,
        1,
        3,
        1,
        3,
        1,
        3,
        1,
        3,
        1,
        3,
        1,
        3,
        1,
        3,
        3,
        3,
        72,
        8,
        3,
        1,
        4,
        1,
        4,
        3,
        4,
        76,
        8,
        4,
        1,
        5,
        1,
        5,
        1,
        5,
        3,
        5,
        81,
        8,
        5,
        1,
        6,
        1,
        6,
        1,
        7,
        1,
        7,
        1,
        8,
        1,
        8,
        1,
        9,
        1,
        9,
        1,
        9,
        0,
        0,
        10,
        0,
        2,
        4,
        6,
        8,
        10,
        12,
        14,
        16,
        18,
        0,
        1,
        2,
        0,
        6,
        7,
        9,
        9,
        94,
        0,
        21,
        1,
        0,
        0,
        0,
        2,
        28,
        1,
        0,
        0,
        0,
        4,
        56,
        1,
        0,
        0,
        0,
        6,
        71,
        1,
        0,
        0,
        0,
        8,
        73,
        1,
        0,
        0,
        0,
        10,
        77,
        1,
        0,
        0,
        0,
        12,
        82,
        1,
        0,
        0,
        0,
        14,
        84,
        1,
        0,
        0,
        0,
        16,
        86,
        1,
        0,
        0,
        0,
        18,
        88,
        1,
        0,
        0,
        0,
        20,
        22,
        3,
        2,
        1,
        0,
        21,
        20,
        1,
        0,
        0,
        0,
        22,
        23,
        1,
        0,
        0,
        0,
        23,
        21,
        1,
        0,
        0,
        0,
        23,
        24,
        1,
        0,
        0,
        0,
        24,
        25,
        1,
        0,
        0,
        0,
        25,
        26,
        5,
        0,
        0,
        1,
        26,
        1,
        1,
        0,
        0,
        0,
        27,
        29,
        5,
        10,
        0,
        0,
        28,
        27,
        1,
        0,
        0,
        0,
        28,
        29,
        1,
        0,
        0,
        0,
        29,
        31,
        1,
        0,
        0,
        0,
        30,
        32,
        3,
        4,
        2,
        0,
        31,
        30,
        1,
        0,
        0,
        0,
        32,
        33,
        1,
        0,
        0,
        0,
        33,
        31,
        1,
        0,
        0,
        0,
        33,
        34,
        1,
        0,
        0,
        0,
        34,
        3,
        1,
        0,
        0,
        0,
        35,
        37,
        5,
        11,
        0,
        0,
        36,
        35,
        1,
        0,
        0,
        0,
        36,
        37,
        1,
        0,
        0,
        0,
        37,
        38,
        1,
        0,
        0,
        0,
        38,
        43,
        3,
        6,
        3,
        0,
        39,
        40,
        5,
        11,
        0,
        0,
        40,
        42,
        3,
        6,
        3,
        0,
        41,
        39,
        1,
        0,
        0,
        0,
        42,
        45,
        1,
        0,
        0,
        0,
        43,
        41,
        1,
        0,
        0,
        0,
        43,
        44,
        1,
        0,
        0,
        0,
        44,
        47,
        1,
        0,
        0,
        0,
        45,
        43,
        1,
        0,
        0,
        0,
        46,
        48,
        5,
        11,
        0,
        0,
        47,
        46,
        1,
        0,
        0,
        0,
        47,
        48,
        1,
        0,
        0,
        0,
        48,
        57,
        1,
        0,
        0,
        0,
        49,
        51,
        5,
        11,
        0,
        0,
        50,
        49,
        1,
        0,
        0,
        0,
        50,
        51,
        1,
        0,
        0,
        0,
        51,
        52,
        1,
        0,
        0,
        0,
        52,
        54,
        5,
        1,
        0,
        0,
        53,
        55,
        5,
        11,
        0,
        0,
        54,
        53,
        1,
        0,
        0,
        0,
        54,
        55,
        1,
        0,
        0,
        0,
        55,
        57,
        1,
        0,
        0,
        0,
        56,
        36,
        1,
        0,
        0,
        0,
        56,
        50,
        1,
        0,
        0,
        0,
        57,
        58,
        1,
        0,
        0,
        0,
        58,
        59,
        3,
        18,
        9,
        0,
        59,
        5,
        1,
        0,
        0,
        0,
        60,
        72,
        3,
        8,
        4,
        0,
        61,
        62,
        3,
        8,
        4,
        0,
        62,
        63,
        3,
        16,
        8,
        0,
        63,
        72,
        1,
        0,
        0,
        0,
        64,
        65,
        3,
        8,
        4,
        0,
        65,
        66,
        3,
        10,
        5,
        0,
        66,
        72,
        1,
        0,
        0,
        0,
        67,
        68,
        3,
        8,
        4,
        0,
        68,
        69,
        3,
        16,
        8,
        0,
        69,
        70,
        3,
        10,
        5,
        0,
        70,
        72,
        1,
        0,
        0,
        0,
        71,
        60,
        1,
        0,
        0,
        0,
        71,
        61,
        1,
        0,
        0,
        0,
        71,
        64,
        1,
        0,
        0,
        0,
        71,
        67,
        1,
        0,
        0,
        0,
        72,
        7,
        1,
        0,
        0,
        0,
        73,
        75,
        3,
        12,
        6,
        0,
        74,
        76,
        3,
        14,
        7,
        0,
        75,
        74,
        1,
        0,
        0,
        0,
        75,
        76,
        1,
        0,
        0,
        0,
        76,
        9,
        1,
        0,
        0,
        0,
        77,
        78,
        5,
        5,
        0,
        0,
        78,
        80,
        3,
        12,
        6,
        0,
        79,
        81,
        3,
        14,
        7,
        0,
        80,
        79,
        1,
        0,
        0,
        0,
        80,
        81,
        1,
        0,
        0,
        0,
        81,
        11,
        1,
        0,
        0,
        0,
        82,
        83,
        5,
        2,
        0,
        0,
        83,
        13,
        1,
        0,
        0,
        0,
        84,
        85,
        5,
        3,
        0,
        0,
        85,
        15,
        1,
        0,
        0,
        0,
        86,
        87,
        5,
        4,
        0,
        0,
        87,
        17,
        1,
        0,
        0,
        0,
        88,
        89,
        7,
        0,
        0,
        0,
        89,
        19,
        1,
        0,
        0,
        0,
        12,
        23,
        28,
        33,
        36,
        43,
        47,
        50,
        54,
        56,
        71,
        75,
        80,
    ]


class ChordsParser(Parser):

    grammarFileName = "Chords.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    sharedContextCache = PredictionContextCache()

    literalNames = [
        "<INVALID>",
        "'%'",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "'/'",
        "':||'",
        "'||'",
        "':'",
        "'|'",
    ]

    symbolicNames = [
        "<INVALID>",
        "MEASURE_REPEAT",
        "NOTE",
        "ALTERATION",
        "SUFFIX",
        "SLASH",
        "REPEAT_BARLINE",
        "DOUBLE_BARLINE",
        "COLON",
        "BARLINE",
        "NEWLINE",
        "WHITESPACE",
    ]

    RULE_sheet = 0
    RULE_line = 1
    RULE_bar = 2
    RULE_chord = 3
    RULE_root = 4
    RULE_bass = 5
    RULE_note = 6
    RULE_alteration = 7
    RULE_suffix = 8
    RULE_right_barlines = 9

    ruleNames = [
        "sheet",
        "line",
        "bar",
        "chord",
        "root",
        "bass",
        "note",
        "alteration",
        "suffix",
        "right_barlines",
    ]

    EOF = Token.EOF
    MEASURE_REPEAT = 1
    NOTE = 2
    ALTERATION = 3
    SUFFIX = 4
    SLASH = 5
    REPEAT_BARLINE = 6
    DOUBLE_BARLINE = 7
    COLON = 8
    BARLINE = 9
    NEWLINE = 10
    WHITESPACE = 11

    def __init__(self, input: TokenStream, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(
            self, self.atn, self.decisionsToDFA, self.sharedContextCache
        )
        self._predicates = None

    class SheetContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self,
            parser,
            parent: ParserRuleContext = None,
            invokingState: int = -1,
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ChordsParser.EOF, 0)

        def line(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(ChordsParser.LineContext)
            else:
                return self.getTypedRuleContext(ChordsParser.LineContext, i)

        def getRuleIndex(self):
            return ChordsParser.RULE_sheet

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterSheet"):
                listener.enterSheet(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitSheet"):
                listener.exitSheet(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitSheet"):
                return visitor.visitSheet(self)
            else:
                return visitor.visitChildren(self)

    def sheet(self):

        localctx = ChordsParser.SheetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_sheet)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 20
                self.line()
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3F) == 0 and ((1 << _la) & 3078) != 0)):
                    break

            self.state = 25
            self.match(ChordsParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LineContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self,
            parser,
            parent: ParserRuleContext = None,
            invokingState: int = -1,
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(ChordsParser.NEWLINE, 0)

        def bar(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(ChordsParser.BarContext)
            else:
                return self.getTypedRuleContext(ChordsParser.BarContext, i)

        def getRuleIndex(self):
            return ChordsParser.RULE_line

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterLine"):
                listener.enterLine(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitLine"):
                listener.exitLine(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitLine"):
                return visitor.visitLine(self)
            else:
                return visitor.visitChildren(self)

    def line(self):

        localctx = ChordsParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_line)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 10:
                self.state = 27
                self.match(ChordsParser.NEWLINE)

            self.state = 31
            self._errHandler.sync(self)
            _alt = 1
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 30
                    self.bar()

                else:
                    raise NoViableAltException(self)
                self.state = 33
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 2, self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BarContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self,
            parser,
            parent: ParserRuleContext = None,
            invokingState: int = -1,
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def right_barlines(self):
            return self.getTypedRuleContext(
                ChordsParser.Right_barlinesContext, 0
            )

        def chord(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(ChordsParser.ChordContext)
            else:
                return self.getTypedRuleContext(ChordsParser.ChordContext, i)

        def MEASURE_REPEAT(self):
            return self.getToken(ChordsParser.MEASURE_REPEAT, 0)

        def WHITESPACE(self, i: int = None):
            if i is None:
                return self.getTokens(ChordsParser.WHITESPACE)
            else:
                return self.getToken(ChordsParser.WHITESPACE, i)

        def getRuleIndex(self):
            return ChordsParser.RULE_bar

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterBar"):
                listener.enterBar(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitBar"):
                listener.exitBar(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitBar"):
                return visitor.visitBar(self)
            else:
                return visitor.visitChildren(self)

    def bar(self):

        localctx = ChordsParser.BarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_bar)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 8, self._ctx)
            if la_ == 1:
                self.state = 36
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == 11:
                    self.state = 35
                    self.match(ChordsParser.WHITESPACE)

                self.state = 38
                self.chord()
                self.state = 43
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 4, self._ctx)
                while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 39
                        self.match(ChordsParser.WHITESPACE)
                        self.state = 40
                        self.chord()
                    self.state = 45
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(
                        self._input, 4, self._ctx
                    )

                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == 11:
                    self.state = 46
                    self.match(ChordsParser.WHITESPACE)

                pass

            elif la_ == 2:
                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == 11:
                    self.state = 49
                    self.match(ChordsParser.WHITESPACE)

                self.state = 52
                self.match(ChordsParser.MEASURE_REPEAT)
                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == 11:
                    self.state = 53
                    self.match(ChordsParser.WHITESPACE)

                pass

            self.state = 58
            self.right_barlines()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ChordContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self,
            parser,
            parent: ParserRuleContext = None,
            invokingState: int = -1,
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def root(self):
            return self.getTypedRuleContext(ChordsParser.RootContext, 0)

        def suffix(self):
            return self.getTypedRuleContext(ChordsParser.SuffixContext, 0)

        def bass(self):
            return self.getTypedRuleContext(ChordsParser.BassContext, 0)

        def getRuleIndex(self):
            return ChordsParser.RULE_chord

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterChord"):
                listener.enterChord(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitChord"):
                listener.exitChord(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitChord"):
                return visitor.visitChord(self)
            else:
                return visitor.visitChildren(self)

    def chord(self):

        localctx = ChordsParser.ChordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_chord)
        try:
            self.state = 71
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 9, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 60
                self.root()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 61
                self.root()
                self.state = 62
                self.suffix()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 64
                self.root()
                self.state = 65
                self.bass()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 67
                self.root()
                self.state = 68
                self.suffix()
                self.state = 69
                self.bass()
                pass

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RootContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self,
            parser,
            parent: ParserRuleContext = None,
            invokingState: int = -1,
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def note(self):
            return self.getTypedRuleContext(ChordsParser.NoteContext, 0)

        def alteration(self):
            return self.getTypedRuleContext(ChordsParser.AlterationContext, 0)

        def getRuleIndex(self):
            return ChordsParser.RULE_root

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterRoot"):
                listener.enterRoot(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitRoot"):
                listener.exitRoot(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitRoot"):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)

    def root(self):

        localctx = ChordsParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_root)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.note()
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 3:
                self.state = 74
                self.alteration()

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BassContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self,
            parser,
            parent: ParserRuleContext = None,
            invokingState: int = -1,
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SLASH(self):
            return self.getToken(ChordsParser.SLASH, 0)

        def note(self):
            return self.getTypedRuleContext(ChordsParser.NoteContext, 0)

        def alteration(self):
            return self.getTypedRuleContext(ChordsParser.AlterationContext, 0)

        def getRuleIndex(self):
            return ChordsParser.RULE_bass

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterBass"):
                listener.enterBass(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitBass"):
                listener.exitBass(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitBass"):
                return visitor.visitBass(self)
            else:
                return visitor.visitChildren(self)

    def bass(self):

        localctx = ChordsParser.BassContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_bass)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(ChordsParser.SLASH)
            self.state = 78
            self.note()
            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 3:
                self.state = 79
                self.alteration()

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NoteContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self,
            parser,
            parent: ParserRuleContext = None,
            invokingState: int = -1,
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOTE(self):
            return self.getToken(ChordsParser.NOTE, 0)

        def getRuleIndex(self):
            return ChordsParser.RULE_note

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterNote"):
                listener.enterNote(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitNote"):
                listener.exitNote(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitNote"):
                return visitor.visitNote(self)
            else:
                return visitor.visitChildren(self)

    def note(self):

        localctx = ChordsParser.NoteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_note)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(ChordsParser.NOTE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AlterationContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self,
            parser,
            parent: ParserRuleContext = None,
            invokingState: int = -1,
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ALTERATION(self):
            return self.getToken(ChordsParser.ALTERATION, 0)

        def getRuleIndex(self):
            return ChordsParser.RULE_alteration

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterAlteration"):
                listener.enterAlteration(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitAlteration"):
                listener.exitAlteration(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitAlteration"):
                return visitor.visitAlteration(self)
            else:
                return visitor.visitChildren(self)

    def alteration(self):

        localctx = ChordsParser.AlterationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_alteration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(ChordsParser.ALTERATION)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SuffixContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self,
            parser,
            parent: ParserRuleContext = None,
            invokingState: int = -1,
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUFFIX(self):
            return self.getToken(ChordsParser.SUFFIX, 0)

        def getRuleIndex(self):
            return ChordsParser.RULE_suffix

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterSuffix"):
                listener.enterSuffix(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitSuffix"):
                listener.exitSuffix(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitSuffix"):
                return visitor.visitSuffix(self)
            else:
                return visitor.visitChildren(self)

    def suffix(self):

        localctx = ChordsParser.SuffixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_suffix)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(ChordsParser.SUFFIX)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Right_barlinesContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self,
            parser,
            parent: ParserRuleContext = None,
            invokingState: int = -1,
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BARLINE(self):
            return self.getToken(ChordsParser.BARLINE, 0)

        def DOUBLE_BARLINE(self):
            return self.getToken(ChordsParser.DOUBLE_BARLINE, 0)

        def REPEAT_BARLINE(self):
            return self.getToken(ChordsParser.REPEAT_BARLINE, 0)

        def getRuleIndex(self):
            return ChordsParser.RULE_right_barlines

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterRight_barlines"):
                listener.enterRight_barlines(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitRight_barlines"):
                listener.exitRight_barlines(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitRight_barlines"):
                return visitor.visitRight_barlines(self)
            else:
                return visitor.visitChildren(self)

    def right_barlines(self):

        localctx = ChordsParser.Right_barlinesContext(
            self, self._ctx, self.state
        )
        self.enterRule(localctx, 18, self.RULE_right_barlines)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            _la = self._input.LA(1)
            if not ((((_la) & ~0x3F) == 0 and ((1 << _la) & 704) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx
