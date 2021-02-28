from django.forms import ModelForm
from .models import powerloom


class AddNewForm(ModelForm):
    class Meta:
        model = powerloom
        fields = '__all__'
