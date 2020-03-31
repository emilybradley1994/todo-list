from django import forms
from todoapp.models import ListItem

class TodoForm(forms.ModelForm):

    item = forms.CharField(max_length=50)

    class Meta:

        model = ListItem
        fields = ('item',)
