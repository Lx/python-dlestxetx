"""
``dlestxetx``: DLE/STX/ETX packet encoder/decoder
=================================================

**DLE/STX/ETX** is a `packet framing algorithm`_,
used by some devices (such as Metlink LED passenger information displays)
to transmit *data* as *packets* over a serial medium.
This algorithm delimits data using ``DLE``, ``STX``, and ``ETX`` `control codes`_.

Packets begin with a ``DLE STX`` sequence,
follow with a byte-stuffed_ data stream
(all ``DLE`` bytes in the data are conveyed as ``DLE DLE``),
and end with a ``DLE ETX`` sequence.

This module provides functions to encode data into packets,
decode packets into data,
and read packets directly from `file objects`_.

.. _packet framing algorithm:
   https://en.wikipedia.org/wiki/Consistent_Overhead_Byte_Stuffing#Packet_framing_and_stuffing
.. _control codes:
   https://en.wikipedia.org/wiki/C0_and_C1_control_codes#C0_controls
.. _byte-stuffed:
   https://en.wikipedia.org/wiki/Byte_stuffing
.. _file objects:
   https://docs.python.org/3/glossary.html#term-file-object
"""

__version__ = '1.0.0'
__all__ = ['encode', 'decode', 'read', '__version__']

from io import RawIOBase, BytesIO
from typing import Union

STX = b'\x02'
ETX = b'\x03'
DLE = b'\x10'

PACKET_HEADER = DLE + STX
PACKET_FOOTER = DLE + ETX
ESCAPED_DLE = DLE * 2


def encode(data: bytes) -> bytes:
    """
    Wrap data into a DLE/STX/ETX packet.

    :param data:
        the data to encode.

    :return:
        the packet containing the supplied data.
    """
    return PACKET_HEADER + data.replace(DLE, ESCAPED_DLE) + PACKET_FOOTER


def decode(packet: bytes) -> bytes:
    """
    Unwrap data from a DLE/STX/ETX packet.

    :param packet:
        the packet to decode.

    :return:
        the data within the supplied packet.

    :raises ValueError:
        if the input doesn't represent a valid packet,
        or if extraneous bytes follow that packet.
    """
    stream = BytesIO(packet)
    decoded = read(stream)
    extra_bytes = stream.getvalue()[stream.tell():]
    if extra_bytes:
        raise ValueError(f'extraneous bytes from index {stream.tell()}: {extra_bytes!r}')
    return decoded


def read(file: Union[RawIOBase, BytesIO]) -> bytes:
    """
    Read precisely one DLE/STX/ETX packet from a `file object`_.

    :param file:
        a file object with a ``read(num_bytes)`` method.

    :return:
        the data within the received packet.

    :raises ValueError:
        if the data from the supplied file object doesn't start with a packet,
        or doesn't follow with a complete, valid packet.

    .. _file object:
       https://docs.python.org/3/glossary.html#term-file-object
    """
    header = file.read(len(PACKET_HEADER))
    if header != PACKET_HEADER:
        raise ValueError(f'found header {header!r} where {PACKET_HEADER!r} was expected')

    decoded = bytearray()
    buffer = bytearray()
    while True:
        buffer += file.read(2 - len(buffer))
        if len(buffer) != 2:
            raise ValueError(f'unexpected end of packet')
        if buffer.startswith(DLE):
            if buffer == ESCAPED_DLE:
                decoded += DLE
                buffer.clear()
            elif buffer == PACKET_FOOTER:
                break
            else:
                raise ValueError(f'found {bytes([buffer[1]])!r} where {ETX!r} or {DLE!r} was expected')
        else:
            decoded += bytes([buffer.pop(0)])

    return bytes(decoded)
