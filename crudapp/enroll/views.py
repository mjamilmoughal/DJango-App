from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import StudentRegisteration
from .models import User
# Create your views here.

# Function to add a new record


def show_Index(request):
    if request.method == "POST":
        fm = StudentRegisteration(request.POST)
        if fm.is_valid():
            _name = fm.cleaned_data['name']
            _email = fm.cleaned_data['email']
            _password = fm.cleaned_data['password']
            new_obj = User(name=_name, email=_email, password=_password)
            new_obj.save()
            fm = StudentRegisteration()
    else:
        fm = StudentRegisteration()
    users_list = User.objects.all()
    return render(request, 'enroll/addIndex.html', {'form': fm, 'users_list': users_list})


def sample_page(request):
    products = ['apple', 'banana', 'orange']
    return render(request, 'enroll/sample.html', {'products': products})


def delete_user(request, id):
    if request.method == "POST":
        user = User.objects.get(pk=id)
        user.delete()
    return HttpResponseRedirect("/")
