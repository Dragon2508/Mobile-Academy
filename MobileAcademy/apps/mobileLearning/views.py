from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django.contrib import auth
from .forms  import CustomUserCreationForm
from .models import AccessCourse, Course, Lection, Profile
from django.core.files.storage import default_storage
import datetime

# mobileLearning/
def account(request):
    imageUser = request.user.profile.images
    data = []
    data.append(request.user.last_name)
    data.append(request.user.first_name)
    data.append(request.user.profile.second_name)
    data.append(request.user.profile.birth_date)
    data.append(request.user.email)
    data.append(request.user.profile.phone)
    data.append(request.user.profile.city)
    data.append(request.user.profile.region)
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
            try:
                request.user.profile.images = request.FILES['myfile']
            except:
                print('Не было фото')
            request.user.save()
            return HttpResponseRedirect(reverse('mobileLearning:account'))
        if 'btnDelete' in post_data:
            data = []
            data.append(request.POST['last_name'])
            data.append(request.POST['first_name'])
            data.append(request.POST['second_name'])
            try:
                data.append(datetime.datetime.strptime(request.POST['birth_date'], "%Y-%m-%d"))
            except:
                data.append(request.user.profile.birth_date)
            data.append(request.POST['email'])
            data.append(request.POST['phone'])
            data.append(request.POST['city'])
            data.append(request.POST['region'])
            try:
                default_storage.delete(str(request.user.profile.images))
            except:
                print('Не было фото')
            request.user.profile.images = Profile.images.field.get_default()
            request.user.save()
            imageUser = request.user.profile.images
            return render(request, 'mobileLearning/account.html',{'imageUser': imageUser, 'data': data})
        if 'data' in post_data:
            print('1----------------------------------------------------------------------')
    #print(imageUser.height)
    #print(imageUser.width)
    return render(request, 'mobileLearning/account.html',{'imageUser': imageUser, 'data': data})
def index(request):
    courses = Course.objects.all()[:4]
    lections = Lection.objects.all()[:4]
    return render(request, 'mobileLearning/main.html',{'courses': courses, 'lections': lections})

def loginOut(request):
    auth.logout(request) 
    return HttpResponseRedirect(reverse('mobileLearning:main'))

def login(request):
    chechAuthentication = True
    if request.POST:
        userName = request.POST['username']
        psw = request.POST['password']
        user = auth.authenticate(username=userName, password=psw)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('mobileLearning:main'))
        else: 
            chechAuthentication = False
            return render(request, 'mobileLearning/login.html',{'chechAuthentication': chechAuthentication})
    return render(request, 'mobileLearning/login.html',{'chechAuthentication': chechAuthentication})
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
                newIndex = (AccessCourse.objects.all().values_list('id',flat=True).last() + 1)
                obj = AccessCourse(id = newIndex, course = Course.objects.get(id = 1), user = user, is_access = True, is_passed = False, test_status = 'не начат')
                obj.save()
                return HttpResponseRedirect(reverse('mobileLearning:main'))
    context = {'form': form}
    return render(request, 'mobileLearning/registration.html', context)

# mobileLearning/courses/
def listOfCourse(request):
    search = ''
    filter = 'All'
    try:
        obj = Course.objects.all() 
        countCourse = obj.count()
    except:
        obj = None
        countCourse = 0
    if request.GET.get('navAll'):
        obj = Course.objects.all()
        filter = 'All'
        countCourse = obj.count()

        newObj = []
        search = request.GET['input_text']
        for course in obj:
            if search in str(course.title):
                newObj.append(course)
        countCourse = len(newObj)
        return render(request, 'mobileLearning/courses/listOfCourse.html',{'courses':newObj, 'countCourse':countCourse, 'filter': filter, 'search':search})
    if request.GET.get('navAndroid'):
        filter = 'Android'
        obj = Course.objects.filter(direction = 'Android')
        newObj = []
        search = request.GET['input_text']
        for course in obj:
            if search in str(course.title):
                newObj.append(course)
        countCourse = len(newObj)
        return render(request, 'mobileLearning/courses/listOfCourse.html',{'courses':newObj, 'countCourse':countCourse, 'filter': filter, 'search':search})
    if request.GET.get('navIOS'):
        try:
            filter = 'IOS'
            obj = Course.objects.filter(direction = 'IOS')
            countCourse = obj.count()
        except:
            obj = None
            countCourse = 0
        newObj = []
        search = request.GET['input_text']
        for course in obj:
            if search in str(course.title):
                newObj.append(course)
        countCourse = len(newObj)
        return render(request, 'mobileLearning/courses/listOfCourse.html',{'courses':newObj, 'countCourse':countCourse, 'filter': filter, 'search':search})
    if request.GET.get('input_text'):
        obj = Course.objects.all()
        newObj = []
        search = request.GET['input_text']
        for course in obj:
            if search in str(course.title):
                newObj.append(course)
        filter = 'All'
        countCourse = len(newObj)
        return render(request, 'mobileLearning/courses/listOfCourse.html',{'courses':newObj, 'countCourse':countCourse, 'filter': filter, 'search':search})
    return render(request, 'mobileLearning/courses/listOfCourse.html', {'courses':obj, 'countCourse':countCourse, 'filter': filter, 'search':search})

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
    obj = AccessCourse.objects.get( user = request.user.id,  course = 1)
    if request.POST:
        post_data = request.POST
        if 'btnYes' in post_data or 'btnNo' in post_data:
            obj.test_status = 'начат'
            obj.save()
            return HttpResponseRedirect(reverse('mobileLearning:testing'))
    print(str(obj.right_answers.find('(1)')) + '---------------------------------------------------')
    return render(request, 'mobileLearning/courses/courseStart/testing.html',{'AccessCourse':obj})

