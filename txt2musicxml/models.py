from dataclasses import dataclass, field
from typing import List, Optional

from txt2musicxml.enums import Barline


class BaseNode:
    pass


@dataclass
class Leaf(BaseNode):
    value: str


@dataclass
class RootNote(Leaf):
    pass


@dataclass
class BassNote(Leaf):
    pass


@dataclass
class Alteration(Leaf):
    def __post_init__(self):
        self.value = self._convert_alteration_to_number_str()

    def _convert_alteration_to_number_str(self) -> str:
        is_all_flat = all([char == "b" for char in self.value])
        is_all_sharp = all(
            [char == "#" or char.lower() == "x" for char in self.value]
        )
        flats = self.value.count("b")
        sharps = (
            self.value.count("#")
            + 2 * self.value.count("X")
            + 2 * self.value.count("x")
        )
        if (
            (not sharps and not flats)
            or (sharps and flats)
            or (not is_all_flat and not is_all_sharp)
        ):
            print("Error, bad alteration string, converting to 0 steps")
            return "0"
        result = -1 * flats if flats else sharps
        return str(result)

    def convert_alteration_to_str_from_number(self) -> str:
        value = int(self.value)
        if value == 0:
            return ""
        elif value < 0:
            return abs(value) * "b"
        elif value == 1:
            return abs(value) * "#"
        elif value == 2:
            return abs(value) * "X"
        else:
            # TODO: what to do in such weird cases?
            return "???"


@dataclass
class RootAlteration(Alteration):
    pass


@dataclass
class BassAlteration(Alteration):
    pass


@dataclass
class Pitch(BaseNode):
    note: Leaf
    alteration: Optional[Leaf] = None


@dataclass
class Root(Pitch):
    note: RootNote
    alteration: Optional[RootAlteration] = None


@dataclass
class Bass(Pitch):
    note: BassNote
    alteration: Optional[BassAlteration] = None


@dataclass
class Suffix(Leaf):
    pass


@dataclass
class Chord(BaseNode):
    root: Root
    suffix: Optional[Suffix] = None
    bass: Optional[Bass] = None

    def __str__(self):
        chord_text = self.root.note.value if self.root.note else ""
        chord_text += (
            self.root.alteration.convert_alteration_to_str_from_number()
            if self.root.alteration
            else ""
        )
        chord_text += self.suffix.value if self.suffix else ""
        if self.bass:
            chord_text += "/"
            chord_text += self.bass.note.value if self.bass.note else ""
            chord_text += (
                self.bass.alteration.convert_alteration_to_str_from_number()
                if self.bass.alteration
                else ""
            )
        return chord_text


@dataclass
class MeasureRepeat(Leaf):
    value: str = "%"


@dataclass
class TimeSignature(BaseNode):
    numerator: int = 4
    denominator: int = 4


@dataclass
class Bar(BaseNode):
    chords: Optional[List[Chord]] = None
    chord_amount: int = field(init=False)
    measure_repeat: bool = False
    right_barline: Barline = Barline.REGULAR
    timesignature: TimeSignature = field(
        default_factory=TimeSignature
    )  # TODO: figure out time signature logic

    def __post_init__(self):
        if self.chords:
            self.chord_amount = len(self.chords)
        else:
            self.chord_amount = 0

    def to_list(
        self,
    ):  # TODO: should implement timesignature? does not for now
        if self.measure_repeat:
            return [str(MeasureRepeat())]
        else:
            return [str(chord) for chord in self.chords]


@dataclass
class Line(BaseNode):
    bars: List[Bar]

    def to_list(self):
        return [bar.to_list() for bar in self.bars]


@dataclass
class Sheet(BaseNode):
    lines: List[Line]

    def to_list(self):
        return [line.to_list() for line in self.lines]
