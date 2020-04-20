from django.contrib import admin
from .models import UserProfile, Social, MyResume,CatResume
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Social)
admin.site.register(MyResume)
admin.site.register(CatResume)
