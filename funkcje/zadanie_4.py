def formatuj(*args, **kwargs):
    tekst = "\n".join(args)
    for k, v in kwargs.items():
        tekst = tekst.replace(f"${k}", str(v))
    return tekst


def test_formatuj():
    actual = formatuj(
        'koszt $cena PLN',
        'kwota $cena brutto',
        cena=10,
    )
    expected = 'koszt 10 PLN\nkwota 10 brutto'
    assert actual == expected
