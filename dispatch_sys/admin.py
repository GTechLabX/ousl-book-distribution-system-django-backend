from django.contrib import admin
from .models import (
    Faculty,
    Department,
    DegreeProgram,
    Course,
    DegreeProgramCourse,
    District,
    Center,
    Student,
    StudentCourse,
    BookReservation,
    Book,
    CenterBook,
    ReceivedBook,
    StudentQRCode
)

# Register all models
admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(DegreeProgram)
admin.site.register(Course)
admin.site.register(DegreeProgramCourse)
admin.site.register(District)
admin.site.register(Center)
admin.site.register(Student)
admin.site.register(StudentCourse)
admin.site.register(Book)
admin.site.register(CenterBook)
admin.site.register(ReceivedBook)
admin.site.register(StudentQRCode)
admin.site.register(BookReservation)

