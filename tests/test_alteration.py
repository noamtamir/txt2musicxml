from txt2musicxml.models import Alteration

FLAT = "b"
SHARP = "#"
DOUBLE_SHARP = "x"
CAPITAL_DOUBLE_SHARP = "X"


def test_convert_alteration_to_number_1_flat():
    number_of_accidentals = 1
    alteration = Alteration(number_of_accidentals * FLAT)
    alteration.value == "-" + str(number_of_accidentals)


def test_convert_alteration_to_number_2_flats():
    number_of_accidentals = 2
    alteration = Alteration(number_of_accidentals * FLAT)
    alteration.value == "-" + str(number_of_accidentals)


def test_convert_alteration_to_number_1_sharp():
    number_of_accidentals = 1
    alteration = Alteration(number_of_accidentals * SHARP)
    alteration.value == str(number_of_accidentals)


def test_convert_alteration_to_number_2_sharps():
    number_of_accidentals = 2
    alteration = Alteration(number_of_accidentals * SHARP)
    alteration.value == str(number_of_accidentals)


def test_convert_alteration_to_number_double_sharp():
    number_of_accidentals = 1
    alteration = Alteration(number_of_accidentals * DOUBLE_SHARP)
    alteration.value == str(2 * number_of_accidentals)


def test_convert_alteration_to_number_2_double_sharps():
    number_of_accidentals = 2
    alteration = Alteration(number_of_accidentals * DOUBLE_SHARP)
    alteration.value == str(2 * number_of_accidentals)


def test_convert_alteration_to_number_double_sharp_capital():
    number_of_accidentals = 1
    alteration = Alteration(number_of_accidentals * CAPITAL_DOUBLE_SHARP)
    alteration.value == str(2 * number_of_accidentals)


def test_convert_alteration_to_number_no_alterations():
    alteration = Alteration("test")
    alteration.value == "0"


def test_convert_alteration_to_number_mixed_alterations():
    alteration = Alteration("b#Xb")
    alteration.value == "0"


def test_convert_alteration_to_number_mixed_illigal_alterations():
    alteration = Alteration("baab")
    alteration.value == "0"
