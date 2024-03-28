from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    name = models.CharField(max_length=200, verbose_name='name')
    preview = models.ImageField(upload_to='product_img/', verbose_name='course preview', **NULLABLE)
    description = models.TextField(verbose_name='description', **NULLABLE)
    owner = models.ForeignKey('users.User', on_delete=models.SET_NULL, **NULLABLE)
    price = models.PositiveIntegerField(**NULLABLE)

    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'courses'

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(max_length=200, verbose_name='name')
    description = models.TextField(verbose_name='description', **NULLABLE)
    preview = models.ImageField(upload_to='product_img/', verbose_name='product preview', **NULLABLE)
    video_link = models.CharField(max_length=400, **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='course')
    owner = models.ForeignKey('users.User', on_delete=models.SET_NULL, **NULLABLE)
    price = models.PositiveIntegerField(**NULLABLE)

    class Meta:
        verbose_name = 'lesson'
        verbose_name_plural = 'lessons'

    def __str__(self):
        return self.name
