from typing import List
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
from project.forms import UserRegisterationForm, assignmentUploadForm
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib import messages
import json

from django.views.generic import CreateView


class AddAssignmentView(CreateView):
    print('viewwww')
    model = Submissions
    form_class = assignmentUploadForm
    template_name = 'project/assignment.html'


def index(request):
    # yag = yagmail.SMTP('adeelirshad440@gmail.com', 'beiquczthbimflzt')
    # yag.send('kashifhussainrajpout@gmail.com',
    #          contents='hey ')

    print('running 1')

    teachers = Teacher.objects.all()
    loggedin_user = request.user
    is_registerred = False
    assignments = Assignment.objects.all()
    students = Student.objects.all()
    if request.user.is_authenticated:
        s = Student.objects.filter(student_username=loggedin_user).exists()
        t = Teacher.objects.filter(teacher_username=loggedin_user).exists()

        if s == True:
            submissions = Submissions.objects.all()
            submissions = (Submissions.objects.filter(
                submitted_by=Student.objects.get(student_username=loggedin_user)))

            context = {
                'submissions': submissions,
                'assignments': assignments,
                'list': list
            }
            return render(request, 'project/assignmentspage.html', context)

        if s == False and t == False:
            print(t)

            print('inside s not registererd runnning')
            return render(request, 'project/not_registered.html',
                          {'loggedin_user': loggedin_user})
        if t:
            print('running 3')
            is_registerred = True
            # all_assignments = Assignment.objects.all()
            # for ass in all_assignments:
            print(request.user)

            assignments = Submissions.objects.filter(
                submitted_to=Teacher.objects.get(teacher_username=request.user))

            print(assignments,)
            return render(request, 'project/teacher.html', {
                'assignments': assignments
            })
    else:
        print('running 2')
        return render(request, 'project/home.html', {'is_registerred': is_registerred})


def teacher(request):
    print('running')
    if request.method == "POST":
        task = request.POST.get('task')
        teacher_instance = Teacher.objects.get(
            teacher_username=request.session[''])
        task = Assignment.objects.create(assignment_creator=teacher_instance,
                                         assignment_details=task)
        print(task)
        task.save()
        return HttpResponse('task created')

    else:
        all_assignments = Submissions.objects.all()
        all_assignments = Submissions.objects.filter(
            submitted_to=Teacher.objects.get(teacher_username=request.user))
        assignments = Assignment.objects.filter()

        # assignment_creator=Teacher.objects.get(teacher_username=request.user)).order_by('-assignment_date')
        print(all_assignments)
        assignments = []
        for ass in all_assignments:
            print(ass)
            assignments.append(ass)

        return render(request, 'project/teacher.html',
                      {'assignments': assignments})


def assignment(request):
    print('-------\n\n\n------------')
    username = type(request.user)
    assignments = Assignment.objects.all()

    if request.method == 'POST':
        assignment_name = request.POST.get('filename')
        print('assignemntname', assignment_name)
        user_form = assignmentUploadForm(request.POST, request.FILES)
        print(user_form)
        if user_form.is_valid():
            user_form.save(commit=False)
            user_form.submission_status = Submissions.objects.get(
                submission_status=True)
            user_form.save()
        else:
            user_form = assignmentUploadForm()
            print(request.method)
        return render(request, 'project/asspagee1.html', {'user_form': user_form, 'assignments': assignments})


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserRegisterationForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            print(user)
            registered = True
            # yag = yagmail.SMTP('adeelirshad440@gmail.com', 'beiquczthbimflzt')
            # yag.send('kashifhussainrajpout@gmail.com',
            #  contents='hey ')

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
        # user = authenticate(username=username, password=password)
        if(authenticate(username=username, password=password)):
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    print(user.is_active)
                    login(request, user)
                    return redirect('index')
                else:
                    return HttpResponse('Account is deactivated')
            else:
                return render(request, 'project/login.html')
        else:
            return render(request, 'project/failed_login.html')

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
        print('print', file)
        text = open(f'./media/{file}', 'rb').read()
        simStd = []
        simIndx = []
        for sub in all_assignments:
            if (str(sub.submission_file) != str(file)):
                print(sub.submission_file)
                print(sub.submitted_by)
                text1 = open(f'./media/{sub.submission_file}', 'rb').read()
                simIndx.append(difflib.SequenceMatcher(
                    None, text, text1).ratio()*100)

                simStd.append(sub.submitted_by)
        print(simStd, simIndx)
        mylist = zip(simStd, simIndx)

    return render(request, 'project/check_plagirism.html',
                  {'simIndx': simIndx,
                   'simStd': simStd,
                   'mylist': mylist}
                  )


def online_plagirism(request):
    print('running')
    if request.method == "POST":
        file = request.POST.get('online_plagirism')
        print('print', file)
        text = open(f'./media/{file}', 'rb').read()

    with open(f'./media/my.json', 'rb')as jsonfile:
        # with open('./sample.json') as jsonfile:
        response = json.load(jsonfile)

    # print(response)
    print(
        '\n\n\n\nsources', response['sources']
    )
    # response['sources'] = {'a', 'b'}

    return render(request, 'project/online_plagirism.html',
                  {'plagPercent':  response['plagPercent'],
                   'uniquePercent':  response['uniquePercent'],
                   'paraphrasePercent':  response['paraphrasePercent'],
                   'sources':  response['sources'],
                   'details': response['details']
                   }
                  )


def marks(request):
    if request.method == "POST":
        marks = request.POST.get('marks')
        name = request.POST.get('stdname')
        file = request.POST.get('filename')
        print(marks, file, name)

    return render(request, 'project/marks.html')


def result(request):
    print('1111')
    if request.method == "POST":
        print('22222')

        submissions = Submissions.objects.filter(submitted_by=Student.objects.get(
            student_username=request.user))
        print(submissions)

    return render(request, 'project/result.html', {'submissions': submissions})


def readfile(request):
    if request.method == "POST":
        file = request.POST.get('readfile')
        print('print', file)
        text = open(f'./media/{file}', 'rb').read()
        print(text)
        context = {
            'text': text
        }

    return render(request, 'project/readfile.html', context)


def teacher_all_assignments(request):

    assignments = Assignment.objects.filter(
        assignment_creator=Teacher.objects.get(teacher_username=request.user)).order_by('-assignment_date')
    print(assignments)

    # teacher_instance = Teacher.objects.get(
    #     teacher_username=request.session[''])
    # assignments = Assignment.objects.create(assignment_creator=teacher_instance,
    #                                         )
    print(assignment)
    return render(request, 'project/teacher_all_assignments.html', {
        'assignments': assignments
    })


def create_assignment(request):

    if request.method == "POST":
        task = request.POST.get('task')
        task_title = request.POST.get('task_title')
        print(request.user)
        teacher_instance = Teacher.objects.get(
            teacher_username=request.user)
        print(teacher_instance)
        task = Assignment.objects.create(assignment_creator=teacher_instance,
                                         assignment_title=task_title,
                                         assignment_details=task)
        print(task, task_title)
        # task.save()
        print('task created')
    return render(request, 'project/create_assignment.html', )
