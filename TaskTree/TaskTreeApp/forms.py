"""
 Модуль forms.py
 class CreateContact - форма для создания нового контакта
    last_name -фамилия (обязательное поле)
    first_name - имя
    second_name - отчество
class CreateTask - форма для создания новой задачи
    title -  текст заголовка задачи (обязательное поле)
    start - дата старта задачи
    end - дата завершения задачи
"""
from django import forms


class CreateContact(forms.Form):
    """
    class CreateContact - форма для создания нового контакта
        last_name -фамилия (обязательное поле)
        first_name - имя
        second_name - отчество
    """
    last_name = forms.CharField(max_length=75, label='Введите фамилию')
    first_name = forms.CharField(max_length=75,label='Введите имя')
    second_name = forms.CharField(max_length=75, label='Введите отяество')
    # def __init__(self,initials):
    #     super().__init__()
    #     print(initials)
    #     self.initials = initials
    #     try:
    #         if initials:
    #             for fld in self.fields:
    #                 fld.initial = initials[fld.name]
    #     except:
    #         pass
class CreateTask(forms.Form):
    """
    class CreateTask - форма для создания новой задачи
        title -  текст заголовка задачи (обязательное поле)
        start - дата старта задачи
        end - дата завершения задачи
    """
    widg = forms.DateInput(format='%d.%m.%Y', attrs={'type': 'date'})
    inform = ['%Y-%m-%d']
    title = forms.CharField(max_length=250, label='Введите текст задачи')
    start = forms.DateField(label='Введите дату старта', required=False, widget=widg, input_formats = inform)
    end = forms.DateField(label='Введите дату завершения',  required=False, widget=widg, input_formats = inform)