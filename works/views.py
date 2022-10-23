from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.http import HttpResponseRedirect, HttpResponse
from .models import Task, Work
from .forms import WorkForm, WorkFormAdmin, TaskForm
from django.contrib import messages



def home(request):
	return redirect('all-tasks')


def all_tasks(request):
    tasks_list = Task.objects.all()
    return render(request, 'works/tasks_list.html', {'tasks_list': tasks_list, 'empty': str(len(tasks_list))})


def add_work(request, task_id):
	task = Task.objects.filter(pk=task_id)[0]
	submitted = False
	if request.method == "POST":
		form = WorkForm(request.POST, request.FILES)
		print(form, request.POST)
		if form.is_valid():
			work = form.save(commit=False)
			work.owner = request.user.id
			work.task = task
			work.save()
			return HttpResponseRedirect(f'/add_work/{task_id}?submitted=True')
	else:
		form = WorkForm
		if 'submitted' in request.GET:
			submitted = True
	return render(request, 'works/add_work.html', {'form': form, 'submitted': submitted, 'task': task})


def add_task(request):
	submitted = False
	if request.method == "POST":
		print("POST")
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/add_task?submitted=True')
	else:
		print("POST")
		form = TaskForm
		print(form)
		if 'submitted' in request.GET:
			submitted = True
	return render(request, 'works/add_task.html', {'form': form, 'submitted': submitted})


def show_works(request):
	works = []
	if request.user.is_superuser:
		works = Work.objects.all()		
	else:
		works = Work.objects.filter(owner=request.user.id)
	return render(request, 'works/show_works.html', {'works': works})


def update_work(request, work_id):
	work = Work.objects.get(pk=work_id)
	if request.user.is_superuser:
		form = WorkFormAdmin(request.POST or None, request.FILES or None, instance=work)
		form.fields['description'].widget.attrs['readonly'] = True
		form.fields['work_image'].widget.attrs['readonly'] = True
	else:
		form = WorkForm(request.POST or None, request.FILES or None, instance=work)
	
	if form.is_valid():
		form.save()
		return redirect('show-works')

	return render(request, 'works/update_work.html', 
		{'work': work,
		'form':form})


def update_task(request, task_id):
	task = Task.objects.get(pk=task_id)
	form = TaskForm(request.POST or None, request.FILES or None, instance=task)
	print("there")
	if form.is_valid():
		form.save()
		return redirect('all-tasks')

	return render(request, 'works/update_task.html', 
		{'task': task,
		'form':form})



def delete_work(request, work_id):
	work = Work.objects.get(pk=work_id)
	if request.user.id == work.owner:
		work.delete()
		messages.success(request, ("Работа удалена"))
		return redirect('show-works')		
	else:
		messages.success(request, ("Вы не имеете прав для удаления данной работы"))
		return redirect('show-works')		



def delete_task(request, task_id):
	task = Task.objects.get(pk=task_id)
	if request.user.is_superuser:
		task.delete()
		messages.success(request, ("Задание удалено"))
		return redirect('all-tasks')		
	else:
		messages.success(request, ("Вы не имеете прав для удаления данного задания"))
		return redirect('all-tasks')	
