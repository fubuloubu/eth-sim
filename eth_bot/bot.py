"""
Base class that account credentials and
inherits available methods from a Contract ABI
"""
from populus import Project
from populus.utils.wait import wait_for_transaction_receipt

class Bot(object):

    def __init__(self, abi_contracts: dict, account=None):
        [self.setup_methods(name, contract) for name, contract in abi_contracts.items()]
        self.web3 = chain.web3
        self.setup_account(**account)

    def setup_account(self, address=None, password=None):
        if address:
            assert account in web3.accounts, "Address not in accounts!"
            self.address = address
            assert password, "If address is provided, key must be too!"
            self.password = password
        else:
            self.web3.personal

    def setup_methods(self, name, abi_contract: ABIContract):
        """
        Defines a contract's set of callable methods
        e.g. `dir(self.Token) => {'transfer': ..., 'allowance': ...}`
        """
        setattr(self, name, abi_contract)

    # User should extend this class with callable methods e.g.
    #def contract_MyMethod(self, arg1=..., arg2=..., ...):
    #    return self.Contract.myMethod(arg1, arg2, ...)
