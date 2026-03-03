def test_print_mixin_product(capsys, product_my):
    product_my
    captured = capsys.readouterr()
    assert "Product(Продукт1, 0, 2)" in captured.out


def test_print_mixin_smartphone(capsys, smartphone):
    smartphone
    captured = capsys.readouterr()
    assert "Smartphone(Название смартфона, 999.99, 10)" in captured.out


def test_print_mixin_lawn_grasst(capsys, lawn_grass):
    lawn_grass
    captured = capsys.readouterr()
    assert "LawnGrass(Название травы, 999.99, 10)" in captured.out
