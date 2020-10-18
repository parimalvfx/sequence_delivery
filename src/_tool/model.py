"""This module contains the model class for sequence delivery controller.
"""


class SequenceDeliveryModel:
    """This model class is the single common interface between sequence
    delivery view and controller.
    """
    def __init__(self):
        """Constructor method.
        """
        self._source_directories = []
        self._destinaion_directory = ""

    @property
    def source_directories(self):
        """Get source directories.

        :return: Source directories.
        :rtype: list
        """
        return self._source_directories

    @source_directories.setter
    def source_directories(self, directories):
        """Set source directories.

        :param directories: Source directories to set.
        :type directories: list
        """
        if not isinstance(directories, list):
            raise ValueError

        self._source_directories = directories

    @property
    def destination_directory(self):
        """Get destination directory.

        :return: Destination directory.
        :rtype: str
        """
        return self._destinaion_directory

    @destination_directory.setter
    def destination_directory(self, directory):
        """Set destination directory.

        :param directory: Destination directory to set.
        :type directory: str
        """
        if not isinstance(directory, str):
            raise ValueError

        self._destinaion_directory = directory
