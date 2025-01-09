# Generated from txt2musicxml/grammer/FrontMatter.g4 by ANTLR 4.13.2
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
        2,
        20,
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
        1,
        0,
        1,
        0,
        1,
        0,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
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
        0,
        0,
        4,
        0,
        2,
        4,
        6,
        0,
        0,
        15,
        0,
        8,
        1,
        0,
        0,
        0,
        2,
        11,
        1,
        0,
        0,
        0,
        4,
        15,
        1,
        0,
        0,
        0,
        6,
        17,
        1,
        0,
        0,
        0,
        8,
        9,
        3,
        2,
        1,
        0,
        9,
        10,
        5,
        0,
        0,
        1,
        10,
        1,
        1,
        0,
        0,
        0,
        11,
        12,
        3,
        4,
        2,
        0,
        12,
        13,
        5,
        1,
        0,
        0,
        13,
        14,
        3,
        6,
        3,
        0,
        14,
        3,
        1,
        0,
        0,
        0,
        15,
        16,
        5,
        2,
        0,
        0,
        16,
        5,
        1,
        0,
        0,
        0,
        17,
        18,
        5,
        2,
        0,
        0,
        18,
        7,
        1,
        0,
        0,
        0,
        0,
    ]


class FrontMatterParser(Parser):

    grammarFileName = "FrontMatter.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    sharedContextCache = PredictionContextCache()

    literalNames = ["<INVALID>", "'-'"]

    symbolicNames = ["<INVALID>", "<INVALID>", "ANY_STRING"]

    RULE_front_matter = 0
    RULE_title_author = 1
    RULE_title = 2
    RULE_author = 3

    ruleNames = ["front_matter", "title_author", "title", "author"]

    EOF = Token.EOF
    T__0 = 1
    ANY_STRING = 2

    def __init__(self, input: TokenStream, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(
            self, self.atn, self.decisionsToDFA, self.sharedContextCache
        )
        self._predicates = None

    class Front_matterContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self,
            parser,
            parent: ParserRuleContext = None,
            invokingState: int = -1,
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def title_author(self):
            return self.getTypedRuleContext(
                FrontMatterParser.Title_authorContext, 0
            )

        def EOF(self):
            return self.getToken(FrontMatterParser.EOF, 0)

        def getRuleIndex(self):
            return FrontMatterParser.RULE_front_matter

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterFront_matter"):
                listener.enterFront_matter(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitFront_matter"):
                listener.exitFront_matter(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitFront_matter"):
                return visitor.visitFront_matter(self)
            else:
                return visitor.visitChildren(self)

    def front_matter(self):

        localctx = FrontMatterParser.Front_matterContext(
            self, self._ctx, self.state
        )
        self.enterRule(localctx, 0, self.RULE_front_matter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.title_author()
            self.state = 9
            self.match(FrontMatterParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Title_authorContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self,
            parser,
            parent: ParserRuleContext = None,
            invokingState: int = -1,
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def title(self):
            return self.getTypedRuleContext(FrontMatterParser.TitleContext, 0)

        def author(self):
            return self.getTypedRuleContext(FrontMatterParser.AuthorContext, 0)

        def getRuleIndex(self):
            return FrontMatterParser.RULE_title_author

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterTitle_author"):
                listener.enterTitle_author(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitTitle_author"):
                listener.exitTitle_author(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitTitle_author"):
                return visitor.visitTitle_author(self)
            else:
                return visitor.visitChildren(self)

    def title_author(self):

        localctx = FrontMatterParser.Title_authorContext(
            self, self._ctx, self.state
        )
        self.enterRule(localctx, 2, self.RULE_title_author)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self.title()
            self.state = 12
            self.match(FrontMatterParser.T__0)
            self.state = 13
            self.author()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TitleContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self,
            parser,
            parent: ParserRuleContext = None,
            invokingState: int = -1,
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ANY_STRING(self):
            return self.getToken(FrontMatterParser.ANY_STRING, 0)

        def getRuleIndex(self):
            return FrontMatterParser.RULE_title

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterTitle"):
                listener.enterTitle(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitTitle"):
                listener.exitTitle(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitTitle"):
                return visitor.visitTitle(self)
            else:
                return visitor.visitChildren(self)

    def title(self):

        localctx = FrontMatterParser.TitleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_title)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self.match(FrontMatterParser.ANY_STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AuthorContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self,
            parser,
            parent: ParserRuleContext = None,
            invokingState: int = -1,
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ANY_STRING(self):
            return self.getToken(FrontMatterParser.ANY_STRING, 0)

        def getRuleIndex(self):
            return FrontMatterParser.RULE_author

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterAuthor"):
                listener.enterAuthor(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitAuthor"):
                listener.exitAuthor(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitAuthor"):
                return visitor.visitAuthor(self)
            else:
                return visitor.visitChildren(self)

    def author(self):

        localctx = FrontMatterParser.AuthorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_author)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self.match(FrontMatterParser.ANY_STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx
