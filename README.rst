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

The ``dlestxetx`` module provides functions
to encode data into packets::

    >>> from dlestxetx import encode
    >>> encode(b'\x01\x10\x05')
    b'\x10\x02\x01\x10\x10\x05\x10\x03'

decode packets into data::

    >>> from dlestxetx import decode
    >>> decode(b'\x10\x02\x01\x10\x10\x05\x10\x03')
    b'\x01\x10\x05'

and read packets directly from `file objects`_::

    >>> from dlestxetx import read
    >>> packets = BytesIO(encode(b'\x04\x05\x06') + encode(b'\x07\x08\x09'))
    >>> read(packets)
    b'\x04\x05\x06'
    >>> read(packets)
    b'\x07\x08\x09'

.. _packet framing algorithm:
   https://en.wikipedia.org/wiki/Consistent_Overhead_Byte_Stuffing#Packet_framing_and_stuffing
.. _control codes:
   https://en.wikipedia.org/wiki/C0_and_C1_control_codes#C0_controls
.. _byte-stuffed:
   https://en.wikipedia.org/wiki/Byte_stuffing
.. _file objects:
   https://docs.python.org/3/glossary.html#term-file-object


Installation
------------

Install this module from PyPI_ using pip_::

    pip install dlestxetx

.. _PyPI: https://pypi.org/project/dlestxtex
.. _pip: https://pip.pypa.io/


Contribute
----------

- Source code:
  https://github.com/Lx/python-dlestxetx


Support
-------

- Issue tracker:
  https://github.com/Lx/python-dlestxetx/issues


License
-------

This project is licensed under the `MIT License`_.

.. _MIT License: https://opensource.org/licenses/MIT
