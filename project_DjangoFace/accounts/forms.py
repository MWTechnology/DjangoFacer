
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django import forms

from account.forms import PasswordResetForm
from account.models import EmailAddress





class MyForm(UserCreationForm):
    is_active = True
    error_messages = {
        'password_mismatch': _('Два поля пароля не совпадают.'),
    }

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = ('username', 'email', 'number', 'password1', 'password2')




class MyAuthForm(AuthenticationForm):
    error_messages = {
        'inactive': ("This account is inactive." ),
        'invalid_login': _("Ваш логин не  активен, обратитесь к администратору для подтверждения личности!"),

    }


class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=_("Email"), required=True)

    def clean_email(self):
        value = self.cleaned_data["email"]
        if not EmailAddress.objects.filter(email__iexact=value).exists():
            raise forms.ValidationError(_("Данный адрес не зарегистрирован на сайте!"))
        return value


class MySetPasswordForm(SetPasswordForm):
    error_messages = {
        'password_mismatch': _('Пароли не совпадают.'),
    }

class MyPasswordChangeForm(PasswordChangeForm):
    error_messages = {
        **MySetPasswordForm.error_messages,
        'password_incorrect': _("Your old password was entered incorrectly. Please enter it again."),
    }


    def __init__(self, *args, **kwargs):

        super(MyPasswordChangeForm, self).__init__(*args, **kwargs)

        for fieldname in ['old_password', 'new_password1', 'new_password2']:
            self.fields[fieldname].help_text = None
