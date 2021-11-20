from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    second_name = models.CharField('Отчество', blank=True, null = True, max_length= 150)
    birth_date = models.DateField('Дата рождения', blank=True, null = True)
    phone = models.CharField('Телефон', blank=True, null = True,  max_length = 12)
    city = models.CharField('Город', blank=True, null = True,  max_length = 150)
    region = models.CharField('Область', blank=True, null = True,  max_length = 150)

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



