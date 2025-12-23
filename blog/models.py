from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User





class Department(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Member(models.Model):
    name = models.CharField(max_length=200, unique=True)
    position = models.CharField(max_length=200, unique=True)
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="", blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    department = models.ForeignKey(Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="members"
    )


    def __str__(self):
        return self.name




class BlogImage(models.Model):
    image = models.ImageField(upload_to="", blank=True, null=True)

    def __str__(self):
        return self.image.name if self.image else "No image"

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    background = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to="", blank=True, null=True)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="authors/", blank=True, null=True)

    def __str__(self):
        return self.user.username

class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="", blank=True, null=True)
    images = models.ManyToManyField(BlogImage, related_name="gallery")
    description = RichTextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(default=datetime.now)

    category = models.ForeignKey(Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="blogs"
    )

    author = models.ForeignKey(
        'Author',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="blogs"
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-create_at']

class JobApplication(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    cv = models.FileField(upload_to='cvs/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

class Services(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


