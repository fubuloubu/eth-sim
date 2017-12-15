"""
BotNet class that allows controlling groups of bots,
both synchronously and asynchronously
"""
import random
import threading

from .bot import Bot

MIN_INTERVAL=1000

class BotNet(object):

    def __init__(self, bot_class: Bot, interval=1000):
        self.bot_class = bot_class
        self.bots = []
        # Start Async Method thread
        self.async_start(interval=interval)

    def create_bot(self, account=None):
        self.bots.append(self.bot_class(self.abi_contracts, account=account))

    def rand_do(self, method_name, kwargs={}):
        [getattr(b, method_name)(**kwargs) for b in random.choice(self.bots)]

    def rand_subset_do(self, num_subset, method_name, kwargs={}):
        [getattr(b, method_name)(**kwargs) for b in random.sample(self.bots, num_subset)]

    def all_do(self, method_name, kwargs={}):
        [getattr(b, method_name)(**kwargs) for b in self.bots]

    def async_do(self):
        # Override to do something asynchronously
        # Allow in-app re-definitions of this function?
        pass

    def async_stop(self):
        self.async_ready = False # Aborts on next pass
    
    def async_start(self, interval=1000):
        assert interval > MIN_INTERVAL, "Timing Interval cannot be less than {:4.3f} secs".format(MIN_INTERVAL/1000)
        self.interval = interval
        self.async_ready = True
        threading.Thread(target=self.async_run).start()

    def async_run(self):
        # Only run while async_ready flag is true, abort otherwise
        while (self.async_ready):
            sleep(self.interval)
            self.async_do()

"""
This function lets you instantiate a command line app for a given bot type
"""
def botnet_app(bot_class: Bot, botnet_class=BotNet, accounts_file='./accounts.json'):
    botnet = botnet_class(bot_class)
    for account in json.parse(accounts_file):
        botnet.create_bot(account)
