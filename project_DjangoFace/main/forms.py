from django import forms
from main.models import Suspect

class SuspectForm(forms.ModelForm):
    default_error_messages = {
        'invalid': ('Введите правильную дату: дд.мм.гггг '),
    }

    class Meta:
        model = Suspect
        fields = ('surname', 'name', 'patronymic', 'passport', 'date_of_birth', 'crimes', 'image')
