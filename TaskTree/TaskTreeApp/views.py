from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *
from django.shortcuts import render
def CreateTask(request):
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
    return render(request, 'create_task.html',context=cont_form)
# Create your views here.
