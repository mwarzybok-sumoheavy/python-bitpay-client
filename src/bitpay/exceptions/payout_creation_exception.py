"""
Payout Creation Exception gets raised when request for payout creation gets failed.
"""
from .payout_exception import PayoutException


class PayoutCreationException(PayoutException):
    """
    PayoutCreationException
    """

    __bitpay_message = "Failed to create payout"
    __bitpay_code = "BITPAY-PAYOUT-CREATE"
    __api_code = ""

    def __init__(self, message: str, code: int = 122, api_code: str = "000000"):
        """
        Construct the PayoutCreationException.

        :param message: The Exception message to throw.
        :param code: [optional] The Exception code to throw.
        :param api_code: [optional] The API Exception code to throw.
        """
        message = self.__bitpay_code + ": " + self.__bitpay_message + ":" + message
        self.__api_code = api_code
        super().__init__(message, code)
