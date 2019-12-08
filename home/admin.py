from django.contrib import admin
from .models import Announce, Tag, Comment, Profile


# Добавляем модели на страницу админа
admin.site.register(Announce)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Profile)
