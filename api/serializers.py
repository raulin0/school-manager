from rest_framework import serializers

from api.models import Course, Enrollment, Student
from api.utils.student_validators import (
    is_valid_cpf,
    is_valid_name,
)


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def validate(self, data):
        if not is_valid_cpf(data['cpf']):
            raise serializers.ValidationError(
                {'cpf': 'Número de CPF inválido'}
            )
        if not is_valid_name(data['name']):
            raise serializers.ValidationError(
                {'nome': 'Não inclua números neste campo'}
            )

        return data


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'
