# Generated from txt2musicxml/grammer/Chords.g4 by ANTLR 4.13.2
from antlr4 import *

if "." in __name__:
    from .ChordsParser import ChordsParser
else:
    from ChordsParser import ChordsParser

# This class defines a complete generic visitor for a parse tree produced by ChordsParser.


class ChordsVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ChordsParser#sheet.
    def visitSheet(self, ctx: ChordsParser.SheetContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ChordsParser#line.
    def visitLine(self, ctx: ChordsParser.LineContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ChordsParser#bar.
    def visitBar(self, ctx: ChordsParser.BarContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ChordsParser#chord.
    def visitChord(self, ctx: ChordsParser.ChordContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ChordsParser#root.
    def visitRoot(self, ctx: ChordsParser.RootContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ChordsParser#bass.
    def visitBass(self, ctx: ChordsParser.BassContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ChordsParser#note.
    def visitNote(self, ctx: ChordsParser.NoteContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ChordsParser#alteration.
    def visitAlteration(self, ctx: ChordsParser.AlterationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ChordsParser#suffix.
    def visitSuffix(self, ctx: ChordsParser.SuffixContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ChordsParser#right_barlines.
    def visitRight_barlines(self, ctx: ChordsParser.Right_barlinesContext):
        return self.visitChildren(ctx)


del ChordsParser
