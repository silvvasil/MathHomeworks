from django import forms
from django.forms import ModelForm
from .models import Work, Task

class WorkForm(ModelForm):
    class Meta:
        model = Work
        fields = ('description', 'work_image')
        labels = {
            'description': '',
            'work_image': '',         
        }
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Опишите свое решение здесь'}),
        }

class WorkFormAdmin(ModelForm):
    class Meta:
        model = Work
        fields = ('description', 'comment', 'work_image')
        labels = {
            'comment': '',
            'description': 'Описание работы',
            'work_image': 'Прикрепленные материалы',         
        }
        widgets = {
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Оцените решение и напишите свой комментарий к нем'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Опишите свое решение здесь'}),
        }   

              
class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = {'name', 'deadline', 'description'}
        labels = {
            'name': '',
            'deadline': 'Формат: ГГГГ-ММ-ДД ЧЧ:ММ:CC',
            'description': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Название работы'}),
            'deadline': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Дедлайн сдачи работы'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Описание работы'}),
        }
