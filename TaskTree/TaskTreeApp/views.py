from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *
from django.shortcuts import render
from django.db.models import Avg, Sum, Max
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
    count_link_tasks = 0
    count_unlink_tasks = 0
    # print(type(vtask_id),vtask_id,task_id)
    # info_task = {}
    # if vtask_id==task_id:
    if find_task:
        lst_field_task = find_task.values()[0]
        vtask_title = lst_field_task['title']
        vtask_start = lst_field_task['start']
        vtask_end = lst_field_task['end']
        vtask_id = str(lst_field_task['id'])
        link_task = Univers_list.objects.filter(id_out=vtask_id)
        count_fulllink_task = link_task.count()
        FindTitleUnLink = ''
        FindTitle = ''
        if request.method == 'POST':
            btn_find_link = request.POST.get('btn_find_link')

            if btn_find_link:
                if request.POST.get('btn_find_link')=='+':
                    FindTitle = request.POST.get('FindTitle')
            btn_find_unlink = request.POST.get('btn_find_unlink')

            if btn_find_unlink:
                if request.POST.get('btn_find_unlink')=='+':
                    FindTitleUnLink = request.POST.get('FindTitleUnlink')

        if count_fulllink_task>0:
            list_link_task = Univers_list.objects.filter(id_out=vtask_id)
            lst_link_idin = list_link_task.values()[0]['id_in']
            # print(lst_link_idin)
            flist_link_task = Tasks.objects.filter(title__icontains=FindTitle, id=lst_link_idin)
            # print(flist_link_task)
            notlist_link_task = Tasks.objects.exclude(id=lst_link_idin).exclude(id=vtask_id).filter(title__icontains=FindTitleUnLink)
            count_link_tasks = flist_link_task.count()
        else:
            flist_link_task = None
            notlist_link_task = Tasks.objects.exclude(id=vtask_id).filter(title__icontains=FindTitleUnLink)
        count_unlink_tasks = notlist_link_task.count()
        if request.method == 'POST':
            btn_unlink = request.POST.get('btn_unlink')
            if btn_unlink:
                Univers_list.objects.filter(id_in=btn_unlink,id_out=vtask_id).delete()
            btn_link = request.POST.get('btn_link')
            if btn_link:
                # print(btn_link,vtask_id)
                if Univers_list.objects.filter(id_in=btn_link, id_out=vtask_id, role='arrow'):
                    return HttpResponse("Задачи уже связаны")
                else:
                    max_indx = Univers_list.objects.filter(id_out=vtask_id, role='arrow').aggregate(Max('num_in_link'))
                    max_indx_int = max_indx['num_in_link__max']
                    if not max_indx_int:
                        max_indx_int = 0
                    max_indx_int += 1
                    # print(max_indx)
                    Univers_list.objects.create(id_in=btn_link, id_out=vtask_id, num_in_link=max_indx_int, role='arrow')
    else:
        return HttpResponse("Задача не найдена")
    info_task = {'task_id': vtask_id, 'task_title': vtask_title, 'task_start':vtask_start,
                'task_end': vtask_end,'list_link_task': flist_link_task,
                 'notlist_link_task': notlist_link_task,
                 'count_link_tasks': count_link_tasks,'count_unlink_tasks': count_unlink_tasks}
    return render(request,'card_task.html',context=info_task)
