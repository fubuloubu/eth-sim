from eth_bot.bot import Bot
from eth_bot.botnet import botnet_app

solidity_contract="""
contract Sol {
    function foo() public returns uint256 {
        return 1;
    }
}
"""

viper_contract="""
def bar() -> num:
    return 1
"""

# Run Interactive Bot Net app
botnet_app(Bot)
