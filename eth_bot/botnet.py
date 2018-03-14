"""
BotNet class that allows controlling groups of bots,
both synchronously and asynchronously
"""
import random
import threading

from .bot import Bot

MIN_INTERVAL=1000 # milli-seconds between calls

class BotNet(object):

    def __init__(self, bot_class: Bot, interval=MIN_INTERVAL):
        self.bot_class = bot_class
        self.bots = []
        self.abi_contracts = {}
        # Start Async Method thread
        self.async_start(interval=interval)

    def create_bot(self, account=None):
        self.bots.append(self.bot_class(self.abi_contracts, account=account))

    def rand_do(self, method_name, kwargs={}):
        return getattr(random.choice(self.bots), method_name)(**kwargs)

    def rand_subset_do(self, num_subset, method_name, kwargs={}):
        return [getattr(b, method_name)(**kwargs) for b in random.sample(self.bots, num_subset)]

    def all_do(self, method_name, kwargs={}):
        return [getattr(b, method_name)(**kwargs) for b in self.bots]

    def async_do(self):
        # Override to do something asynchronously
        # Allow in-app re-definitions of this function?
        pass

    def async_stop(self):
        self.async_ready = False # Aborts on next pass
    
    def async_start(self, interval=MIN_INTERVAL):
        assert interval > MIN_INTERVAL, \
                "Timing Interval ((:4.3f} secs) cannot be less than {:4.3f} secs".\
                format(interval, MIN_INTERVAL/1000)
        self.interval = interval
        self.async_ready = True
        threading.Thread(target=self.async_run).start()

    def async_run(self):
        # Only run while async_ready flag is true, abort otherwise
        while (self.async_ready):
            sleep(self.interval)
            self.async_do()

# Utils
import json
from os.path import exists as file_exists
DEFAULT_FILE='./accounts.json'
"""
This function lets someone create a set of accounts
"""
def add_accounts(number_bots=10, accounts_file=DEFAULT_FILE):
    # 8 char passwords of random uppercase, lowercase and digits
    from string import printable as ascii_chars
    from random import choice as rand_choice
    pw = lambda: ''.join(rand_choice(ascii_chars) for _ in range(8))
    # Create password-protected accounts
    passwords = [pw() for _ in range(number_bots)]
    get_address = lambda pw: 
    gen_accounts = lambda: [{"address": get_address(pw), "password": pw} for pw in passwords]
    accounts = 
    # Append to file if it exists, else set these to be the only accounts
    if file_exists(accounts_file):
        with open(accounts_file, 'r') as f:
            accounts = json.loads(f.read())
        accounts.extend(gen_accounts())
    else:
        if accounts_file == DEFAULT_FILE:
            print("Creating accounts file at '{}'".format(accounts_file))
            accounts = gen_accounts()
    # Write out file
    with open(accounts_file, 'w') as f:
        f.write(json.dumps(accounts))

"""
This function lets you instantiate a command line app for a given bot type
"""
def botnet_app(bot_class: Bot, abi_contracts: dict, \
        botnet_class=BotNet, accounts_file=DEFAULT_FILE):
    # Handle accounts file and load accounts
    if file_exists(accounts_file):
        with open(accounts_file, 'r') as f:
            accounts = json.loads(f.read())
    else:
        raise IOError("File '{}' doesn't exist!".format(accounts_file))
    # Start the botnet class
    botnet = botnet_class(bot_class)
    [botnet.create_bot(account) for account in accounts]
    return botnet
