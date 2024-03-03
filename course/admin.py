from django.contrib import admin
from .models import Course,Customer,CustomerCourse
# Register your models here.
admin.site.register(Course)
admin.site.register(Customer)
admin.site.register(CustomerCourse)
