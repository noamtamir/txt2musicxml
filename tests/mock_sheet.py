from models import (Bar, Bass, BassAlteration, BassNote, Chord, Line, Root,
                    RootAlteration, RootNote, Sheet, Suffix)


def mock_sheet():
    return Sheet(
        [
            Line(
                [
                    Bar(
                        [
                            Chord(
                                Root(RootNote("B"), RootAlteration("b")),
                                None,
                                Bass(BassNote("A"), BassAlteration("b")),
                            )
                        ]
                    ),
                    Bar(
                        [
                            Chord(
                                Root(RootNote("B"), RootAlteration("b")),
                                None,
                                Bass(BassNote("A"), BassAlteration("b")),
                            )
                        ]
                    ),
                    Bar([Chord(Root(RootNote("G")), Suffix("m6"))]),
                    Bar(
                        [
                            Chord(
                                Root(RootNote("C")),
                                Suffix("m7b5"),
                                Bass(BassNote("G"), BassAlteration("b")),
                            )
                        ]
                    ),
                ]
            ),
            Line(
                [
                    Bar(
                        [
                            Chord(
                                Root(RootNote("B"), RootAlteration("b")),
                                None,
                                Bass(BassNote("A"), BassAlteration("b")),
                            ),
                            Chord(
                                Root(RootNote("B"), RootAlteration("b")),
                                None,
                                Bass(BassNote("A"), BassAlteration("b")),
                            ),
                        ]
                    ),
                    Bar(
                        [
                            Chord(Root(RootNote("G")), Suffix("m6")),
                            Chord(
                                Root(RootNote("C")),
                                Suffix("m7b5"),
                                Bass(BassNote("G"), BassAlteration("b")),
                            ),
                        ]
                    ),
                ]
            ),
        ]
    )
