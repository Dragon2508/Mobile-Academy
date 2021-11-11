from django.urls import path

from . import views

app_name = 'mobileLearning'
urlpatterns = [
    path('', views.index, name='main'),
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('listOfCourse/', views.listOfCourse, name='listOfCourse'),
    path('account/', views.account, name='account'),
    path('listOfCourse/lessonOne/', views.lessonOne, name='lessonOne'),
    path('listOfCourse/lessonTwo/', views.lessonTwo, name='lessonTwo'),
    path('listOfCourse/lessonThree/', views.lessonThree, name='lessonThree'),
    path('listOfCourse/lessonFour/', views.lessonFour, name='lessonFour'),
    path('listOfCourse/lessonFive/', views.lessonFive, name='lessonFive'),
    path('listOfCourse/Six/', views.lessonSix, name='lessonSix'),
    path('listOfCourse/testing/', views.testing, name='testing'),
]
