from antlr4 import CommonTokenStream, InputStream

from txt2musicxml.concrete_chords_visitor import ConcreteChordsVisitor
from txt2musicxml.grammer.ChordsLexer import ChordsLexer
from txt2musicxml.grammer.ChordsParser import ChordsParser
from txt2musicxml.models import Sheet
from tests.mock_sheet import mock_sheet


def test_visit():
    with open("tests/crd_files/aguas_de_marco_snippet.crd", "r") as f:
        crd_text = f.read()
    data = InputStream(crd_text)
    lexer = ChordsLexer(data)
    stream = CommonTokenStream(lexer)
    parser = ChordsParser(stream)
    parse_tree = parser.sheet()
    visitor = ConcreteChordsVisitor()
    result: Sheet = visitor.visit(parse_tree)
    expected = mock_sheet()
    expected = expected.to_list()
    result = result.to_list()
    expected == result
