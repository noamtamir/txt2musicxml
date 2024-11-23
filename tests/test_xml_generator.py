from tests.mock_sheet import mock_sheet
from txt2musicxml.xml_generator import (SheetXmlGenerator, is_first,
                                        is_power_of_2)


# TODO: add more tests to generator
def test_generate_sheet():
    sheet = mock_sheet()
    sheet_xml_generator = SheetXmlGenerator(sheet)
    result = sheet_xml_generator.generate_xml()
    with open("tests/xml_files/aguas_de_marco_snippet.musicxml", "r") as f:
        expected = f.read()
    expected == result


def test_is_first_0():
    assert is_first(0) is True


def test_is_first_fail():
    assert is_first(1) is False
    assert is_first(12) is False
    assert is_first(-12) is False
    assert is_first("0") is False


def test_is_power_of_2():
    assert is_power_of_2(1) is True
    assert is_power_of_2(2) is True
    assert is_power_of_2("2") is True
    assert is_power_of_2(4) is True
    assert is_power_of_2(8) is True
    assert is_power_of_2(16) is True
    assert is_power_of_2(32) is True
    assert is_power_of_2(64) is True
    assert is_power_of_2(128) is True


def test_is_power_of_2_fail():
    assert is_power_of_2(0) is False
    assert is_power_of_2(3) is False
    assert is_power_of_2(11) is False
    assert is_power_of_2(100) is False
    assert is_power_of_2(-13) is False
    assert is_power_of_2("3") is False
