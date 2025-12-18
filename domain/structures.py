
from dataclasses import dataclass
from enum import Enum
from typing import Optional


class District(Enum):
    CENTRAL = 'c'
    NORTH = 's'
    NORTH_EAST = 'sw'
    EAST = 'w'
    SOUTH_EAST = 'yw'
    SOUTH = 'u'
    SOUTH_WEST = 'uz'
    WEST = 'z'
    NORTH_WEST = 'sz'


@dataclass
class Position:
    id: Optional[int]
    name: str
    visibility_role: Optional[int]
    type: str


@dataclass
class PinInfo:
    group_id: int
    pin: Optional[str]


@dataclass
class StaffMember:
    hash_id: str
    full_name: str
    photo_url: Optional[str]
    is_visible: bool
    group_ids: list[int]
    pins: list[PinInfo]
    positions: list[Position]


@dataclass
class Department:
    id: int
    title: str
    position: int
    staff: list[StaffMember]
