from django import forms
from .models import Course


class CourseForm(forms.ModelForm):
    slug = forms.SlugField(
        label='Название URL',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите идентификатор курса'})
    )
    title = forms.CharField(
        label='Название курса',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название курса'})
    )
    desc = forms.CharField(
        label='Описание курса',
        required=True,
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите описание курса'})
    )
    image = forms.ImageField(
        label='Изображение курса',
        required=False,
        widget=forms.FileInput
    )

    class Meta:
        model = Course
        fields = ['slug', 'title', 'desc', 'image']
