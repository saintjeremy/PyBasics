#!/usr/bin/python3

# Exercise the Accounts class.

# Get the acct module, which contains the Accounts class.
from acct import Accounts

# Print all the existing accounts and values.
def praccts(ao):
    "Print all accounts."
    for n in sorted(ao.list()):
        print('%-15s %4d' % (n + ':', ao.value(n)))

# Create the account set with 4000 in hunter, then create several other
# accounts starting with 400 taken from hunter.
act = Accounts('hunter', 4000)
for n in ['abong', 'bill', 'ernie', 'frye']:
    act.newacct(n)
    act.transfer('hunter', n, 400)
print('**** Initially ****')
praccts(act)
print()

# Some random operations.
act.transfer('bill', 'abong', 45)
act.transfer('ernie', 'frye', 155)
act.transfer('ernie', 'bill', 221)
act.close('ernie', 'hunter')

print('**** Finally ****')
praccts(act)
print()
