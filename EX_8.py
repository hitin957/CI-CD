class MoneyError(Exception):
    def init(self, sender_balance, receiver_balance):
        self.sender_balance = sender_balance
        self.receiver_balance = receiver_balance
        self.message = f"Ошибка: Не удается перевести деньги с баланса отправителя ({sender_balance}) на баланс получателя ({receiver_balance})."


def __str__(self):
    return self.message


def transfer_money(sender_balance, receiver_balance, amount):
    if amount < 0:
        raise MoneyError(sender_balance, receiver_balance)


try:
    transfer_money(1000, 500, -100)
except MoneyError as e:
    print(e)