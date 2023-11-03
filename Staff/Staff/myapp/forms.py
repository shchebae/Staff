from .models import Task
from django.forms import ModelForm, TextInput, EmailInput, Select

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["name", "num_staff", "mail", "phone_number", "job"]
        widgets ={
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Александров Александр Аслекс'
            }),
            "num_staff": TextInput(attrs={
                'class': 'form-control',
                'placeholder': '00002'
            }),
            "mail": EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'alex@gmail.com'
            }),
            "phone_number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': '89054325517'
            }),
            'job': Select(attrs={
                'class': 'form-control',
                'placeholder': 'Выберете из списка'
            })
        }