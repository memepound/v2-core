from brownie import accounts, UniswapV2Factory
from scripts.constants import *


def main():
    # todo: load deployer address
    deployer = accounts.load("qom", "qom")

    factory = UniswapV2Factory.at(FACTORY)

    tokenB = W_QOM

    factory.createPair(Q, tokenB, {"from": deployer})
    factory.createPair(O, tokenB, {"from": deployer})
    factory.createPair(M, tokenB, {"from": deployer})
