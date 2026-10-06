import pytest
from string_utils import StringUtils


@pytest.mark.capitalize_test_pozitive
@pytest.mark.parametrize("input_text, expected_output",
                         [("cкайпро", "Cкайпро"),
                          ("домашка", "Домашка."),
                          ("love", "Love"), ],
                         )
def test_capitalize_pozitive(input_text: str, expected_output: str):
    stroka = StringUtils()
    assert stroka.capitalize(input_text) == expected_output


@pytest.mark.capitalize_test_negative
@pytest.mark.parametrize("input_text, expected_output",
                         [("Кот ", " Кот "),
                          ("домашка сложно", " Домашка сложно"),
                          ("   ", "love"),
                          ("1020", "1020"),
                          (" ", " "),
                          (None, "Лужа")
                          ]
                         )
def test_capitalize_negative(input_text: str, expected_output: str):
    stroka = StringUtils()
    assert stroka.capitalize(input_text) == expected_output


@pytest.mark.trim_test_pozitive
@pytest.mark.parametrize("input_text_probel, expected_text",
                         [(" Клавиатура", "Клавиатура"),
                          ("     Мышь", "Мышь"),
                          (" 123", "123"),
                          ]
                         )
def test_trim_pozitive(input_text_probel, expected_text):
    probel = StringUtils()
    assert probel.trim(input_text_probel) == expected_text


@pytest.mark.trim_test_negative
@pytest.mark.parametrize("input_text_negative, expected_text_negative",
                         [("Зеркало  ", "Зеркало"),
                          (" Х леб", "Х леб"),
                          (" Я 1", "Я 1"),
                          ]
                         )
def test_trim_negative(input_text_negative, expected_text_negative):
    neg_prov = StringUtils()
    assert neg_prov(input_text_negative) == expected_text_negative


@pytest.mark.search_symbol_pozitive
@pytest.mark.parametrize("input_symbol, symbol, expected_string",
                         [("Ковер", "в", True),
                          ("Стена", "а", True),
                          ("Flower", "F", True),
                          ("Питон это змея", "з", True),
                          ("04", "0", True),
                          ]
                         )
def test_contains_pozitive(input_symbol, symbol, expected_string):
    cont_poz = StringUtils()
    exp = cont_poz.contains(input_symbol, symbol)
    assert exp == expected_string


@pytest.mark.search_symbol_negative
@pytest.mark.parametrize("input_symbol, symbol, expected_string",
                         [("Box", "S", False),
                          ("Ручка", "РУ", False),
                          ("Обои", " ", True),
                          ("Учебник", "123", True),
                          ("  ", "   ", True),
                          ]
                         )
def test_contains_negative(input_symbol, symbol, expected_string):
    cont_neg = StringUtils()
    exp = cont_neg.contains(input_symbol, symbol)
    assert exp == expected_string


@pytest.mark.delete_symbol_pozitive
@pytest.mark.parametrize("input_string, symbol, expected_string",
                         [("Бокс", "с", "Бок"),
                          ("Кобра", "б", "Кора"),
                          ("Бык", "Б", "ык"),
                          ("1997", "1", "997"),
                          ("Луна в окне", "н", "Луа в оке"),
                          ]
                         )
def test_delete_pozitive(input_string, symbol, expected_string):
    poz_prov_del = StringUtils()
    assert poz_prov_del.delete_symbol(input_string, symbol) == expected_string


@pytest.mark.delete_symbol_negative
@pytest.mark.parametrize("input_string, symbol, expected_string",
                         [("   ", " ", "     "),
                          (" ", "б", "   "),
                          ("Кошка   ", "  ", "  Кошка"),
                          ("1997", "10", "1997"),
                          ("Солнце на горизонте", "Ж", "Солнце на горизонте"),
                          ]
                         )
def test_delete_negative(input_string, symbol, expected_string):
    neg_prov_del = StringUtils()
    assert neg_prov_del.delete_symbol(input_string, symbol) == expected_string
