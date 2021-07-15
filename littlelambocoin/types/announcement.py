from dataclasses import dataclass

from littlelambocoin.types.blockchain_format.sized_bytes import bytes32
from littlelambocoin.util.hash import std_hash


@dataclass(frozen=True)
class Announcement:
    origin_info: bytes32
    message: bytes

    def name(self) -> bytes32:
        return std_hash(bytes(self.origin_info + self.message))