def answersOnQuestions(request):
    if request.POST:
        obj = AccessCourse.objects.get( user = request.user.id,  course = 1) 
        grade = 0
        if (request.POST['firstQuestion'] == '2'):
            obj.right_answers += '(1)'
            grade +=1
        else:
            obj.wrong_answers += ' (1-'+ request.POST['firstQuestion']+')'
        if (request.POST['secondQuestion'] == '4'):
            obj.right_answers += '(2)'
            grade +=1
        else:
            obj.wrong_answers += ' (2-'+ request.POST['secondQuestion']+')'
        if (request.POST['thirdQuestion'] == '1'):
            obj.right_answers += '(3)'
            grade +=1
        else:
            obj.wrong_answers += ' (3-'+ request.POST['thirdQuestion']+')'
        if (request.POST['fourthQuestion'] == '2'):
            obj.right_answers += '(4)'
            grade +=1
        else:
            obj.wrong_answers += ' (4-'+ request.POST['fourthQuestion']+')'
        if (request.POST['fifthQuestion'] == '2'):
            obj.right_answers += '(5)'
            grade +=1
        else:
            obj.wrong_answers += ' (5-'+ request.POST['fifthQuestion']+')'

        obj.test_status = str(grade)
        
        obj.save()
        return HttpResponseRedirect(reverse('mobileLearning:testing'))

# mobileLearning/lections/
def listOfLection(request):
    search = ''
    filter = 'All'
    try:
        obj = Lection.objects.all() 
        countLections = obj.count()
    except:
        obj = None
        countLections = 0
    if request.GET.get('navAll'):
        obj = Lection.objects.all()
        filter = 'All'
        countLections = obj.count()
        
        newObj = []
        search = request.GET['input_text']
        for lection in obj:
            if search in str(lection.title):
                newObj.append(lection)
        countLections = len(newObj)
        return render(request, 'mobileLearning/lections/listOfLection.html',{'lections':newObj, 'countLections':countLections, 'filter': filter, 'search':search})
    if request.GET.get('navAndroid'):
        filter = 'Android'
        obj = Lection.objects.filter(direction = 'Android')
        countLections = obj.count()

        newObj = []
        search = request.GET['input_text']
        for lection in obj:
            if search in str(lection.title):
                newObj.append(lection)
        countLections = len(newObj)
        return render(request, 'mobileLearning/lections/listOfLection.html',{'lections':newObj, 'countLections':countLections, 'filter': filter, 'search':search})
    if request.GET.get('navIOS'):
        try:
            filter = 'IOS'
            obj = Lection.objects.filter(direction = 'IOS')
            countLections = obj.count()
        except:
            obj = None
            countLections = 0
        
        newObj = []
        search = request.GET['input_text']
        for lection in obj:
            if search in str(lection.title):
                newObj.append(lection)
        countLections = len(newObj)
        return render(request, 'mobileLearning/lections/listOfLection.html',{'lections':newObj, 'countLections':countLections, 'filter': filter, 'search':search})
    if request.GET.get('input_text'):
        obj = Lection.objects.all()
        newObj = []
        search = request.GET['input_text']
        for lection in obj:
            if search in str(lection.title):
                newObj.append(lection)
        filter = 'All'
        countLections = len(newObj)
        return render(request, 'mobileLearning/lections/listOfLection.html',{'lections':newObj, 'countLections':countLections, 'filter': filter, 'search':search})
    return render(request, 'mobileLearning/lections/listOfLection.html',{'lections':obj, 'countLections':countLections, 'filter': filter, 'search':search})

# mobileLearning/lections/lectionStart/
def lectionEmulator(request):
    return render(request, 'mobileLearning/lections/lectionStart/lectionEmulator.html')
def lectionCSharp(request):
    return render(request, 'mobileLearning/lections/lectionStart/lectionCSharp.html')
def lectionVisual(request):
    return render(request, 'mobileLearning/lections/lectionStart/lectionVisual.html')
def lectionXamarin(request):
    return render(request, 'mobileLearning/lections/lectionStart/lectionXamarin.html')