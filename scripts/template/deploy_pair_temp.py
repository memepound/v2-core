from brownie import accounts, UniswapV2Factory
from scripts.constants import *


def main():
    # todo: load deployer address
    deployer = accounts.load()

    factory = UniswapV2Factory.at(FACTORY)

    tokenA = "IMPORT FROM CONSTANTS"
    tokenB = "IMPORT FROM CONSTANTS"

    factory.createPair(tokenA, tokenB, {"from": deployer})

    print("pair:", factory.getPair(tokenA, tokenB))
