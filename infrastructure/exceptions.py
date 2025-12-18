
class TeacherFetcherException(Exception):
    pass


class BadSchoolData(TeacherFetcherException):
    pass


class FailedToLoadTeachers(TeacherFetcherException):
    pass
