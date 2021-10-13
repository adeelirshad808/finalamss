from django import forms
import difflib
import PyPDF2
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from project.models import Teacher
from project.models import Student
from project.models import Submissions
from project.models import Assignment
from project.forms import UserRegisterationForm
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    teachers = Teacher.objects.all()
    loggedin_user = request.user
    is_registerred = False
    assignments = Assignment.objects.all()
    students = Student.objects.all()
    if request.user.is_authenticated:
        s = Student.objects.filter(student_username=loggedin_user).exists()
        t = Teacher.objects.filter(teacher_username=loggedin_user).exists()
        print(s)
        print(t)

        print('user', request.user.is_authenticated)
        if s == True:
            print(s)
            is_registerred = True
            print('inside s assignment page')
            return render(request, 'project/assignmentspage.html',
                          {'assignments': assignments})
        if s == False and t == False:
            print(t)

            print('inside s not registererd runnning')
            return render(request, 'project/not_registered.html',
                          {'loggedin_user': loggedin_user})
        if t:
            print('running 3')
            is_registerred = True
            assignments = Submissions.objects.all()
            for assignment in assignments:
                print('assignments', assignments)
                return render(request, 'project/teacher.html', {'assignments': assignments})
    else:
        print('running 2')
        return render(request, 'project/home.html', {'is_registerred': is_registerred})


def teacher(request):
    print('running')
    if request.method == "POST":
        task = request.POST.get('task')
        teacher_instance = Teacher.objects.get(teacher_username=request.user)
        task = Assignment.objects.create(assignment_creator=teacher_instance,
                                         assignment_details=task)
        print(task)
        task.save()
        return HttpResponse('task created')

    else:
        all_assignments = Submissions.objects.all()
        # print(all_assignments)
        # text1 = []
        # for sub1 in all_assignments:
        #     text1.append(open(f'./media/{sub1.submission_file}', 'rb').read())

        # for sub in all_assignments:
        #     print(sub.submission_file)
        #     text = open(f'./media/{sub.submission_file}', 'rb').read()
        # print(text1)

        # print(difflib.SequenceMatcher(None, text, text1).ratio()*100)

        return render(request, 'project/teacher.html',
                      {'assignments': all_assignments})


def assignment(request):
    username = request.user
    if request.method == "POST":

        uploaded_file = request.FILES['inputFile']
        print(uploaded_file)
        student = Student.objects.get(student_name=request.user)
        std_instance = student
        document = Submissions.objects.create(submitted_by=std_instance,
                                              submission_file=uploaded_file)
        document.save()

        return HttpResponse('you file uploaded')
    return render(request, 'project/assignment.html')


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserRegisterationForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            print(user)
            registered = True
    else:
        user_form = UserRegisterationForm()

    return render(request, 'project/register.html', {
        'registered': registered,
        'user_form': user_form
    })


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                print(user.is_active)
                login(request, user)
                return redirect('index')
            else:
                return HttpResponse('Account is deactivated')
        else:
            return HttpResponse('Please use correct username and password')
    else:
        print('running')
        return render(request, 'project/login.html')


@ login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def check_plagirism(request):
    all_assignments = Submissions.objects.all()
    # print(all_assignments)
    text1 = []
    # for sub1 in all_assignments:
    #     text1.append(open(f'./media/{sub1.submission_file}', 'rb').read())

    for sub in all_assignments:
        print(sub.submission_file)
        text = open(f'./media/{sub.submission_file}', 'rb').read()
    print(text1)

    # print(difflib.SequenceMatcher(None, text, text1).ratio()*100)

    print('runninggggg')
    if request.method == "POST":
        file = request.POST.get('checkPlagirism')
        print('jjj')
        print('print', file)

    return render(request, 'project/check_plagirism.html')
