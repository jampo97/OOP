import pytest


def test_product_iterator(product_iterator):
    assert product_iterator.index == -1
    assert product_iterator.products == ["Продукт2 10 руб. Остаток: 6 шт.", "Продукт1 15 руб. Остаток: 12 шт.", ""]
    assert product_iterator.category.name == "Название категории"
    assert next(product_iterator) == "Продукт2 10 руб. Остаток: 6 шт."
    assert product_iterator.index == 0
    assert next(product_iterator) == "Продукт1 15 руб. Остаток: 12 шт."
    assert product_iterator.index == 1
    assert next(product_iterator) == ""
    assert product_iterator.index == 2
    with pytest.raises(StopIteration):
        assert next(product_iterator) == ""
    #
    #     next(product_iterator)


def test_product_iterator_none(product_iterator_none) -> None:

    assert product_iterator_none.products == [""]
