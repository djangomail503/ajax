from django import forms
from ajax_app import models
class MyUserForm(forms.ModelForm):

    class Meta():
        model = models.MyUser
        fields = '__all__'