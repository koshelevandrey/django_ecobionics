from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Теги объявлений
class Tag(models.Model):
    tag_ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ["name"]

    # Получение URL для отдельного тега
    def get_absolute_url(self):
        return reverse('tag-detail', args=[str(self.tag_ID)])

    def __str__(self):
        return self.name


# Возвращает путь, в который нужно сохранить файл пользователя
def user_directory_path(instance, filename):
    # Файл будет сохранён в MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)


def image_path(instance, filename):
    return 'images/{0}'.format(filename)


# Объявления
class Announce(models.Model):
    announce_ID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, unique=True)
    headline = models.TextField(null=True, blank=True)
    publication_date = models.DateTimeField(auto_now_add=True)
    preview_image = models.ImageField(upload_to='images', null=True, blank=True)
    # preview_image = models.ImageField(upload_to=user_directory_path)
    # Ссылка на превью-картинку
    # preview_image = models.CharField(max_length=300, null=True, blank=True)
    announce_tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    presentation = models.FileField(upload_to='files', null=True, blank=True)
    document = models.FileField(upload_to='files', null=True, blank=True)
    # presentation = models.CharField(max_length=300, null=True, blank=True)

    # Метаданные класса
    class Meta:
        # Способ сортировки: сначала идут самые свежие объявления
        ordering = ["-publication_date"]

    # Получение URL для отдельного объявления
    def get_absolute_url(self):
        return reverse('announce-detail', args=[str(self.announce_ID)])

    def __str__(self):
        return self.title


# Профили пользователей
class Profile(models.Model):
    profile_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    registration_date = models.DateField(auto_now_add=True)
    # События, на которые пользователь хочет пойти
    want_to_go_announces = models.ManyToManyField(Announce, blank=True, verbose_name="Хочу пойти")


# Функция для создания/обновления профиля пользователя при создании/обновлении пользователя
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


# Комментарии
class Comment(models.Model):
    comment_ID = models.AutoField(primary_key=True)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    announce = models.ForeignKey(Announce, on_delete=models.CASCADE)

    class Meta:
        # Задаём порядок сортировки комментариев по датам
        ordering = ["date"]

    # Получение URL для отдельного комментария
    def get_absolute_url(self):
        return reverse('comment-detail', args=[str(self.comment_ID)])

    def __str__(self):
        return self.content
