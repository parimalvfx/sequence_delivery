"""This module contains the model class for sequence delivery controller.
"""


class SequenceDeliveryModel:
    """This model class is the single common interface between sequence
    delivery view and controller.
    """
    def __init__(self):
        """Constructor method.
        """
        self.source_directories = []
        self.destinaion_directory = ""
