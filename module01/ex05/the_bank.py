class Account(object):
    ID_COUNT = 1
    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)
        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, 'value'):
            self.value = 0
        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")
    def transfer(self, amount):
        self.value += amount

class Bank(object):
    """The bank"""
    def __init__(self):
        self.accounts = []
    def add(self, new_account: Account):
        """ Add new_account in the Bank
        @new_account: Account() new account to append
        @return True if success, False if an error occured
        """
        if not isinstance(new_account, Account):
            print("not a valid account")
            return
        if new_account in self.accounts:
            print("account already in bank")
            return
        self.accounts.append(new_account)
    def transfer(self, origin, dest, amount):
        """" Perform the fund transfer
        @origin: str(name) of the first account
        @dest: str(name) of the destination account
        @amount: float(amount) amount to transfer
        @return True if success, False if an error occured
        """
        origin_acc: Account = None
        dest_acc: Account = None
        for i in self.accounts:
            if i.name == origin:
                origin_acc = i
            elif i.name == dest:
                dest_acc: Account = i
        if origin == dest:
            if isvalidacc(origin_acc):
                return True
            else:
                return False
        if isvalidacc(origin_acc) and isvalidacc(dest_acc) and amount > 0 and origin_acc.value >= amount:
            if origin_acc is not dest_acc:
                dest_acc.transfer(amount)
                origin_acc.value -= amount
            return True
        return False
    def fix_account(self, name):
        """ fix account associated to name if corrupted
        @name: str(name) of the account
        @return True if success, False if an error occured
        """
        if not isinstance(name, str):
            return False
        account: Account = None
        for i in self.accounts:
            if i.name == name:
                account = i
        if not account:
            return False
        attr = account.__dict__
        while not isvalidacc(account):
            if not len(attr) % 2:
                ind = None
                for i in attr:
                    if i != "name" and i != "value" and i != "id" and i.find("zip") and i.find("addr"):
                        ind = i
                attr.pop(ind)
            z, addr = 0, 0
            if not attr.get("name") or not isinstance(attr["name"], str):
                attr["name"] = name
            if not attr.get("id") or not isinstance(attr["id"], int):
                attr["id"] = Account.ID_COUNT
                Account.ID_COUNT += 1
            if not attr.get("value") or not isinstance(attr["value"], (int, float)):
                attr["value"] = 0.0
            for i in attr:
                if i[0] == 'b':
                    i.lstrip("b")
                elif i.find("zip") == 0:
                    z += 1
                elif i.find("addr") == 0:
                    addr += 1
            if z == 0 and addr == 0:
                attr["zip"] = input("Enter zip addres:\n")
        return True

def isvalidacc(account = None):
    if not isinstance(account, Account):
        # print("instance is not account")
        return False
    attr = account.__dict__
    if not len(attr) % 2:
        # print("even number of attributes")
        return False
    z, addr = 0, 0
    if  not attr.get("id"):
        # print("missing id")
        return False
    if not isinstance(attr.get("value"), (int, float)):
        # print("missing value")
        return False
    if not attr.get("name"):
        # print("missing name")
        return False
    for i in attr:
        if i[0] == 'b':
            # print(i, attr[i])
            return False
        elif i.find("zip") == 0:
            z += 1
        elif i.find("addr") == 0:
            addr += 1
        elif i == "name" and not isinstance(attr[i], str):
            # print(i, attr[i])
            return False
        elif i == "id" and not isinstance(attr[i], int):
            # print(i, attr[i])
            return False
        elif i == "value" and not isinstance(attr[i], (int, float)):
            # print(i, attr[i])
            return False
    if z == 0 and addr == 0:
        # print("no zip or addr")
        return False
    return True