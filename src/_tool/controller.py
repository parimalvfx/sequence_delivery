"""This module contains the controller class for sequence delivery view.
"""
from datetime import datetime
import os
import shutil

import fileseq

from _core import exceptions as custom_exceptions
from _core import image_file


class SequenceDeliveryController:
    """This controller class provides the business logic to sequence delivery
    view.

    :param model: Sequence delivery model.
    :type model: SequenceDeliveryModel
    """
    def __init__(self, model) -> None:
        """Constructor method.
        """
        self._model = model
        self._date = datetime.now().strftime("%Y%m%d%H%M")  # `YYYYMMDDHHMM` format

    def _find_sequences_on_disk(self):
        """Get image sequences from source directories.

        :return: Returns all image sequences from source directories.
        :rtype: list(:class:`fileseq.FileSequence`)
        """
        sequences = []
        for directory in self._model.source_directories:
            sequences += fileseq.findSequencesOnDisk(
                directory,
                strictPadding=True,
                pad_style=fileseq.PAD_STYLE_HASH4)

        return sequences

    def _generate_delivery_path(self, ifo):
        """Generate delivery path from source path.

        :param ifo: Source :class:`_core.image_file.ImageFile` object.
        :type ifo: :class:`_core.image_file.ImageFile`
        :return: Delivery directory and file path for current time.
        :rtype: tuple
        """
        project_shot_name = "{0}_{1}".format(ifo.project_name, ifo.shot_name)

        directory = os.path.join(
            self._model.destinaion_directory, ifo.project_name, self._date,
            project_shot_name, ifo.task_name, ifo.file_type.upper())

        file_path = os.path.join(directory, ifo.basename)

        return directory, file_path

    def move_sequences(self):
        """Method to move all image sequences from source directories to
        destination directory.

        :raises _core.exceptions.DataIntegrityError: If the data of moved image
            file does not match with the original image.
        :return: Returns True if all image sequences are moved without any error.
        :rtype: bool
        """
        all_sequences = self._find_sequences_on_disk()

        for sequence in all_sequences:
            for image in sequence:
                ifo_source = image_file.ImageFile(image)
                delivery_dir, delivery_path = self._generate_delivery_path(
                    ifo_source)

                if not os.path.isdir(delivery_dir):
                    os.makedirs(delivery_dir)

                shutil.move(image, delivery_path)
                ifo_destination = image_file.ImageFile(delivery_path)

                if ifo_source != ifo_destination:
                    raise custom_exceptions.DataIntegrityError(
                        "Moved image does not match with source image: " \
                        "{0} (source) != {1} (destination)".format(
                            image, delivery_path))

        return True
