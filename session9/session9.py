# 1.
class Person:

    def __init__(self, fn, ln):
        self.first_name = fn
        self.last_name = ln
        self.address = None  # addresses stored as strings

    def set_address(self, adr):
        self.address = adr  # strings


class IndividualBankAccount:

    def __init__(self, sort_code, account_number, owner):
        self.bank_account = {'Sort code': sort_code, 'Account number': account_number,
                             'Owner': f'{owner.first_name } {owner.last_name}'}

    def set_sort_code(self, sort_code):
        self.bank_account['Sort code'] = sort_code

    def get_sort_code(self):
        return (self.bank_account['Sort code'])

    def set_account_number(self, account_number):

        self.bank_account['Account number'] = account_number

    def get_account_number(self):
        return (self.bank_account['Account number'])

    def get_account_data(self):
        return (f"{self.bank_account['Owner']} {self.bank_account['Sort code']} {self.bank_account['Account number']}")


class SharedBankAccount:
    def __init__(self, sort_code, account_number, owners):
        self.account_owners = []
        for owner in owners:
            self.account_owners.append(f'{owner.first_name} {owner.last_name}')
        self.bank_account = {'Sort code': sort_code, 'Account number': account_number,
                             'Owners': f"{', '.join(self.account_owners)}"}

    def set_sort_code(self, sort_code):
        self.bank_account['Sort code'] = sort_code

    def get_sort_code(self):
        return (self.bank_account['Sort code'])

    def set_account_number(self, account_number):
        self.bank_account['Account number'] = account_number

    def get_account_number(self):
        return (self.bank_account['Account number'])

    def get_account_data(self):
        return (f"{self.bank_account['Owners']}, {self.bank_account['Sort code']} {self.bank_account['Account number']}")


john01 = Person("John", "Doe")
john01.set_address("Birkbeck, Malet st., WC1E 7HX")
john01s_account = IndividualBankAccount("12-34-56", "12345678", john01)
john01s_account.set_sort_code("11-11-11")

mary01 = Person("Mary", "Ann")
mary01.set_address("UCL, Gower st., WC1E 6BT")
mary01s_account = IndividualBankAccount("65-43-21", "87654321", mary01)
mary01s_account.set_account_number("99999999")

acc02 = SharedBankAccount("11-22-33", "11223344", [john01, mary01])
print(acc02.get_account_data())

# 2. With inheritance


class Person:
    def __init__(self, fn, ln):
        self.first_name = fn
        self.last_name = ln
        self.address = None  # addresses stored by strings

    def set_address(self, adr):
        self.address = adr  # strings


class BankAccount:
    def __init__(self, sort_code, account_number):
        self.bank_account = {'Sort code': sort_code,
                             'Account number': account_number}

    def set_sort_code(self, sort_code):
        self.bank_account['Sort code'] = sort_code

    def get_sort_code(self):
        return (self.bank_account['Sort code'])

    def set_account_number(self, account_number):
        self.bank_account['Account number'] = account_number

    def get_account_number(self):
        return (self.bank_account['Account number'])

    def get_account_data(self):
        return (f"{self.bank_account['Sort code']} {self.bank_account['Account number']}")


class IndividualBankAccount(BankAccount):
    def __init__(self, sort_code, account_number, owner):
        super().__init__(sort_code, account_number)
        self.owner = f"{owner.first_name} {owner.last_name}"

    def get_account_data(self):
        return f'{self.owner} {super().get_account_data()}'


class SharedBankAccount(BankAccount):
    def __init__(self, sort_code, account_number, owners):
        super().__init__(sort_code, account_number)
        self.account_owners = []
        for owner in owners:
            self.account_owners.append(f'{owner.first_name} {owner.last_name}')

    def get_account_data(self):
        return f"{', '.join(self.account_owners)}, {super().get_account_data()}"
