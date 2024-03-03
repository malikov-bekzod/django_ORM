from django.contrib import admin
from .models import Book,Author,AuthorBook,Review,Teacher,Subject,TeacherSubject
# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(AuthorBook)
admin.site.register(Review)
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(TeacherSubject)
