from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from typing import Callable, Generic, TypeVar

from antlr4 import CommonTokenStream, InputStream

from txt2musicxml.concrete_chords_visitor import ConcreteChordsVisitor
from txt2musicxml.concrete_front_matter_visitor import (
    ConcreteFrontMatterVisitor,
)
from txt2musicxml.grammer.ChordsLexer import ChordsLexer
from txt2musicxml.grammer.ChordsParser import ChordsParser
from txt2musicxml.grammer.FrontMatterLexer import FrontMatterLexer
from txt2musicxml.grammer.FrontMatterParser import FrontMatterParser
from txt2musicxml.models import FrontMatter, Sheet
from txt2musicxml.xml_generator import SheetXmlGenerator

T = TypeVar("T")
U = TypeVar("U")


@dataclass
class pipe(Generic[T]):
    v: T

    def __rshift__(self, f: Callable[[T], U]) -> pipe[U]:
        return pipe(f(self.v))

    def __call__(self) -> T:
        return self.v


def main():
    if sys.stdin.isatty():
        exit("Missing input")
    input_ = sys.stdin.read().strip()
    split = re.split(r"----*", input_, 1)
    front_matter_str: str | None = None
    front_matter: FrontMatter | None = None
    if len(split) == 2:
        front_matter_str, chords = split
    elif len(split) == 1:
        chords = split[0]
    else:
        exit("Bad input")
    if front_matter_str:
        front_matter: FrontMatter = (
            pipe(
                (
                    pipe(front_matter_str.strip())
                    >> InputStream
                    >> FrontMatterLexer
                    >> CommonTokenStream
                    >> FrontMatterParser
                )().front_matter()
            )
            >> ConcreteFrontMatterVisitor().visit
        )()

    sheet: Sheet = (
        pipe(
            (
                pipe(chords.strip())
                >> InputStream
                >> ChordsLexer
                >> CommonTokenStream
                >> ChordsParser
            )().sheet()
        )
        >> ConcreteChordsVisitor().visit
    )()

    if front_matter:
        sheet = add_front_matter_to_sheet(sheet, front_matter)

    (
        pipe((pipe(sheet) >> SheetXmlGenerator)().generate_xml())
        >> print  # noqa: F633
    )


def add_front_matter_to_sheet(sheet: Sheet, front_matter: FrontMatter):
    sheet.title = front_matter.title
    sheet.author = front_matter.author
    return sheet


if __name__ == "__main__":
    main()
