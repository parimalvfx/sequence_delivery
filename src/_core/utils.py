"""Utility functions to be used by other modules of this project."""
import hashlib

def generate_file_hash(source):
    """Function to generate md5 hash for the given file source.

    :param source: Source file for which hash needs to be generated.
    :type source: str
    :return: Returns md5 hash for the given file source.
    :rtype: str
    """
    block_size = 131072  # 64 MB
    md5 = hashlib.md5()
    with open(source, "rb") as source_handler:
        buffer = source_handler.read(block_size)
        while len(buffer) > 0:
            md5.update(buffer)
            buffer = source_handler.read(block_size)

    return md5.hexdigest()
