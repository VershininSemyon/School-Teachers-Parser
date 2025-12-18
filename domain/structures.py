
from dataclasses import dataclass
from enum import Enum
from typing import Optional


class District(Enum):
    CENTRAL = ('c', 'Центральный')
    NORTH = ('s', 'Северный')
    NORTH_EAST = ('sv', 'Северо-Восточный')
    EAST = ('v', 'Восточный')
    SOUTH_EAST = ('uv', 'Юго-Восточный')
    SOUTH = ('u', 'Южный')
    SOUTH_WEST = ('uz', 'Юго-Западный')
    WEST = ('z', 'Западный')
    NORTH_WEST = ('sz', 'Северо-Западный')
    
    @property
    def short_name(self) -> str:
        return self.value[0]
    
    @property
    def full_name(self) -> str:
        return self.value[1]


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
