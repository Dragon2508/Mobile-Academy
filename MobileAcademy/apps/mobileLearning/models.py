from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    second_name = models.CharField('Отчество', blank=True, default='', max_length= 150)
    birth_date = models.DateField('Дата рождения', blank=True, default=datetime.date(1,1,1))
    phone = models.CharField('Телефон', blank=True, default='',  max_length = 12)
    city = models.CharField('Город', blank=True, default='',  max_length = 150)
    region = models.CharField('Область', blank=True, default='',  max_length = 150)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

class Course(models.Model):
    title = models.CharField('Название курса', max_length = 200)

class AccessCourse(models.Model):
    course = models.ForeignKey(Course, on_delete= models.CASCADE)
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    is_access = models.BooleanField('Есть ли доступ к курсу')
    is_passed = models.BooleanField('Пройден ли курс')



