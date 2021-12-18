from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    second_name = models.CharField('Отчество', blank=True, default='', max_length= 150)
    birth_date = models.DateField('Дата рождения', blank=True, default=datetime.datetime.now())
    phone = models.CharField('Телефон', blank=True, default='',  max_length = 12)
    city = models.CharField('Город', blank=True, default='',  max_length = 150)
    region = models.CharField('Область', blank=True, default='',  max_length = 150)
    images = models.ImageField('Фото', upload_to ='media/', default = 'None')

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

class Course(models.Model):
    title = models.CharField('Название курса', max_length = 200, default='')
    image = models.CharField('Фото курса', max_length = 200, default='')
    time = models.CharField('Время прохождения',max_length = 20, default='')
    start_course = models.CharField('Ссылка на старт курса',max_length = 50, default='')

class AccessCourse(models.Model):
    course = models.ForeignKey(Course, on_delete= models.CASCADE)
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    is_access = models.BooleanField('Есть ли доступ к курсу')
    is_passed = models.BooleanField('Пройден ли курс')
    test_status = models.CharField('Статус теста', default='не начат', max_length=20)
    right_answers = models.CharField('Правильные варианты ответа', default='', max_length=50)
    wrong_answers = models.CharField('Неправильные варианты ответа', default='', max_length=50)

class Lection(models.Model):
    title = models.CharField('Название курса', max_length = 200, default='')
    image = models.CharField('Фото курса', max_length = 200, default='')
    time = models.CharField('Время прохождения',max_length = 20, default='')
    start_lection = models.CharField('Ссылка на старт курса',max_length = 50, default='')
    direction = models.CharField('Направление подготовки',max_length = 50, default='ALL')



