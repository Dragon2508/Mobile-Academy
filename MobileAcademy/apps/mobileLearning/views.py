from django.shortcuts import render

def index(request):
    return render(request, 'mobileLearning/main.html')


def login(request):
    return render(request, 'mobileLearning/login.html')
    
def registration(request):
    return render(request, 'mobileLearning/registration.html')

def listOfCourse(request):
    return render(request, 'mobileLearning/listOfCourse.html')

def account(request):
    return render(request, 'mobileLearning/account.html')

def lessonOne(request):
    return render(request, 'mobileLearning/lessonOne.html')

def lessonTwo(request):
    return render(request, 'mobileLearning/lessonTwo.html')

def lessonThree(request):
    return render(request, 'mobileLearning/lessonThree.html')

def lessonFour(request):
    return render(request, 'mobileLearning/lessonFour.html')

def lessonFive(request):
    return render(request, 'mobileLearning/lessonFive.html')

def lessonSix(request):
    return render(request, 'mobileLearning/lessonSix.html')

def testing(request):
    return render(request, 'mobileLearning/testing.html')