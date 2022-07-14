from django.views.generic import ListView, DetailView, CreateView
from .models import Course, Lesson
from django.shortcuts import render, redirect
from .forms import CourseForm
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


class HomePage(ListView):
    model = Course
    template_name = 'courses/home.html'
    context_object_name = 'courses'
    ordering = ['-id']

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(HomePage, self).get_context_data(**kwargs)
        ctx['title'] = 'Главная страница сайта'
        return ctx


class CourseDetailPage(DetailView):
    model = Course
    template_name = 'courses/course-detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(CourseDetailPage, self).get_context_data(**kwargs)
        course = Course.objects.filter(slug=self.kwargs['slug']).first()
        ctx['title'] = course
        ctx['lessons'] = Lesson.objects.filter(course=course).order_by('number')
        return ctx


class LessonDetailPage(DetailView):
    model = Course
    template_name = 'courses/lesson-detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(LessonDetailPage, self).get_context_data(**kwargs)
        course = Course.objects.filter(slug=self.kwargs['slug']).first()
        lesson = Lesson.objects.filter(slug=self.kwargs['lesson_slug']).first()

        lesson.video = lesson.video.split("=")[1]

        ctx['title'] = lesson
        ctx['lesson'] = lesson
        return ctx


# Первый способ создания нового курса
class CreateCourse(CreateView, SuccessMessageMixin):
    model = Course
    template_name = 'courses/add-course.html'
    fields = ['slug', 'title', 'desc', 'image']
    # вывод сообщения об успехе не удался. Не смог найти почему
    success_message = 'Курс  был успешно добавлен!'
    success_url = '/'


# Второй способ создания нового курса с выводом сообщения об успехе
def AddCourse(request):
    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            course = form.cleaned_data.get('title')
            messages.success(request, f'Курс {course} был успешно добавлен!')
            return redirect('home')
    else:
        form = CourseForm()

    data = {
            'title': 'Добавление курса',
            'form': form
        }

    return render(request, 'courses/add-course.html', data)
