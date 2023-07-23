from django.db import models

# Create your models here.
class Student(models.Model):
    number = models.PositiveBigIntegerField()
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    study = models.CharField(max_length=50)
    gpa = models.FloatField()

    def __str__(self):
        return f'Студент: {self.name} Фамилия: {self.last_name}'