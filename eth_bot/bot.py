"""
Base class that account credentials and
inherits available methods from a Contract ABI
"""
from populus import web3, ABIContract

class Bot(object):

    def __init__(self, abi_contracts: dict, account=None):
        [self.setup_methods(name, contract) for name, contract in abi_contracts.items()]
        self.web3 = web3
        self.setup_account(**account)

    def setup_account(self, address=None, key=None):
        if address:
            assert account in web3.accounts, "Address not in accounts!"
            self.address = address
            assert key, "If address is provided, key must be too!"
            self.key = key
        else:
            self.web3.personal

    def setup_methods(self, name, abi_contract: ABIContract):
        """
        Defines a contract's set of callable methods
        e.g. `dir(self.Token) => {'transfer': ..., 'allowance': ...}`
        """
        pass

    # User should extend this class with callable methods e.g.
    #def contract_MyMethod(self, arg1=..., arg2=..., ...):
    #    return self.Contract.myMethod(arg1, arg2, ...)
