"""This module contains the :class:`ImageFile` class to represent a single
image of image sequence.
"""
import os


class ImageFile:
    """This class is represent a single image file of a image sequence.

    :param source: Image file to represent.
    :type source: str
    """
    def __init__(self, source) -> None:
        """Constructor method.

        :raises ValueError: If given source file does not exist on disk.
        """
        if not os.path.isfile(source):
            raise ValueError
