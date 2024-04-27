from django.shortcuts import render,redirect

# Create your views here.
def projecthomepage(request):
    return render(request, 'projecthomepage.html')

def employeerhomepage(request):
    return render(request, 'employeerhomepage.html')

def jobseekerhomepage(request):
    return render(request, 'jobseekerhomepage.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

def signup(request):
    return render(request, 'signup.html')

def signup1(request):
    if request.method == 'POST':
        user_type = request.POST.get('user_type')
        username = request.POST['username']
        pass1 = request.POST['password']
        pass2 = request.POST['password1']

        # Basic password validation
        if len(pass1) < 8:
            messages.error(request, 'Password must be at least 8 characters long.')
            return render(request, 'signup.html')

        if pass1 != pass2:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'signup.html')

        # Differentiate between student and company signup based on username length
        if user_type == 'student' and len(username) != 10:
            messages.error(request, 'Student username must be exactly 10 digits long.')
            return render(request, 'signup.html')

        if user_type == 'company' and len(username) <= 3:
            messages.error(request, 'Company username must be greater than 3 characters long.')
            return render(request, 'signup.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken.')
            return render(request, 'signup.html')

        user = User.objects.create_user(username=username, password=pass1)
        user.save()
        messages.success(request, 'Account created successfully.')
        return redirect('login')
    else:
        return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            if len(username) == 10:
                return redirect('jobseekerhomepage')
            elif len(username) >= 3:
                return redirect('employeerhomepage')
            else:
                return redirect('projecthomepage')
        else:
            messages.error(request, 'Invalid Credentials')
            return render(request, 'login.html')
    else:
        return render(request,'login.html')
def logout(requst):
    auth.logout(requst)
    return render(requst, 'projecthomepage.html')