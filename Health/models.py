from django.db import models


class Blood_type(models.TextChoices):
    A = 'A+'
    a = 'A-'
    B = 'B'
    AB = 'AB'
    O = 'O'


class health_state (models.Model):
    id_number = models.CharField(max_length=14, default=None)
    name = models.CharField(max_length=200, default=None)
    Blood_quarter = models.CharField(max_length=3, choices=Blood_type.choices, default=None)
    health_problem = models.CharField(max_length=500, default=None)

def __str__(self):
    return f"{self.id_num}"


class medical_history (models.Model):
    chronic_diseases = models.CharField(max_length=100,default=None)
    another_diseases = models.CharField(max_length=100, default=None)


