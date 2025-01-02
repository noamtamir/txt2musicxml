from abc import ABC
from dataclasses import dataclass, field
from itertools import count
from pathlib import Path
from typing import List, Optional, Protocol, Union
from xml.dom import minidom
from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement

from txt2musicxml.constants import (
    CHORDS_NAME_TO_XML_MATRIX,
    MIDDLE_LINE_ON_G_CLEF,
    MIDDLE_OCTAVE_ON_G_CLEF,
    MUSICXML_HEADERS,
    MUSICXML_TEMPLATE_FILENAME,
    NO_STEM,
    NOTE_TYPE_MAP,
    SLASH_NOTEHEAD,
)
from txt2musicxml.enums import Barline
from txt2musicxml.models import (
    Bar,
    BaseNode,
    Bass,
    BassAlteration,
    BassNote,
    Chord,
    Line,
    Root,
    RootAlteration,
    RootNote,
    Sheet,
    Suffix,
)


class XmlNodeGeneratorProtocol(Protocol):
    ast_node: BaseNode

    def generate_xml(self) -> Element: ...


class XmlRootGeneratorProtocol(Protocol):
    ast_node: BaseNode

    def generate_xml(self) -> str: ...


class XmlLeafGeneratorProtocol(Protocol):
    ast_node: BaseNode
    text: str
    tag: str

    def generate_xml(self) -> Element: ...


@dataclass
class BaseXmlLeafGenerator:
    ast_node: Union[RootNote, BassNote, RootAlteration, BassAlteration]
    tag: str
    text: str = field(init=False)

    def __post_init__(self):
        self.text = self.ast_node.value

    def generate_xml(self, **kwargs) -> Element:
        element = Element(self.tag, **kwargs)
        element.text = self.text
        return element


@dataclass
class RootNoteXmlGenerator(BaseXmlLeafGenerator):
    ast_node: RootNote
    tag: str = "root-step"


@dataclass
class BassNoteXmlGenerator(BaseXmlLeafGenerator):
    ast_node: BassNote
    tag: str = "bass-step"


@dataclass
class RootAlterationXmlGenerator(BaseXmlLeafGenerator):
    ast_node: RootAlteration
    tag: str = "root-alter"


@dataclass
class BassAlterationXmlGenerator(BaseXmlLeafGenerator):
    ast_node: BassAlteration
    tag: str = "bass-alter"


class PitchXmlGeneratorProtocol(Protocol):
    note_xml_generator: Union[RootNoteXmlGenerator, BassNoteXmlGenerator]
    alteration_xml_generator: Union[
        RootAlterationXmlGenerator, BassAlterationXmlGenerator
    ]


class PitchXmlGeneratorMixin(ABC):
    note_xml_generator: Union[RootNoteXmlGenerator, BassNoteXmlGenerator]
    alteration_xml_generator: Union[
        RootAlterationXmlGenerator, BassAlterationXmlGenerator, None
    ]
    tag: str

    def generate_xml(self) -> Element:
        element = Element(self.tag)
        element.append(self.note_xml_generator.generate_xml())
        if self.alteration_xml_generator:
            element.append(self.alteration_xml_generator.generate_xml())
        return element


@dataclass
class RootXmlGenerator(PitchXmlGeneratorMixin):
    ast_node: Root
    note_xml_generator: RootNoteXmlGenerator = field(init=False)
    alteration_xml_generator: Union[RootAlterationXmlGenerator, None] = None
    tag: str = "root"

    def __post_init__(self):
        self.note_xml_generator = RootNoteXmlGenerator(self.ast_node.note)
        if self.ast_node.alteration:
            self.alteration_xml_generator = RootAlterationXmlGenerator(
                self.ast_node.alteration
            )


@dataclass
class BassXmlGenerator(PitchXmlGeneratorMixin):
    ast_node: Bass
    note_xml_generator: BassNoteXmlGenerator = field(init=False)
    alteration_xml_generator: Union[BassAlterationXmlGenerator, None] = None
    tag: str = "bass"

    def __post_init__(self):
        self.note_xml_generator = BassNoteXmlGenerator(self.ast_node.note)
        if self.ast_node.alteration:
            self.alteration_xml_generator = BassAlterationXmlGenerator(
                self.ast_node.alteration
            )


