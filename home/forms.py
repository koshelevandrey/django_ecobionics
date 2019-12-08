from django.contrib.auth.models import User
from django import forms
from home.models import Profile, Tag, Comment
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


# Форма добавления комментария
class AddCommentForm(forms.Form):
    # Поле формы
    comment_content = forms.CharField(widget=forms.Textarea, required=True)

    # Проверка правильности введённых данных
    def clean_renewal_date(self):
        data = self.cleaned_data['comment_content']
        return data


# Форма для введения данных пользователя
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


# Форма для введения данных профиля пользователя
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('want_to_go_announces',)


# Формы для регистрации
class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'email')


# Форма изменения данных пользователя
class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = User
        fields = ('username', 'email')
