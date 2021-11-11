from django.contrib import admin

from .models import Profile, Course, AccessCourse

admin.site.register(Profile)
admin.site.register(Course)
admin.site.register(AccessCourse)
