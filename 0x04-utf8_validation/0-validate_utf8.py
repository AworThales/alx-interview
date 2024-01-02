#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """
    Method to determines if the given data set represents a valid
    UTF-8 encoding.
    """
    bytes_number = 0

    check_1 = 1 << 7
    check_2 = 1 << 6

    for i in data:

        mask_byte = 1 << 7

        if bytes_number == 0:

            while mask_byte & i:
                bytes_number += 1
                mask_byte = mask_byte >> 1

            if bytes_number == 0:
                continue

            if bytes_number == 1 or bytes_number > 4:
                return False

        else:
            if not (i & check_1 and not (i & check_2)):
                    return False

        bytes_number -= 1

    if bytes_number == 0:
        return True

    return False
