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
