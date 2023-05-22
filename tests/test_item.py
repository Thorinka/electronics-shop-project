"""Здесь надо написать тесты с использованием pytest для модуля item."""
import src
from src.item import InstantiateCSVError
from src.item import Item

item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)


def test___repr__():
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert repr(item2) == "Item('Ноутбук', 20000, 5)"


def test___str__():
    assert str(item1) == 'Смартфон'
    assert str(item2) == 'Ноутбук'


def test_calculate_total_price():
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000


def test_apply_discount():
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000.0
    item2.apply_discount()
    assert item2.price == 16000.0


def test_instantiate_from_csv():
    Item.all = []
    try:
        Item.instantiate_from_csv()
        assert len(Item.all) == 5
    except FileNotFoundError:
        assert Item.instantiate_from_csv() == FileNotFoundError("_Отсутствует файл item.csv_")
    except InstantiateCSVError:
        assert Item.instantiate_from_csv() == InstantiateCSVError("_Файл item.csv поврежден_")


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
