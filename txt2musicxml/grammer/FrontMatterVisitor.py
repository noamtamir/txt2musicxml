# Generated from txt2musicxml/grammer/FrontMatter.g4 by ANTLR 4.13.2
from antlr4 import *

if "." in __name__:
    from .FrontMatterParser import FrontMatterParser
else:
    from FrontMatterParser import FrontMatterParser

# This class defines a complete generic visitor for a parse tree produced by FrontMatterParser.


class FrontMatterVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by FrontMatterParser#front_matter.
    def visitFront_matter(self, ctx: FrontMatterParser.Front_matterContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by FrontMatterParser#title_author.
    def visitTitle_author(self, ctx: FrontMatterParser.Title_authorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by FrontMatterParser#title.
    def visitTitle(self, ctx: FrontMatterParser.TitleContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by FrontMatterParser#author.
    def visitAuthor(self, ctx: FrontMatterParser.AuthorContext):
        return self.visitChildren(ctx)


del FrontMatterParser
