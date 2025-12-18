
import asyncio

from infrastructure.exceptions import FailedToLoadTeachers, BadSchoolData
from services.teacher_service import TeacherService
from presentation.inputs import SchoolInput


async def main():
    try:
        school_number, district = SchoolInput().get_input()
        service = TeacherService(school_number, district)
        
        await service.fetch_and_process()
        teachers = await service.get_teachers_by_position('Учитель')
        print(f'\nНайдено учителей: {len(teachers)}')
    except FailedToLoadTeachers as e:
        print(f'Ошибка загрузки данных: {e}')
    except BadSchoolData as e:
        print(f'Ошибка корректности данных о школе: {e}')
    except Exception as e:
        print(f'Неизвестная ошибка: {e}')


if __name__ == '__main__':
    asyncio.run(main())
