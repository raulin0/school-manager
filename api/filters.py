import django_filters

from api.models import Enrollment


class EnrollmentFilter(django_filters.FilterSet):
    class Meta:
        model = Enrollment
        fields = {
            'student_id': ['exact'],
            'course_id': ['exact'],
            'period': ['exact'],
            'active': ['exact'],
        }
