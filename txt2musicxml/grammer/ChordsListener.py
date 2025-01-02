# Generated from txt2musicxml/grammer/Chords.g4 by ANTLR 4.13.2
from antlr4 import *

if "." in __name__:
    from .ChordsParser import ChordsParser
else:
    from ChordsParser import ChordsParser


# This class defines a complete listener for a parse tree produced by ChordsParser.
class ChordsListener(ParseTreeListener):

    # Enter a parse tree produced by ChordsParser#sheet.
    def enterSheet(self, ctx: ChordsParser.SheetContext):
        pass

    # Exit a parse tree produced by ChordsParser#sheet.
    def exitSheet(self, ctx: ChordsParser.SheetContext):
        pass

    # Enter a parse tree produced by ChordsParser#line.
    def enterLine(self, ctx: ChordsParser.LineContext):
        pass

    # Exit a parse tree produced by ChordsParser#line.
    def exitLine(self, ctx: ChordsParser.LineContext):
        pass

    # Enter a parse tree produced by ChordsParser#bar.
    def enterBar(self, ctx: ChordsParser.BarContext):
        pass

    # Exit a parse tree produced by ChordsParser#bar.
    def exitBar(self, ctx: ChordsParser.BarContext):
        pass

    # Enter a parse tree produced by ChordsParser#chord.
    def enterChord(self, ctx: ChordsParser.ChordContext):
        pass

    # Exit a parse tree produced by ChordsParser#chord.
    def exitChord(self, ctx: ChordsParser.ChordContext):
        pass

    # Enter a parse tree produced by ChordsParser#root.
    def enterRoot(self, ctx: ChordsParser.RootContext):
        pass

    # Exit a parse tree produced by ChordsParser#root.
    def exitRoot(self, ctx: ChordsParser.RootContext):
        pass

    # Enter a parse tree produced by ChordsParser#bass.
    def enterBass(self, ctx: ChordsParser.BassContext):
        pass

    # Exit a parse tree produced by ChordsParser#bass.
    def exitBass(self, ctx: ChordsParser.BassContext):
        pass

    # Enter a parse tree produced by ChordsParser#note.
    def enterNote(self, ctx: ChordsParser.NoteContext):
        pass

    # Exit a parse tree produced by ChordsParser#note.
    def exitNote(self, ctx: ChordsParser.NoteContext):
        pass

    # Enter a parse tree produced by ChordsParser#alteration.
    def enterAlteration(self, ctx: ChordsParser.AlterationContext):
        pass

    # Exit a parse tree produced by ChordsParser#alteration.
    def exitAlteration(self, ctx: ChordsParser.AlterationContext):
        pass

    # Enter a parse tree produced by ChordsParser#suffix.
    def enterSuffix(self, ctx: ChordsParser.SuffixContext):
        pass

    # Exit a parse tree produced by ChordsParser#suffix.
    def exitSuffix(self, ctx: ChordsParser.SuffixContext):
        pass

    # Enter a parse tree produced by ChordsParser#right_barlines.
    def enterRight_barlines(self, ctx: ChordsParser.Right_barlinesContext):
        pass

    # Exit a parse tree produced by ChordsParser#right_barlines.
    def exitRight_barlines(self, ctx: ChordsParser.Right_barlinesContext):
        pass


del ChordsParser
