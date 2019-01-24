import io

from pycoin.encoding.hash import double_sha256
from pycoin.satoshi.satoshi_struct import parse_struct, stream_struct
from pycoin.block import Block as BaseBlock
from .Tx import Tx

class Block(BaseBlock):
    Tx = Tx
