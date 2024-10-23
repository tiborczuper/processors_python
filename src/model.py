from __future__ import annotations
from enum import Enum
from dataclasses import dataclass,field
@dataclass
class cpu:
    id: int = field(hash=True)
    speed: float = field(compare=False)
    core: int = field(compare=False)
    company: manufacturer = field(compare=False,default_factory= lambda: cpu.manufacturer.apple)
    connected_phones: list[smartphone] = field(compare=False,repr=False,default_factory= lambda : [])
    class manufacturer(Enum):
        snapdragon = "Snapdragon"
        intel = "Intel"
        apple = "Apple"
        qualcomm = "Qualcomm"

    @dataclass
    class smartphone:
        number: int = field(hash=True)
        year:int = field(compare=False)
        model:str = field(compare=False)