from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django.contrib import auth
from .forms  import CustomUserCreationForm

# mobileLearning/
def account(request):
    imageUser = request.user.profile.images
    if request.POST:
        post_data = request.POST
        if 'btnSave' in post_data:
            request.user.last_name = request.POST['last_name']
            request.user.first_name = request.POST['first_name']
            request.user.profile.second_name = request.POST['second_name']
            request.user.profile.birth_date = request.POST['birth_date']
            request.user.email = request.POST['email']
            request.user.profile.phone = request.POST['phone']
            request.user.profile.city = request.POST['city']
            request.user.profile.region = request.POST['region']
            request.user.profile.images = request.FILES['image']
            request.user.save()
            return HttpResponseRedirect(reverse('mobileLearning:account'))
    #print(imageUser.height)
    #print(imageUser.width)
    return render(request, 'mobileLearning/account.html',{'imageUser': imageUser})
def index(request):
    return render(request, 'mobileLearning/main.html')

def loginOut(request):
    auth.logout(request) 
    return HttpResponseRedirect(reverse('mobileLearning:main'))

def login(request):
    if request.POST:
        userName = request.POST['username']
        psw = request.POST['password']
        user = auth.authenticate(username=userName, password=psw)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('mobileLearning:main'))
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
                return HttpResponseRedirect(reverse('mobileLearning:main'))
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
    return render(request, 'mobileLearning/lections/lectionStart/lectionEmulator.html')
def lectionCSharp(request):
    return render(request, 'mobileLearning/lections/lectionStart/lectionCSharp.html')
def lectionVisual(request):
    return render(request, 'mobileLearning/lections/lectionStart/lectionVisual.html')
def lectionXamarin(request):
    return render(request, 'mobileLearning/lections/lectionStart/lectionXamarin.html')