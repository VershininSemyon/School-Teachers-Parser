
from domain.structures import District
from infrastructure.exceptions import BadSchoolData


class SchoolInput:
    def __init__(self):
        self.school_number = None
        self.district = None
    
    def display_district_menu(self) -> None:
        print('\n' + '=' * 40)
        print('ВЫБЕРИТЕ ОКРУГ ШКОЛЫ')
        print('=' * 40)
        
        for district in District:
            print(f'{district.short_name} - {district.full_name}')

        print('=' * 40)
    
    def get_school_number(self) -> int:
        while True:
            try:
                number = int(input('Введите номер школы (например, 2086): '))
                if number <= 0:
                    print('Номер школы должен быть положительным числом!')
                    continue
                return number
            except ValueError:
                print('Пожалуйста, введите корректный номер!')
    
    def get_district(self) -> District:
        districts = {district.short_name: district for district in District}
        
        while True:
            choice = input('Выберите округ (введите букву): ').lower().strip()
            if choice in districts:
                return districts[choice]
            print('Неверный выбор! Пожалуйста, выберите букву из списка.')
    
    def get_input(self) -> tuple[int, District]:
        print('\n' + '=' * 50)
        print('НАСТРОЙКА ПАРСЕРА УЧИТЕЛЕЙ')
        print('=' * 50)
        
        self.school_number = self.get_school_number()
        
        self.display_district_menu()
        self.district = self.get_district()
        
        return self.school_number, self.district
    
    def get_data(self) -> tuple[int, District]:
        if self.school_number is None or self.district is None:
            raise BadSchoolData('Данные не были введены!')
        return self.school_number, self.district
