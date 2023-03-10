from django.forms import ModelForm, TextInput, DateTimeInput, Textarea
from .models import News

class NewsForm(ModelForm):
    model = News
    fields = ['title', 'full_text', 'date']

    widgets = {
            'title': TextInput(attrs={
                'class': "form-control",
                "placeholder":"Название статьи"
            }),
            'date': DateTimeInput(attrs={
                'class': "form-control",
                "placeholder":"Дата публикации"
            }),
             'full_text': Textarea(attrs={
                'class': "form-control",
                "placeholder":"Текст  статьи"
            })
        }