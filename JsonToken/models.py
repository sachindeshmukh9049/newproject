from django.db import models

# Create your models here.


class Student(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    address=models.TextField()

    def __str__(self):
        return self.first_name


class Branch(models.Model):
    branch_name=models.CharField(max_length=100)
    student=models.ManyToManyField(Student)
    joined_on=models.DateField()
    
    def __str__(self):
        return self.branch_name