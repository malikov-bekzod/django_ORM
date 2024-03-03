from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length = 50)
    description = models.TextField()
    duration = models.IntegerField()


    def __str__(self):
        return f"{self.title}"

class Customer(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60, null=True)
    email = models.CharField(max_length=60)
    password = models.CharField(10)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class CustomerCourse(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
