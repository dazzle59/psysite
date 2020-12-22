from django import forms
from django.forms import Textarea
from django.utils.translation import gettext_lazy as _
from main.models import Article
from main.models import Contact


class BootstapForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class' : 'form-control'})

class SearchForm(BootstapForm):
    search = forms.CharField(label='поиск', max_length=1000, empty_value='поиск')

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = "__all__"

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')#'__all__'
        widgets = {
            'name': forms.TextInput(attrs={'size':'40', 'class': 'form-control', 'placeholder': '---'}),
            'email': forms.TextInput(attrs={'size':'40', 'class': 'form-control', 'placeholder': '8 900 00 000 00'}),
            'message': forms.Textarea(attrs={'style': 'height: 10em', 'class': 'form-control', 'placeholder': '---'})
        }
        labels = {
            'name': _('Тема'),
            'email': _('e-mail или номер телефона'),
            'message': _('Текст сообщения')
        }
        error_messages = {
            'name': {
                'max_length': _("Очень длинное название темы"),
            },
            'email':{'error_message' : _("Введите почту или номер телефона")}
        }
        field_classes = {
            'name': forms.CharField,
            'email': forms.CharField,
            'message': forms.CharField,
        }

