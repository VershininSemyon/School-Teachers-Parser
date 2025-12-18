
import aiohttp
from infrastructure.exceptions import FailedToLoadTeachers
from domain.structures import District
from typing import Any


class TeacherFetcher:
    def __init__(self, school_number: int, school_district: District) -> None:
        self.school_number = school_number
        self.school_district = school_district.short_name
        self.url = f'https://sch{self.school_number}{self.school_district}.mskobr.ru/v1/api/staff/groups'
        self.params = {'code_role': 'teacher'}

    async def fetch(self) -> list[dict[str, Any]]:
        async with aiohttp.ClientSession() as session:
            response = await session.get(
                url=self.url,
                params=self.params
            )

            if response.status != 200:
                raise FailedToLoadTeachers(f'Неверный статус код: {response.status}')

            return await response.json()
