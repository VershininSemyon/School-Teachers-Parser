
from typing import Any

from domain.structures import Department, PinInfo, Position, StaffMember


class DataParser:
    @staticmethod
    def parse_position(position_data: dict[str, Any], position_type: str) -> Position:
        return Position(
            id=position_data.get('id'),
            name=position_data.get('position_name', ''),
            visibility_role=position_data.get('visibility_role'),
            type=position_type
        )
    
    @staticmethod
    def parse_pin(pin_data: dict[str, Any]) -> PinInfo:
        return PinInfo(
            group_id=pin_data.get('group_id'),
            pin=pin_data.get('pin')
        )
    
    @staticmethod
    def parse_staff_member(member_data: dict[str, Any]) -> StaffMember:
        positions = []
        
        for position_type, position_list in member_data.get('position_names', {}).items():
            if position_list:
                for pos_data in position_list:
                    positions.append(DataParser.parse_position(pos_data, position_type))
        
        pins = [DataParser.parse_pin(pin) for pin in member_data.get('pins_group_id', [])]
        
        return StaffMember(
            hash_id=member_data.get('hash_id', ''),
            full_name=member_data.get('fio', ''),
            photo_url=member_data.get('photo'),
            is_visible=member_data.get('visibility', False),
            group_ids=member_data.get('groups', []),
            pins=pins,
            positions=positions
        )
    
    @staticmethod
    def parse_department(dept_data: dict[str, Any]) -> Department:
        staff_members = [
            DataParser.parse_staff_member(member) 
            for member in dept_data.get('items', [])
        ]
        
        return Department(
            id=dept_data.get('id'),
            title=dept_data.get('title', ''),
            position=dept_data.get('position', 0),
            staff=staff_members
        )
    
    @staticmethod
    def parse_all(raw_data: list[dict[str, Any]]) -> list[Department]:
        return [DataParser.parse_department(dept) for dept in raw_data]
