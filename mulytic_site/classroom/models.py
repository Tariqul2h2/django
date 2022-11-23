from django.db import models

# Create your models here.

class Department(models.Model):
    dept = models.CharField(max_length=200)
    seat_cap = models.IntegerField(default=0)
    dept_code = models.CharField(max_length=5) #eg: CSE, CE, EEE, ARCH, ME

    def __str__(self) -> str:
        return self.dept_code

class Course(models.Model):
    couse_name = models.CharField(max_length=200)
    course_code = models.CharField(max_length=10)
    dept = models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.course_code

class Student(models.Model):
    student_id = models.CharField(max_length=20)
    student_name = models.CharField(max_length=200)
    student_phone_number = models.CharField(max_length=15)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    course_code = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.student_id
