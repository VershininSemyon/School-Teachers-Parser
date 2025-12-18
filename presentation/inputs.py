
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
        
        russian_names = {
            'c': 'Центральный',
            's': 'Северный', 
            'sw': 'Северо-Восточный',
            'w': 'Восточный',
            'yw': 'Юго-Восточный',
            'u': 'Южный',
            'uz': 'Юго-Западный',
            'z': 'Западный',
            'sz': 'Северо-Западный'
        }
        
        for key, name in russian_names.items():
            print(f'{key} - {name}')
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
        districts = {
            'c': District.CENTRAL,
            's': District.NORTH,
            'sw': District.NORTH_EAST,
            'w': District.EAST,
            'yw': District.SOUTH_EAST,
            'u': District.SOUTH,
            'uz': District.SOUTH_WEST,
            'z': District.WEST,
            'sz': District.NORTH_WEST
        }
        
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
