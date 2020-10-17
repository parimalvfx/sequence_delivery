"""Custom exceptions to use in this project.
"""

class SequenceDeliveryBaseException(Exception):
    """Base class for exceptions in this module.
    """


class InvalidImageNameError(SequenceDeliveryBaseException):
    """Exception raise to raise when image file name does not meet
    convention.

    :param message: Message to show when exception is raised.
    :type message: str
    """
    def __init__(self, message) -> None:
        self.message = message


class DataIntegrityError(SequenceDeliveryBaseException):
    """Exception to raise when the data of two sources does not match.

    :param message: Message to show when exception is raised.
    :rtype message: str
    """
    def __init__(self, message) -> None:
        self.message = message
