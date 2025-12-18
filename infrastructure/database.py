
import aiosqlite

from domain.structures import Department


class DatabaseManager:
    def __init__(self, db_path: str = 'school_data.db'):
        self.db_path = db_path
    
    async def init_db(self):
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute('''
                CREATE TABLE IF NOT EXISTS departments (
                    id INTEGER PRIMARY KEY,
                    title TEXT NOT NULL,
                    position INTEGER
                )
            ''')
            
            await db.execute('''
                CREATE TABLE IF NOT EXISTS staff_members (
                    hash_id TEXT PRIMARY KEY,
                    full_name TEXT NOT NULL,
                    photo_url TEXT,
                    is_visible BOOLEAN,
                    department_id INTEGER,
                    FOREIGN KEY (department_id) REFERENCES departments(id)
                )
            ''')
            
            await db.execute('''
                CREATE TABLE IF NOT EXISTS positions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    position_id INTEGER,
                    name TEXT NOT NULL,
                    visibility_role INTEGER,
                    type TEXT,
                    staff_member_id TEXT,
                    FOREIGN KEY (staff_member_id) REFERENCES staff_members(hash_id)
                )
            ''')
            
            await db.commit()
    
    async def save_departments(self, departments: list[Department]):
        async with aiosqlite.connect(self.db_path) as db:
            for dept in departments:
                await db.execute(
                    'INSERT OR REPLACE INTO departments (id, title, position) VALUES (?, ?, ?)',
                    (dept.id, dept.title, dept.position)
                )
                
                for member in dept.staff:
                    await db.execute(
                        '''INSERT OR REPLACE INTO staff_members 
                           (hash_id, full_name, photo_url, is_visible, department_id) 
                           VALUES (?, ?, ?, ?, ?)''',
                        (member.hash_id, member.full_name, member.photo_url, 
                         member.is_visible, dept.id)
                    )
                    
                    for position in member.positions:
                        await db.execute(
                            '''INSERT INTO positions 
                               (position_id, name, visibility_role, type, staff_member_id) 
                               VALUES (?, ?, ?, ?, ?)''',
                            (position.id, position.name, position.visibility_role, 
                             position.type, member.hash_id)
                        )
            
            await db.commit()
