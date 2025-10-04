from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Subject(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]


class Course(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="courses_created"
    )
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, related_name="courses"
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title


class Module(models.Model):
    course = models.ForeignKey(Course, related_name="modules", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
