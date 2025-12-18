
import asyncio

from domain.structures import District
from infrastructure.database import DatabaseManager
from infrastructure.dto import DataParser
from services.teacher_service import TeacherFetcher


async def school_task(school_number: int, district: District) -> None:
    try:
        fetcher = TeacherFetcher(school_number, district)
        parser = DataParser()
        db_manager = DatabaseManager(db_path=f'school_{school_number}.db')

        raw_data = await fetcher.fetch()
        departments = parser.parse_all(raw_data)
        
        await db_manager.init_db()
        await db_manager.save_departments(departments)
        
        print(f"School № {school_number}[{district}] - OK")
    except Exception as e:
        print(f"School № {school_number}[{district}] - ERROR {e}")


async def process_schools():
    tasks = []
    
    for school_number in range(1, 3001):
        for district in District:
            task = school_task(school_number, district)
            tasks.append(task)
    
    await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == "__main__":
    asyncio.run(process_schools())
