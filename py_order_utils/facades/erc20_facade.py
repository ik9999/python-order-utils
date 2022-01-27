from py_order_utils.utils import normalize_address
from py_order_utils.facades.base_facade import BaseFacade


class Erc20Facade(BaseFacade):
    
    ABIS = {"erc20": "abi/ERC20ABI.json"}
    transferFrom = "transferFrom"
    balanceOf = "balanceOf"

    def __init__(self):
        super().__init__(self.ABIS)

    def transfer_from(self, from_address, to_address, value : str):
        """
        Creates transaction data for an ERC20 transferFrom
        """
        return self._get_contract("erc20").encodeABI(fn_name=self.transferFrom, 
        args=[
            normalize_address(from_address), 
            normalize_address(to_address), 
            value
            ]
        )

    def balance_of(self, address):
        """
        Creates transaction data for an ERC20 balanceOf
        """
        return self._get_contract("erc20").encodeABI(fn_name=self.balanceOf, args=[normalize_address(address)])