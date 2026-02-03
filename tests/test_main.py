import json
from unittest.mock import Mock

from src.main import json_to_object, open_json


# Тест если файл не найден
def test_open_json_not_found(capsys):
    open_json("operations.json")
    captured = capsys.readouterr()
    assert captured.out == "Файл не найден\n"


# Тест если файл пустой
def test_open_json_empty(capsys):
    open_json("empty.json")
    captured = capsys.readouterr()
    assert captured.out == "Ошибка декодирования\n"


# Тест списка словарей с данными (замоканный)
def test_open_json() -> None:
    my_mock = Mock(return_value=[{"category": "Phones"}, {"category": "TV"}])
    json.load = my_mock
    assert open_json("products.json") == [{"category": "Phones"}, {"category": "TV"}]


def test_json_to_object(all_categories:list[dict])-> None:
    assert json_to_object(all_categories)[0].name == "phones"


def test_json_to_object_2(all_categories:list[dict])-> None:
    assert json_to_object(all_categories)[1].name == "TV"


def test_json_to_object_3(all_categories:list[dict])-> None:
    assert json_to_object(all_categories)[0].description == "android"


def test_json_to_object_4(all_categories:list[dict])-> None:
    assert len(json_to_object(all_categories)[0].products) == 2
