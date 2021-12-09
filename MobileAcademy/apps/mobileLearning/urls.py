from django.urls import path

from . import views

app_name = 'mobileLearning'
urlpatterns = [
    path('', views.index, name='main'),
    path('loginOut', views.loginOut, name='loginOut'),
    path('login', views.login, name='login'),
    path('registration', views.registration, name='registration'),
    path('account', views.account, name='account'),
    # Courses
    path('listOfCourse', views.listOfCourse, name='listOfCourse'),
    path('listOfCourse/lessonOne', views.lessonOne, name='lessonOne'),
    path('listOfCourse/lessonTwo', views.lessonTwo, name='lessonTwo'),
    path('listOfCourse/lessonThree', views.lessonThree, name='lessonThree'),
    path('listOfCourse/lessonFour', views.lessonFour, name='lessonFour'),
    path('listOfCourse/lessonFive', views.lessonFive, name='lessonFive'),
    path('listOfCourse/Six', views.lessonSix, name='lessonSix'),
    path('listOfCourse/testing', views.testing, name='testing'),
    # Lections
    path('listOfLection', views.listOfLection, name='listOfLection'),
    path('listOfLection/lectionEmulator', views.lectionEmulator, name='lectionEmulator'),
    path('listOfLection/lectionCSharp', views.lectionCSharp, name='lectionCSharp'),
    path('listOfLection/lectionVisual', views.lectionVisual, name='lectionVisual'),
    path('listOfLection/lectionXamarin', views.lectionXamarin, name='lectionXamarin'),
]
