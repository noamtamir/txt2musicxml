MIDDLE_LINE_ON_G_CLEF = "B"
MIDDLE_OCTAVE_ON_G_CLEF = "4"
NO_STEM = "none"
SLASH_NOTEHEAD = "slash"
MUSICXML_TEMPLATE_FILENAME = "empty_template.xml"
MUSICXML_HEADERS = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">"""  # noqa: E501

NOTE_TYPE_MAP = {
    # 4: "whole",
    # 2: "half",
    1: "quarter",
    1 / 2: "eighth",
    1 / 4: "16th",
    1 / 8: "32nd",
}

CHORDS_NAME_TO_XML_MATRIX = [
    {"kind": "major", "names": [""]},
    {"kind": "power", "names": ["5"]},
    {"kind": "suspended-second", "names": ["sus2"]},
    {"kind": "suspended-fourth", "names": ["sus4"]},
    {"kind": "major-sixth", "names": ["6"]},
    {"kind": "major-seventh", "names": ["^", "^7", "maj7"]},
    {"kind": "major-ninth", "names": ["^9", "maj9"]},
    {"kind": "major-11th", "names": ["^11", "maj11"]},
    {"kind": "major-13th", "names": ["^13", "maj13"]},
    {"kind": "dominant", "names": ["7"]},
    {"kind": "dominant-ninth", "names": ["7,9", "9"]},
    {"kind": "dominant-11th", "names": ["11"]},
    {"kind": "dominant-13th", "names": ["13"]},
    {
        "degrees": [{"degree-alter": "-1", "degree-value": "5"}],
        "kind": "dominant",
        "names": ["7b5"],
    },
    {
        "degrees": [{"degree-alter": "-1", "degree-value": "9"}],
        "kind": "dominant",
        "names": ["7b9"],
    },
    {
        "degrees": [{"degree-alter": "1", "degree-value": "9"}],
        "kind": "dominant",
        "names": ["7#9"],
    },
    {
        "degrees": [{"degree-alter": "0", "degree-value": "13"}],
        "kind": "dominant",
        "names": ["7,13", "7add13"],
    },
    {
        "degrees": [
            {"degree-alter": "-1", "degree-value": "9"},
            {"degree-alter": "-1", "degree-value": "13"},
        ],
        "kind": "dominant",
        "names": ["b9b13", "7b9b13"],
    },
    {
        "degrees": [
            {"degree-alter": "0", "degree-value": "9"},
            {"degree-alter": "0", "degree-value": "13"},
        ],
        "kind": "dominant",
        "names": ["9,13", "7,9,13"],
    },
    {
        "degrees": [
            {"degree-alter": "-1", "degree-value": "9"},
            {"degree-alter": "0", "degree-value": "13"},
        ],
        "kind": "dominant",
        "names": ["7b9,13", "b9,13"],
    },
    {
        "degrees": [
            {"degree-alter": "0", "degree-value": "9"},
            {"degree-alter": "-1", "degree-value": "5"},
        ],
        "kind": "dominant",
        "names": ["9b5", "7,9b5"],
    },
    {
        "degrees": [
            {"degree-alter": "0", "degree-value": "9"},
            {"degree-alter": "-1", "degree-value": "13"},
        ],
        "kind": "dominant",
        "names": ["7,9b13", "9b13"],
    },
    {"kind": "augmented", "names": ["+", "aug", "#5"]},
    {"kind": "augmented-seventh", "names": ["+7", "aug7", "7#5"]},
    {
        "degrees": [{"degree-alter": "1", "degree-value": "7"}],
        "kind": "augmented-seventh",
        "names": ["+maj7", "+M7", "augM7"],
    },
    {
        "degrees": [{"degree-alter": "0", "degree-value": "9"}],
        "kind": "augmented-seventh",
        "names": ["+9", "aug9", "9#5"],
    },
    {
        "degrees": [
            {"degree-alter": "0", "degree-value": "9"},
            {"degree-alter": "1", "degree-value": "11"},
        ],
        "kind": "augmented-seventh",
        "names": ["+#11", "+9#11", "aug#11", "aug9#11", "9#11#5"],
    },
    {"kind": "minor", "names": ["-", "m"]},
    {"kind": "minor-sixth", "names": ["-6", "m6"]},
    {"kind": "minor-seventh", "names": ["-7", "m7"]},
    {"kind": "minor-ninth", "names": ["-9", "m9"]},
    {"kind": "minor-11th", "names": ["-11", "m11"]},
    {"kind": "minor 13th", "names": ["-13", "m13"]},
    {
        "kind": "major-minor",
        "names": ["-^", "-^7", "-maj", "-maj7", "mmaj", "mmaj7", "m^", "m^7"],
    },
    {
        "degrees": [{"degree-alter": "0", "degree-value": "9"}],
        "kind": "major-minor",
        "names": ["-^9", "m^9", "-maj9", "mmaj9"],
    },
    {
        "degrees": [
            {"degree-alter": "0", "degree-value": "9"},
            {"degree-alter": "1", "degree-value": "11"},
        ],
        "kind": "major-minor",
        "names": ["-^#11", "m^#11", "-maj#11", "mmaj#11"],
    },
    {
        "degrees": [
            {"degree-alter": "0", "degree-value": "9"},
            {"degree-alter": "1", "degree-value": "11"},
            {"degree-alter": "0", "degree-value": "13"},
        ],
        "kind": "major-minor",
        "names": ["-^#11,13", "m^#11,13", "-maj#11,13", "mmaj#11,13"],
    },
    {"kind": "diminished", "names": ["dim", "mb5", "-b5"]},
    {"kind": "diminished-seventh", "names": ["dim7", "o", "o7"]},
    {"kind": "half-diminished", "names": ["m7b5", "-7b5", "ø", "ø7"]},
    {
        "degrees": [{"degree-alter": "1", "degree-value": "7"}],
        "kind": "diminished-seventh",
        "names": ["ømaj7", "mmaj7b5", "-maj7b5", "-^7b5", "m^7b5", "ø^7"],
    },
]
