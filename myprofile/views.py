from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile, Social, MyResume, CatResume



users = UserProfile.objects.order_by('id')
u = UserProfile.objects.order_by('id')
form = UserCreationForm()
link = Social.objects.order_by('id')
catresume = CatResume.objects.all() 
resume = MyResume.objects.order_by('category')

# Create your views here.
context = {'users' : users, 'form' : form, 'link' : link, 'catresume' : catresume, 'resume' : resume}
def index(request):
    return render(request,'myprofile/index.html', context)

def signUp(request):
    return render(request, 'signup/signUp.html', context)