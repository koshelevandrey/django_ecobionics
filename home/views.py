from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.views import generic
from django.http import HttpResponseRedirect, Http404
from django.db.models import Count
from datetime import datetime, timedelta

from home.forms import UserForm, ProfileForm, CustomUserCreationForm
from home.models import Announce, Comment, Tag


# Информация о сайте
def info(request):
    # render() - отрисовка HTML-шаблона info.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'info.html',
    )


# Отображение списка объявлений
class AnnounceListView(generic.ListView):
    model = Announce
    # Имя переменной контекста в шаблоне
    context_object_name = 'announce_list'
    # Получаем все объявления
    queryset = Announce.objects.all()
    # Расположение шаблона и его имя
    template_name = 'templates/home/announce_list.html'
    # Количество объявлений в отображении (на одной странице)
    paginate_by = 10


# Поставить "хочу пойти" на объявление
@login_required(login_url='/home/login/')
def want_to_go(request, announce_pk):
    try:
        announce = Announce.objects.get(pk=announce_pk)
    except Announce.DoesNotExist:
        raise Http404("Announce does not exist")

    if request.user.profile.want_to_go_announces.filter(announce_ID=announce.announce_ID).exists():
        # Удаляем "хочу пойти"
        request.user.profile.want_to_go_announces.remove(announce)
    else:
        # Добавляем "хочу пойти"
        request.user.profile.want_to_go_announces.add(announce)

    request.user.profile.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# Добавить комментарий
@login_required(login_url='/home/login/')
def add_comment(request, announce_pk):
    try:
        announce = Announce.objects.get(pk=announce_pk)
    except Announce.DoesNotExist:
        raise Http404("Announce does not exist")
    if request.method == 'POST':
        comment_content = request.POST.get('comment_field_' + str(announce.announce_ID))
        Comment.objects.create(content=comment_content, user=request.user, announce=announce)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# Обновление профиля пользователя
@login_required(login_url='/home/login/')
# Указываем, что это транзакция. Если она не выполнится успешно, то будет откат
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('index')
        else:
            pass
            # messages.error(request, 'Please correct the error below.')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profiles/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


# Регистрация пользователя
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    # Адрес страницы, на который нужно совершить переход после успешного заполнения формы
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


# Объявления по тегу
class TagAnnounceListView(generic.ListView):
    model = Announce
    context_object_name = 'announce_list'
    # Расположение шаблона
    template_name = 'home/tag_announce_list.html'
    paginate_by = 10

    # Функция формирования контекста
    def get_context_data(self, **kwargs):
        context = super(TagAnnounceListView, self).get_context_data(**kwargs)
        try:
            tag = Tag.objects.get(tag_ID=self.kwargs['tag_pk'])
        except Tag.DoesNotExist:
            raise Http404("Tag does not exist")
        context['tag'] = tag

        return context

    def get_queryset(self):
        try:
            tag = Tag.objects.filter(tag_ID=self.kwargs['tag_pk'])
        except Tag.DoesNotExist:
            raise Http404("Tag does not exist")
        return Announce.objects.filter(announce_tags__in=tag)


# Страница с информацией о Ю. Т. Каганове
def kaganov(request):
    return render(
        request,
        'kaganov.html',
    )


# Страница с информацией о Д. М. Жуке
def zhuk(request):
    return render(
        request,
        'zhuk.html',
    )


# Страница с информацией о А. П. Карпенко
def karpenko(request):
    return render(
        request,
        'karpenko.html',
    )


# Страница с информацией о В. Г. Редько
def redko(request):
    return render(
        request,
        'redko.html',
    )


# Страница с информацией о А. С. Ющенко
def yushenko(request):
    return render(
        request,
        'yushenko.html',
    )


# Страница оргкомитета
def committee(request):
    return render(
        request,
        'committee.html',
    )


# Страница плана семинаров
def plan(request):
    return render(
        request,
        'plan.html',
    )


# Страница литературы
def literature(request):
    return render(
        request,
        'literature.html',
    )

