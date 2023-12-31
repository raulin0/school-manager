from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    birthday = models.DateField()

    def __str__(self):
        return f'{self.name}'


class Course(models.Model):
    LEVEL = (('B', 'Basic'), ('I', 'Intermediate'), ('A', 'Advanced'))
    name = models.CharField(max_length=100)
    level = models.CharField(
        max_length=1, choices=LEVEL, blank=False, null=False, default='B'
    )

    def __str__(self):
        return f'{self.name}, {self.level}'


class Enrollment(models.Model):
    PERIOD = (('M', 'Morning'), ('E', 'Evening'), ('N', 'Night'))
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    period = models.CharField(
        max_length=1, choices=PERIOD, blank=False, null=False, default='M'
    )
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.student.name}, {self.period}, {self.active}'
