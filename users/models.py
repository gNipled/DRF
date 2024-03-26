from django.contrib.auth.models import AbstractUser
from django.db import models

from lms.models import Course, Lesson

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(verbose_name='email', unique=True)
    is_active = models.BooleanField(verbose_name='active', default=False)

    avatar = models.ImageField(upload_to='users/', verbose_name='avatar', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='phone number', **NULLABLE)
    country = models.CharField(max_length=100, verbose_name='country', **NULLABLE)
    verification_key = models.CharField(max_length=15, verbose_name='verification key', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Payments(models.Model):
    CASH = 'CS'
    TRANSFER = 'TR'
    PAYMENT_METHOD_CHOICES = [
        (CASH, 'Cash'),
        (TRANSFER, 'Bank transfer')
    ]

    user = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='user', **NULLABLE)
    payment_date = models.DateTimeField(auto_now_add=True, verbose_name='payment date')
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, verbose_name='course', **NULLABLE)
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, verbose_name='lesson', **NULLABLE)
    payed_amount = models.IntegerField(verbose_name='amount payed')
    payment_method = models.CharField(max_length=2, choices=PAYMENT_METHOD_CHOICES, verbose_name='payment method')


class Subscriptions(models.Model):
    users = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='course')