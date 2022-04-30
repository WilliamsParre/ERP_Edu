from http.client import HTTPResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import allowed_user
from django.contrib.auth.models import Group
from django.shortcuts import redirect, render
from .forms import signUpForm, OrginizationRegistrationForm, FacultyRegistriationForm, NonTeachingFacultyRegistriationForm
from leave.forms import Leave, LeaveForm, NonTeachingLeaveForm
from .models import Course, Student


@login_required(login_url='login')
def home(request):
    return render(request, 'base/dashboard.html')


def login_page(request):

    page = 'login'

    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exists')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password doesnot exist')

    context = {'page': page}
    return render(request, 'base/login_register.html', context)


@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('home')


def signup_page(request):
    form = signUpForm()

    if request.method == 'POST':
        form = signUpForm(request.POST)
        form2 = OrginizationRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.is_active = False
            lecturer = Group.objects.get(name='Lecturer')
            user.save()
            user.groups.add(lecturer)
            user.save()
            messages.success(
                request, 'Registered successful! Account created successfully!')
            org = OrginizationRegistrationForm()
            faculty = FacultyRegistriationForm()
            non_teaching = NonTeachingFacultyRegistriationForm()
            return render(request, 'base/registration.html', {'org': org, 'faculty': faculty, 'non_teaching': non_teaching})
        else:
            messages.error(request, 'An error occured during regestration')

    return render(request, 'base/login_register.html', {'form': form})


def org_registration(request):

    if request.method == 'POST':
        form = OrginizationRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Registered successful! Orginization added successfully.')
        else:
            messages.error(request, 'An error occured during regestration')

    return redirect('signup')


def faculty_registration(request):

    if request.method == 'POST':
        form = FacultyRegistriationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Registered successful! Message is sent to you orginisation for account activation.')
        else:
            messages.error(request, 'An error occured during regestration')

    return redirect('signup')

def non_teaching_registration(request):
    
    if request.method == 'POST':
        form = NonTeachingFacultyRegistriationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Registered successful! Message is sent to you orginisation for account activation.')
        else:
            messages.error(request, 'An error occured during regestration')
    
    return redirect('signup')

@login_required(login_url='login')
def user_profile(request):
    # user = User.objects.get(id=pk)
    # context = {'user': user}
    return render(request, 'base/profile.html')


@login_required(login_url='login')
def dashboard(request):
    return render(request, 'base/dashboard.html')


@login_required(login_url='login')
def courses(request):
    return render(request, 'base/courses.html')


@login_required(login_url='login')
def attendance(request):
    return render(request, 'base/attendance.html')


@login_required(login_url='login')
@allowed_user(roles=['admin', 'Lecturer', 'non_teaching'])
def leave(request):
    if request.user.groups.all()[0].name == 'non_teaching':
        form = NonTeachingLeaveForm()
    else:
        form = LeaveForm()
    
    if request.method == "POST":
        if request.user.groups.all()[0].name == 'non_teaching':
            form = NonTeachingLeaveForm(request.POST)
        else:
            form = LeaveForm(request.POST)
        if form.is_valid():
            form.save()
            form = LeaveForm()
            messages.success(
                request, 'Leave has been applied successfully! Message is sent to you orginisation for leave approval.')
        else:
            messages.error(request, 'An error occured during leave processing.')
            
    return render(request, 'base/leave.html', {'form': form})


@login_required(login_url='login')
def fees(request):
    return render(request, 'base/fees.html')


@login_required(login_url='login')
def grades(request):
    return render(request, 'base/grades.html')


@login_required(login_url='login')
def qualification(request):
    return render(request, 'base/qualification.html')


def settings(request):
    return render(request, 'base/settings.html')

def accept(request):
    
    print(Leave.objects.get().all()[0].name)
    
    return