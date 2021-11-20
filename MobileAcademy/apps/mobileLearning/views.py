from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django.contrib import auth
from .forms  import CustomUserCreationForm

# mobileLearning/
def account(request):
    return render(request, 'mobileLearning/account.html')
def index(request):
    return render(request, 'mobileLearning/main.html')
def login(request):
    if request.POST:
        userName = request.POST['username']
        psw = request.POST['password']
        user = auth.authenticate(username=userName, password=psw)
        if user is not None:
            auth.login(request, user)
            return render(request, 'mobileLearning/main.html')
    return render(request, 'mobileLearning/login.html')
def registration(request):
    form = CustomUserCreationForm()
    if request.POST:
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.save()
            user = auth.authenticate(username = request.POST['username'], password = request.POST['password2'])
            if user is not None:
                auth.login(request, user)
                return render(request, 'mobileLearning/main.html')
    context = {'form': form}
    return render(request, 'mobileLearning/registration.html', context)

# mobileLearning/courses/
def listOfCourse(request):
    return render(request, 'mobileLearning/courses/listOfCourse.html')

# mobileLearning/courses/courseStart/
def lessonOne(request):
    return render(request, 'mobileLearning/courses/courseStart/lessonOne.html')
def lessonTwo(request):
    return render(request, 'mobileLearning/courses/courseStart/lessonTwo.html')
def lessonThree(request):
    return render(request, 'mobileLearning/courses/courseStart/lessonThree.html')
def lessonFour(request):
    return render(request, 'mobileLearning/courses/courseStart/lessonFour.html')
def lessonFive(request):
    return render(request, 'mobileLearning/courses/courseStart/lessonFive.html')
def lessonSix(request):
    return render(request, 'mobileLearning/courses/courseStart/lessonSix.html')
def testing(request):
    return render(request, 'mobileLearning/courses/courseStart/testing.html')

# mobileLearning/lections/
def listOfLection(request):
    return render(request, 'mobileLearning/lections/listOfLection.html')

# mobileLearning/lections/lectionStart/
def lectionEmulator(request):
    return render(request, 'mobileLearning/lections/lectionStart/lectionCSharp.html')
def lectionCSharp(request):
    return render(request, 'mobileLearning/lections/lectionStart/lectionEmulator.html')
def lectionVisual(request):
    return render(request, 'mobileLearning/lections/lectionStart/lectionVisual.html')
def lectionXamarin(request):
    return render(request, 'mobileLearning/lections/lectionStart/lectionXamarin.html')