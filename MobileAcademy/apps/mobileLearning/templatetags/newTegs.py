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
    print(idUser)
    print(courseTitle)
    print(courseId)
    return AccessCourse.objects.get(user = idUser,  course = courseId)
