from django.contrib import admin

from api.models import Course, Enrollment, Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'cpf',
        'birthday',
    )
    list_display_links = ('id', 'name')
    search_fields = ('name', 'cpf')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'level')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'level')


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'student',
        'course',
        'period',
        'active',
    )
    list_display_links = ('id', 'student', 'course')
    search_fields = ('student', 'course', 'period', 'active')
