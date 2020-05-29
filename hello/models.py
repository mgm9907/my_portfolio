from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=200)

    class Meta:
        db_table='student_info'
