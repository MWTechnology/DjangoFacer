from django import forms
from searchface.models import Mysearchface

class MysearchfaceForm(forms.ModelForm):
    class Meta:
        model = Mysearchface
        fields = ('image', 'name')
