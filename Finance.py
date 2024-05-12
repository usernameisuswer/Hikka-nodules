# meta developer:@DieModules

from .. import loader, utils
from telethon.tl.custom import Message

@loader.tds
class FinanceModule(loader.Module):
    """Модуль для учета финансов"""
    strings = {
        "name": "FinanceModule",
        "balance": "Текущий баланс: {}",
        "income_added": "Доход добавлен: {}",
        "expense_added": "Расход добавлен: {}",
        "invalid_amount": "Неверная сумма.",
        "insufficient_funds": "Недостаточно средств для этой операции."
    }

    async def client_ready(self, client, db):
        self.db = db

    async def balancecmd(self, message: Message):
        """Показать текущий баланс"""
        balance = self.db.get(self.strings["name"], "balance", 0)
        await utils.answer(message, self.strings["balance"].format(balance))

    async def incomecmd(self, message: Message):
        """Добавить доход: .income сумма"""
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, self.strings["invalid_amount"])
            return
        try:
            amount = float(args)
        except ValueError:
            await utils.answer(message, self.strings["invalid_amount"])
            return
        balance = self.db.get(self.strings["name"], "balance", 0)
        balance += amount
        self.db.set(self.strings["name"], "balance", balance)
        await utils.answer(message, self.strings["income_added"].format(amount))

    async def expensecmd(self, message: Message):
        """Добавить расход: .expense сумма"""
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, self.strings["invalid_amount"])
            return
        try:
            amount = float(args)
        except ValueError:
            await utils.answer(message, self.strings["invalid_amount"])
            return
        balance = self.db.get(self.strings["name"], "balance", 0)
        
        if balance - amount < 0:
            await utils.answer(message, self.strings["insufficient_funds"])
            return
        
        balance -= amount
        self.db.set(self.strings["name"], "balance", balance)
        await utils.answer(message, self.strings["expense_added"].format(amount))
        