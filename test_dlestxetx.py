from io import BytesIO

from pytest import raises

from dlestxetx import encode, decode, read


def test_encode():
    assert encode(b'') == b'\x10\x02\x10\x03'
    assert encode(b'\x01\x10\x05') == b'\x10\x02\x01\x10\x10\x05\x10\x03'


def test_decode():
    assert decode(b'\x10\x02\x10\x03') == b''
    assert decode(b'\x10\x02\x10\x10\x10\x03') == b'\x10'
    with raises(ValueError):
        decode(b'\x10\x02\x10\x03<extraneous data>')
    with raises(ValueError):
        decode(b'<incorrect header>')
    with raises(ValueError):
        decode(b'\x10\x02<incomplete packet>')
    with raises(ValueError):
        decode(b'\x10\x02<unescaped DLE>\x10\x00\x10\x03')


def test_read():
    assert read(BytesIO(b'\x10\x02\x10\x10\x10\x03<extraneous data>')) == b'\x10'
    packets = BytesIO(encode(b'\x04\x05\x06') + encode(b'\x07\x08\x09'))
    assert read(packets) == b'\x04\x05\x06'
    assert read(packets) == b'\x07\x08\x09'
    with raises(ValueError):
        read(packets)
