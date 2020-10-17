"""This module contains the :class:`ImageFile` class to represent a single
image of image sequence.
"""
import os
import re

from _core import exceptions as custom_exceptions
from _core import utils


class ImageFile:
    """This class is represent a single image file of a image sequence.

    :param source: Image file to represent.
    :type source: str
    """
    def __init__(self, source) -> None:
        """Constructor method.

        :raises ValueError: If given source file does not exist on disk.
        """
        self._source = source
        if not os.path.isfile(self._source):
            raise ValueError

        self._project_name, self._shot_name, self._task_name, self._frame, \
            self._file_type = self._parse_basename()

        self._hash = self._generate_hash()

    def __repr__(self) -> str:
        """Method to represent instance of this class.

        :return: Representation of object.
        :rtype: dict
        """
        dict_repr = {
            "project_name": self.project_name,
            "shot_name": self.shot_name,
            "task_name": self.task_name,
            "frame": self.frame,
            "file_type": self.file_type,
            "hash": self._hash
        }

        return str(dict_repr)

    def __eq__(self, other):
        """Equality method.

        :return: True if this object is equal with other object,
            False otherwise.
        :rtype: bool
        """
        return self.hash == other.hash

    def __ne__(self, other):
        """Inequality method.

        :return: True if this object is not equal with other object,
            False otherwise.
        :rtype: bool
        """
        return self.hash != other.hash

    def _parse_basename(self):
        """Method to parse basename as per naming convention.

        :return: Tuple of separated name units.
        :rtype: tuple
        """
        basename = os.path.basename(self._source)
        units = re.split("[_.]", basename)

        if len(units) != 5:
            raise custom_exceptions.SequenceDeliveryBaseException(
                "Image name {0} does not meet the convention length of " \
                    "5".format(basename)
            )

        return tuple(units)

    def _generate_hash(self):
        """Method to generate md5 hash of this image file.

        :return: md5 hash.
        :rtype: str
        """
        return utils.generate_file_hash(self._source)

    @property
    def basename(self):
        """Basename of this image.

        :return: Image basename.
        :rtype: str
        """
        return os.path.basename(self._source)

    @property
    def project_name(self):
        """Project with which this image is associated.

        :return: Project name.
        :rtype: str
        """
        return self._project_name

    @property
    def shot_name(self):
        """Shot with which this image is associated.

        :return: Shot name.
        :rtype: str
        """
        return self._shot_name

    @property
    def task_name(self):
        """Task with which this image is associated.

        :return: Task name.
        :rtype: str
        """
        return self._task_name

    @property
    def frame(self):
        """Frame number of this image in a sequence.

        :return: Frame number.
        :rtype: str
        """
        return self._frame

    @property
    def file_type(self):
        """File type (extension) of this image.

        :return: File type.
        :rtype: str
        """
        return self._file_type

    @property
    def hash(self):
        """md5 hash of this image.

        :return: md5 hash.
        :rtype: str
        """
        return self._hash
