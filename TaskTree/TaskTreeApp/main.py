from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *

def main(request):
    tasks_lst = Tasks.objects.query.join(join=)
