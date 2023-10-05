from django.db import models

class Student(models.Model):
    GENDER_F = (
        ('male', "Male"),
        ('female', 'Female'),
    )
    name = models.CharField(max_length=30)
    age = models.PositiveSmallIntegerField(default=20, blank=True, null=True)
    p_num = models.CharField(max_length=12, null=True, blank=True)
    email = models.EmailField(null=True, blank=True,)
    gender = models.CharField(max_length=6, blank=True, null= True)
    city = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True, null= True, blank=True)

    def __str__(self):
        return self.name

class Author(models.Model):
    GENDER_F = (
        ('male', "Male"),
        ('female', 'Female'),
    )

    name = models.CharField(max_length=30)
    age = models.PositiveSmallIntegerField(default=20)
    email = models.EmailField(null=True, blank=True)
    gender = models.CharField(max_length=6,choices=GENDER_F)
    city = models.CharField(max_length=30)
    is_alive = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=50)
    year = models.IntegerField()
    author = models.ManyToManyField(Author)
    genre = models.CharField(max_length=50)
    page = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Book_record(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.IntegerField(default=1)

    def __str__(self):
        return self.student.name
