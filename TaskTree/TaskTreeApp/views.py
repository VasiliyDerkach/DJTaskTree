from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *
from django.shortcuts import render
def VCreateTask(request):
    if request.method == 'POST':
        form = CreateTask(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            task_start = form.cleaned_data['start']
            task_end = form.cleaned_data['end']
            Tasks.objects.create(title=title, start=task_start, end=task_end)
    else:
        form = CreateTask()
    cont_form={'form': form}
    return render(request, 'create_contact.html',context=cont_form)
# Create your views here.
def VCreateContact(request):
    if request.method == 'POST':
        form = CreateContact(request.POST)
        if form.is_valid():
            last_name = form.cleaned_data['last_name']
            first_name = form.cleaned_data['first_name']
            second_name = form.cleaned_data['second_name']
            Contacts.objects.create(last_name=last_name,first_name=first_name,second_name=second_name)
    else:
        form = CreateContact()
    cont_form={'form': form}
    return render(request, 'create_contact.html',context=cont_form)
def MainPage(request):
    FindTitle = ''
    if request.method == 'POST':
        if request.POST.get('btn_find')=='new_find':
            FindTitle = request.POST.get('FindTitle')

    tasks_lst = Tasks.objects.filter(title__icontains=FindTitle)
    count_tasks = tasks_lst.count()
    if count_tasks == 0:
        PageStr = 'Нет задач соответствующих условиям'
    elif count_tasks > 0:
        PageStr = f'Количество задач = {count_tasks}'
    info_main = {'PageTitle': PageStr, 'tasks_list': tasks_lst,
                 'count_tasks': count_tasks, 'FindTitle': FindTitle}
    return render(request, 'main.html', context=info_main)

def VCardTask(request, task_id):
    find_task = Tasks.objects.filter(id=task_id)
    vtask_id = find_task.values()['id']
    info_task = {}
    if vtask_id==task_id:
        link_task = Univers_list.object.filter(id_out=vtask_id)
        count_link_task = link_task.count()
        list_link_task = Tasks.object.filter(id_in=link_task)
        notlist_link_task = Tasks.object.filter(id_in!=[link_task,vtask_id])
    else:
        return HttpResponse("Задача не найдена")
    info_task = {'task_id': vtask_id, 'find_task':find_task,'count_link_task':count_link_task,
                 'list_link_task':list_link_task, 'notlist_link_task':notlist_link_task}
    return render(request,'card_task.html',context=info_task)
