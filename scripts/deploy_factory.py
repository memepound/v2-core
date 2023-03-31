from brownie import accounts, UniswapV2Factory


def main():
    # todo: load deployer address
    deployer = accounts.load()

    factory = UniswapV2Factory.deploy(deployer, {"from": deployer})
    print(f"{factory = }")
