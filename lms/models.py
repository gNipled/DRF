from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=200)
    preview = models.ImageField()
    description = models.TextField()

    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'courses'

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    preview = models.ImageField()
    video_link = models.CharField(max_length=400)
    course = models.ManyToManyField(
        'Course',
    )

    class Meta:
        verbose_name = 'lesson'
        verbose_name_plural = 'lessons'

    def __str__(self):
        return self.name
