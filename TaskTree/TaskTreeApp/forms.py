from django import forms
class CreateContact(forms.Form):
    last_name = forms.CharField(max_length=75)
    first_name = forms.CharField(max_length=75)
    second_name = forms.CharField(max_length=75)

class CreateTask(forms.Form):
    title = forms.CharField(max_length=250, label='Введите текст задачи')
    start = forms.DateTimeField(widget=forms.SplitDateTimeWidget())
    end = forms.DateTimeField(widget=forms.SplitDateTimeWidget())