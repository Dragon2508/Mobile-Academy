from django import template
from mobileLearning.models import AccessCourse, Course

register = template.Library()

@register.simple_tag()
def find_in(str,word):
    return str.find(word)

@register.simple_tag()
def equating(str):
    return str

@register.simple_tag()
def getAccessCourse(idUser, courseTitle):
    courseId =  Course.objects.get(title = courseTitle).id
    # print(idUser)
    # print(courseTitle)
    # print(courseId)
    return AccessCourse.objects.get(user = idUser,  course = courseId)

@register.simple_tag()
def inkr(a, b):
    # print("-------------"+ str(a) + "------------------------")
    # print("-------------"+ str(b)+ "------------------------")
    i = a + b
    return i
    
@register.simple_tag()
def compare(a, b):
    c = a == b
    # print(c)
    return c

@register.simple_tag()
def takeElement(a, b):
    return a[b]