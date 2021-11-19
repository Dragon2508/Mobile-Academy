from django.shortcuts import render

# mobileLearning/
def account(request):
    return render(request, 'mobileLearning/account.html')
def index(request):
    return render(request, 'mobileLearning/main.html')
def login(request):
    return render(request, 'mobileLearning/login.html')
def registration(request):
    return render(request, 'mobileLearning/registration.html')

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