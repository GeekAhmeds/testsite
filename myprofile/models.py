from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    username =   models.OneToOneField(User, on_delete=models.CASCADE)
    fname    =   models.CharField(max_length=240)
    jobtitle =   models.CharField(max_length=150, default='blank')
    photo    =   models.ImageField(upload_to='uploads/profiles/', default='blank')
    website  =   models.URLField(max_length=200, default='blank')
    bio      =   models.TextField(default='')
   
   
    def __str__(self):
        return self.username



class Social(models.Model):
    name = models.CharField(max_length=70)
    url  = models.URLField(max_length=200, default='blank')
    def __str__(self):
        return self.name



class CatResume(models.Model):
    title = models.CharField(max_length=70, verbose_name="Title")
    def __str__(self):
        return self.title



class MyResume(models.Model):

    title       = models.CharField(max_length=120)
    name        = models.CharField(max_length=120, null=True)
    year        = models.DateField(auto_now=False, auto_now_add=False)
    current     = models.BooleanField(default=False)
    desc        = models.TextField()
    icon        = models.CharField(max_length=50)
    category    = models.ForeignKey(CatResume, verbose_name=("Category"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("MyResume")
        verbose_name_plural = ("MyResumes")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("MyResume_detail", kwargs={"pk": self.pk})
