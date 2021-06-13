from django import forms
from django.forms import ModelForm, DateInput
from .models import AddStudent, FeeReceipt


class AddStudent_form(ModelForm):
    class Meta:
        model = AddStudent
        fields = '__all__'
        # widgets = {
        # 'StuRegDate':DateInput(format='%Y/%m/%d',attrs={'type':'date'}),
        # 'StuDateOfBirth':DateInput(format='%Y/%m/%d',attrs={'type':'date'}),
        # }


class CollectFeeForm(ModelForm):
    class Meta:
        model = FeeReceipt
        fields = '__all__'
