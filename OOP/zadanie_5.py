class CashMachine:

    def __init__(self):
        self._money = []

    @property
    def is_avaiable(self):
        if len(self._money) == 0:
            return False
        return True

    def put_money(self, money):
        self._money.extend(money)

    def withdraw_money(self, amount):
        money_to_withdraw = []
        for bill in sorted(self._money, reverse=True):
            if sum(money_to_withdraw) + bill <= amount:
                money_to_withdraw.append(bill)

        if sum(money_to_withdraw) != amount:
            return []

        for bill in money_to_withdraw:
            self._money.remove(bill)

        return money_to_withdraw


def test_cash_machine_not_avaiable():
    cs = CashMachine()
    assert cs.is_avaiable is False


def test_cash_machine_put_money():
    cs = CashMachine()
    cs.put_money([50])
    assert cs.is_avaiable is True


def test_cash_machine_withdraw_money():
    cs = CashMachine()
    cs.put_money([100, 200, 200, 100, 50])
    assert cs.withdraw_money(150) == [100, 50]
    assert cs.withdraw_money(150) == []


def test_cash_machine_withdraw_money_2():
    cs = CashMachine()
    cs.put_money([20, 100, 200, 200, 100, 50])
    assert cs.withdraw_money(150) == [100, 50]
    assert cs.withdraw_money(150) == []
