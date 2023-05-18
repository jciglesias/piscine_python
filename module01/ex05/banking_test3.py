from the_bank import Account, Bank

if __name__ == "__main__":
    bank = Bank()
    accounts = []
    accounts.append(Account('Sherlock Holmes', zip='NW1 6XE', addr='221B Baker street', value=1000.0))
    accounts.append(Account('James Watson',
                          zip='NW1 6XE',
                          addr='221B Baker street',
                          value=25000.0,
                          info=None))

    accounts.append(Account("Douglass",
                            zip='42',
                            addr='boulevard bessieres',
                            value=42))
    accounts.append(Account("Adam",
                            value=42,
                            zip='0',
                            addr='Somewhere'))
    accounts.append(Account("Bender Bending Rodríguez",
                            zip='1',
                            addr='Mexico',
                            value=42))
    accounts.append(Account("Charlotte",
                            zip='2',
                            addr='Somewhere in the Milky Way',
                            value=42))
    accounts.append(Account("Edouard",
                            zip='3',
                            addr='France',
                            value=42))
    
    for i in accounts: bank.add(i)

    for i in accounts:
        if bank.transfer('James Watson', i.name, 1000.0) is False:
            print(f'Failed James to {i.name}')
            bank.fix_account('James Watson')
            bank.fix_account(i.name)
            if bank.transfer('James Watson', i.name, 1000.0) is False:
                print(f'Failed James to {i.name} again')
            else:
                print(f'Success James to {i.name} in second attempt')
        else:
            print(f"success James to {i.name}")
