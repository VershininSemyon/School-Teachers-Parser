
import aiofiles

from domain.structures import Department, StaffMember


class ReportGenerator:
    @staticmethod
    def generate_summary(departments: list[Department]) -> str:
        total_departments = len(departments)
        total_staff = sum(len(dept.staff) for dept in departments)
        
        teachers = sum(
            1 for dept in departments 
            for member in dept.staff 
            if any(pos.type == 'teacher' for pos in member.positions)
        )
        
        employees = total_staff - teachers
        
        report = [
            '=' * 50,
            'СВОДНЫЙ ОТЧЕТ О СОТРУДНИКАХ',
            '=' * 50,
            f'Всего отделов: {total_departments}',
            f'Всего сотрудников: {total_staff}',
            f'  - Преподавателей: {teachers}',
            f'  - Сотрудников: {employees}',
            '=' * 50
        ]
        
        for dept in sorted(departments, key=lambda x: x.position):
            report.append(f'\n{dept.title} (позиция: {dept.position}):')
            for member in dept.staff:
                positions = ', '.join(f'{pos.name} ({pos.type})' for pos in member.positions)
                report.append(f'  - {member.full_name}: {positions}')
        
        return '\n'.join(report)
    
    @staticmethod
    async def write_summary_into_file(file_path: str, summary: str) -> None:
        async with aiofiles.open(file_path, mode='w', encoding='utf-8') as file:
            await file.write(summary)
    
    @staticmethod
    def find_by_position(departments: list[Department], position_name: str) -> list[StaffMember]:
        result = []
        for dept in departments:
            for member in dept.staff:
                if any(pos.name == position_name for pos in member.positions):
                    result.append(member)
        return result