@dataclass
class SuffixXmlGenerator:
    ast_node: Optional[Suffix]
    chord_type: dict = field(init=False)

    def __post_init__(self):
        self.chord_type = {"kind": "major"}
        if self.ast_node:
            chords_map = index_chords(CHORDS_NAME_TO_XML_MATRIX)
            self.chord_type = chords_map.get(
                self.ast_node.value, {"kind": "major"}
            )

    def generate_xml(self) -> List[Element]:
        elements = []
        kind_element = Element("kind", {"use-symbols": "yes"})
        kind_element.text = self.chord_type.get("kind", "major")
        elements.append(kind_element)
        degrees = self.chord_type.get("degrees")
        if degrees:
            for degree in degrees:
                degree_element = Element("degree")
                degree_value_element = SubElement(
                    degree_element, "degree-value"
                )
                degree_value_element.text = degree.get("degree-value")
                degree_alter_element = SubElement(
                    degree_element, "degree-alter"
                )
                degree_alter_element.text = degree.get("degree-alter")
                degree_type_element = SubElement(degree_element, "degree-type")
                degree_type_element.text = degree.get("degree-type", "alter")
                elements.append(degree_element)
        return elements


@dataclass
class ChordXmlGenerator:
    ast_node: Chord
    duration: int
    quarter_note_divisions: int

    def generate_xml(self) -> list[Element]:
        harmony_element = Element("harmony")
        harmony_element.append(
            RootXmlGenerator(self.ast_node.root).generate_xml()
        )
        harmony_element.extend(
            SuffixXmlGenerator(self.ast_node.suffix).generate_xml()
        )
        if self.ast_node.bass:
            harmony_element.append(
                BassXmlGenerator(self.ast_node.bass).generate_xml()
            )

        note_element = Element("note")
        pitch_element = SubElement(note_element, "pitch")
        pitch_step_element = SubElement(pitch_element, "step")
        pitch_step_element.text = MIDDLE_LINE_ON_G_CLEF
        pitch_octave_element = SubElement(pitch_element, "octave")
        pitch_octave_element.text = MIDDLE_OCTAVE_ON_G_CLEF
        duration_per_divisions = self.duration / self.quarter_note_divisions
        if (
            duration_per_divisions > 1
        ):  # add slashes instead of full note duration
            self.duration = self.quarter_note_divisions  # quarter note
        duration_element = SubElement(note_element, "duration")
        duration_element.text = str(self.duration)
        type_element = SubElement(note_element, "type")
        type_element.text = NOTE_TYPE_MAP.get(
            duration_per_divisions, "quarter"
        )
        if duration_per_divisions >= 1:
            stem_element = SubElement(note_element, "stem")
            stem_element.text = NO_STEM
        notehead_element = SubElement(note_element, "notehead")
        notehead_element.text = SLASH_NOTEHEAD
        extra_slashes: list[Element] = []
        if (
            duration_per_divisions > 1
        ):  # add slashes instead of full note duration
            amount_of_slashes = int(duration_per_divisions - 1)
            for _ in range(amount_of_slashes):
                extra_slashes.append(self._add_slash())
        return [harmony_element, note_element] + extra_slashes

    def _add_slash(self):
        note_element = Element("note")
        pitch_element = SubElement(note_element, "pitch")
        pitch_step_element = SubElement(pitch_element, "step")
        pitch_step_element.text = MIDDLE_LINE_ON_G_CLEF
        pitch_octave_element = SubElement(pitch_element, "octave")
        pitch_octave_element.text = MIDDLE_OCTAVE_ON_G_CLEF
        duration = self.quarter_note_divisions  # quarter note
        duration_element = SubElement(note_element, "duration")
        duration_element.text = str(duration)
        type_element = SubElement(note_element, "type")
        type_element.text = "quarter"
        stem_element = SubElement(note_element, "stem")
        stem_element.text = NO_STEM
        notehead_element = SubElement(note_element, "notehead")
        notehead_element.text = SLASH_NOTEHEAD
        return note_element


