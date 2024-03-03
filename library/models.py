from django.db import models


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length = 60)
    birth_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    title = models.CharField(max_length = 60)
    description = models.TextField()
    count = models.IntegerField

    def __str__(self):
        return f"{self.title}"
class AuthorBook(models.Model):
    author_id = models.ForeignKey(Author,on_delete = models.CASCADE)
    book_id = models.ForeignKey(Book,on_delete = models.CASCADE)


class User(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60,null = True)
    email = models.CharField(max_length=60)
    password = models.CharField(10)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
class Review(models.Model):
    text = models.TextField()
    start_count = models.IntegerField()
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.text}"


class Teacher(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60, null=True)
    email = models.CharField(max_length=60)
    password = models.CharField(10)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Subject(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()

class TeacherSubject(models.Model):
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
