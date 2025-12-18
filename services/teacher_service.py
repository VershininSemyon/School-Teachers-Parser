
from domain.structures import Department, District, StaffMember
from infrastructure.database import DatabaseManager
from infrastructure.dto import DataParser
from services.api_client import TeacherFetcher
from presentation.reports import ReportGenerator


class TeacherService:
    def __init__(self, school_number: int, district: District):
        self.school_number = school_number
        self.fetcher = TeacherFetcher(school_number, district)
        self.parser = DataParser()
        self.db_manager = DatabaseManager(db_path=f'school_{school_number}.db')
        self.report_generator = ReportGenerator()
    
    async def fetch_and_process(self, create_report: bool = True) -> list[Department]:
        try:
            raw_data = await self.fetcher.fetch()
            departments = self.parser.parse_all(raw_data)
            
            await self.db_manager.init_db()
            await self.db_manager.save_departments(departments)
            
            if create_report:
                report = self.report_generator.generate_summary(departments)
                print(report)

                await self.report_generator.write_summary_into_file(
                    f"school_{self.school_number}.txt",
                    report
                )
            
            return departments
        except Exception as e:
            print(f'Ошибка при обработке данных: {e}')
            raise
    
    async def get_teachers_by_position(self, position_name: str) -> list[StaffMember]:
        departments = await self.fetch_and_process(create_report=False)
        return self.report_generator.find_by_position(departments, position_name)