@dataclass
class BarXmlGenerator:
    ast_node: Bar
    divisions: int = field(init=False)
    chord_durations: List[int] = field(init=False)

    def __post_init__(self):
        self._validate_timesignature_denominator()
        if not self.ast_node.measure_repeat:
            self._calculate_rhythm()

    def generate_xml(
        self,
        new_line: bool,
        bar_counter: count,
        is_first_bar_in_sheet: bool = False,
        is_prev_repeat: bool = False,
    ) -> Element:
        measure_element = Element("measure")
        measure_element.attrib["number"] = str(next(bar_counter))
        if new_line:
            SubElement(measure_element, "print", {"new-system": "yes"})
        attributes_element = SubElement(measure_element, "attributes")
        if is_prev_repeat and not self.ast_node.measure_repeat:
            measure_style_element = SubElement(
                attributes_element, "measure-style"
            )
            measure_repeat_element = SubElement(
                measure_style_element, "measure-repeat"
            )
            measure_repeat_element.attrib["type"] = "stop"
            measure_repeat_element.text = "1"
        if not self.ast_node.measure_repeat:
            divisions_element = SubElement(attributes_element, "divisions")
            divisions_element.text = str(self.divisions)
        if is_first_bar_in_sheet:
            key_element = SubElement(
                attributes_element, "key"
            )  # TODO: add key signature support?
            fifths_element = SubElement(key_element, "fifths")
            fifths_element.text = "0"
            mode_element = SubElement(key_element, "mode")
            mode_element.text = "major"
            time_element = SubElement(attributes_element, "time")
            beats_element = SubElement(time_element, "beats")
            beats_element.text = str(self.ast_node.timesignature.numerator)
            beat_type_element = SubElement(time_element, "beat-type")
            beat_type_element.text = str(self.ast_node.timesignature.numerator)
            clef_element = SubElement(attributes_element, "clef")
            sign_element = SubElement(clef_element, "sign")
            sign_element.text = "G"
            line_element = SubElement(clef_element, "line")
            line_element.text = "2"
        if self.ast_node.chords:
            chord_elements: list[Element] = []
            for duration_and_chord in list(
                zip(self.ast_node.chords, self.chord_durations)
            ):
                chord_elements.extend(
                    ChordXmlGenerator(
                        duration_and_chord[0],
                        duration_and_chord[1],
                        self.divisions,
                    ).generate_xml()
                )
            measure_element.extend(chord_elements)
        elif self.ast_node.measure_repeat:
            measure_style_element = SubElement(
                attributes_element, "measure-style"
            )
            measure_repeat_element = SubElement(
                measure_style_element, "measure-repeat"
            )
            measure_repeat_element.attrib["type"] = "start"
            measure_repeat_element.text = "1"
        if (
            self.ast_node.right_barline != Barline.REGULAR
        ):  # implicit when it is a regular barline
            right_barline = self._generate_barline(self.ast_node.right_barline)
            measure_element.append(right_barline)
        return measure_element

    def _generate_barline(self, barline: Barline) -> Element:
        BAR_STYLE_BARLINE_MAP = {
            Barline.REGULAR: "regular",
            Barline.DOUBLE: "light-heavy",
            Barline.REPEAT: "light-heavy",
        }

        barline_element = Element("barline")  # location is implicitly right
        if barline is not Barline.REGULAR:  # regular barline is implicit
            bar_style = Element("bar-style")
            bar_style.text = BAR_STYLE_BARLINE_MAP.get(barline, "regular")
            barline_element.append(bar_style)
        if barline is Barline.REPEAT:
            repeat = Element(
                "repeat", {"direction": "backward"}
            )  # only support backward repeat for now
            barline_element.append(repeat)
        return barline_element

    def _validate_timesignature_denominator(self):
        # TODO: handle error
        assert is_power_of_2(int(self.ast_node.timesignature.denominator))

    def _calculate_rhythm(self):
        numerator = self.ast_node.timesignature.numerator
        denominator = self.ast_node.timesignature.denominator
        chord_amount = self.ast_node.chord_amount
        divisions = int(denominator / 4)
        if numerator < chord_amount:
            divisions *= 2
        divisions_in_bar = numerator * divisions
        self.divisions = divisions
        temp_chord_durations = [1] * chord_amount
        self.chord_durations = self._calculate_durations(
            temp_chord_durations, divisions_in_bar
        )

    def _calculate_durations(
        self, durations: List[int], divisions_in_bar: int
    ):
        # initial durations = [1] * chord_amount
        # TODO: make this work for dotted groupings (i.e. 6/8, 9/8)
        temp_durations = durations.copy()
        for i, _ in enumerate(temp_durations):
            if sum(temp_durations) == divisions_in_bar:
                return temp_durations
            else:
                temp_durations[i] += 1
        if not sum(temp_durations) == divisions_in_bar:
            return self._calculate_durations(temp_durations, divisions_in_bar)
        return temp_durations

    def _calculate_durations_2(
        self, durations: List[int], divisions_in_bar: int, chord_amount: int
    ):
        # initial durations = [1] * divisions_in_bar
        if len(durations) == chord_amount:
            return durations
        temp_durations = durations.copy()
        for i, _ in enumerate(range(divisions_in_bar - chord_amount)):
            try:
                temp_durations[i] += temp_durations.pop(i)
            except IndexError:
                return self._calculate_durations_2(
                    temp_durations, divisions_in_bar, chord_amount
                )
        return self._calculate_durations_2(
            temp_durations, divisions_in_bar, chord_amount
        )


