# Generated from txt2musicxml/grammer/FrontMatter.g4 by ANTLR 4.13.2
from antlr4 import *

if "." in __name__:
    from .FrontMatterParser import FrontMatterParser
else:
    from FrontMatterParser import FrontMatterParser


# This class defines a complete listener for a parse tree produced by FrontMatterParser.
class FrontMatterListener(ParseTreeListener):

    # Enter a parse tree produced by FrontMatterParser#front_matter.
    def enterFront_matter(self, ctx: FrontMatterParser.Front_matterContext):
        pass

    # Exit a parse tree produced by FrontMatterParser#front_matter.
    def exitFront_matter(self, ctx: FrontMatterParser.Front_matterContext):
        pass

    # Enter a parse tree produced by FrontMatterParser#title_author.
    def enterTitle_author(self, ctx: FrontMatterParser.Title_authorContext):
        pass

    # Exit a parse tree produced by FrontMatterParser#title_author.
    def exitTitle_author(self, ctx: FrontMatterParser.Title_authorContext):
        pass

    # Enter a parse tree produced by FrontMatterParser#title.
    def enterTitle(self, ctx: FrontMatterParser.TitleContext):
        pass

    # Exit a parse tree produced by FrontMatterParser#title.
    def exitTitle(self, ctx: FrontMatterParser.TitleContext):
        pass

    # Enter a parse tree produced by FrontMatterParser#author.
    def enterAuthor(self, ctx: FrontMatterParser.AuthorContext):
        pass

    # Exit a parse tree produced by FrontMatterParser#author.
    def exitAuthor(self, ctx: FrontMatterParser.AuthorContext):
        pass


del FrontMatterParser
