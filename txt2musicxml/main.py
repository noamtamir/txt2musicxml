from __future__ import annotations

import sys
from dataclasses import dataclass
from typing import Callable, Generic, TypeVar

from antlr4 import CommonTokenStream, InputStream

from txt2musicxml.concrete_chords_visitor import ConcreteChordsVisitor
from txt2musicxml.grammer.ChordsLexer import ChordsLexer
from txt2musicxml.grammer.ChordsParser import ChordsParser
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
    (
        pipe(
            (
                pipe(
                    (
                        pipe(sys.stdin.read())
                        >> InputStream
                        >> ChordsLexer
                        >> CommonTokenStream
                        >> ChordsParser
                    )().sheet()
                )
                >> ConcreteChordsVisitor().visit
                >> SheetXmlGenerator
            )().generate_xml()
        )
        >> print  # noqa: F633
    )


if __name__ == "__main__":
    main()