@dataclass
class LineXmlGenerator:
    ast_node: Line

    def generate_xml(
        self,
        is_first_line: bool,
        bar_counter: count,
        is_prev_repeat: bool = False,
    ) -> tuple[list[Element], bool]:
        bar_elements = []
        # is_prev_repeat = False
        for i, bar in enumerate(self.ast_node.bars):
            new_line = False
            is_first_bar = is_first(i)
            if is_first_bar and not is_first_line:
                new_line = True
            is_first_bar_in_sheet = False
            if is_first_bar and is_first_line:
                is_first_bar_in_sheet = True
            bar_elements.append(
                BarXmlGenerator(bar).generate_xml(
                    new_line,
                    bar_counter,
                    is_first_bar_in_sheet,
                    is_prev_repeat,
                )
            )
            if bar.measure_repeat:
                is_prev_repeat = True
            else:
                is_prev_repeat = False
        return bar_elements, is_prev_repeat


@dataclass
class SheetXmlGenerator:
    ast_node: Sheet
    bar_counter: count = field(init=False)
    xml_root: Element = field(init=False)

    def __post_init__(self):
        self.bar_counter = count(1)

    def generate_xml(self) -> str:
        xml_root = self._init_musicxml_tree()
        part_element: Element = xml_root.find("part")  # type: ignore # noqa: E501
        bar_elements: list[Element] = []
        is_prev_repeat = False
        for i, line in enumerate(self.ast_node.lines):
            is_first_line = is_first(i)
            line_xml, is_prev_repeat = LineXmlGenerator(line).generate_xml(
                is_first_line, self.bar_counter, is_prev_repeat
            )
            bar_elements.extend(line_xml)
        part_element.extend(bar_elements)
        return self._to_string(MUSICXML_HEADERS, xml_root)

    @staticmethod
    def _init_musicxml_tree() -> Element:
        filepath = Path(__file__).parent / MUSICXML_TEMPLATE_FILENAME
        tree = ElementTree.parse(filepath)
        return tree.getroot()

    @staticmethod
    def _to_string(xml_headers, xml_root):
        return (
            xml_headers
            + "\n"
            + ElementTree.tostring(xml_root, encoding="unicode")
        )

    @staticmethod
    def write_xml_to_file(text, output_file_path):
        dom = minidom.parseString(text)
        pretty_xml_as_string = dom.toprettyxml(encoding="utf-8").decode(
            "utf-8"
        )
        with open(output_file_path, "w") as f:
            f.write(pretty_xml_as_string)


def is_first(x: int) -> bool:
    return True if x == 0 else False


def is_power_of_2(n: int) -> bool:
    n = int(n)
    return (n & (n - 1) == 0) and n != 0


def index_chords(chords_list):
    # converts CHORDS_NAME_TO_XML_MATRIX into a dictionary
    # indexed by chord name
    from copy import copy

    chords_dict = {}
    for chord in chords_list:
        for name in chord["names"]:
            c = copy(chord)
            del c["names"]
            chords_dict[name] = c
    return chords_dict
