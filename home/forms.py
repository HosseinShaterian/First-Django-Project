from django import forms
from .models import CustomerRequest


class CustomerRequestCreateForm(forms.Form):
    name = forms.CharField(max_length=100, required=False, label='نام:')
    address = forms.CharField(max_length=500,label='آدرس:')
    phone = forms.CharField(max_length=20)
    type_of_service = forms.IntegerField()
    device_name = forms.CharField(max_length=100)
    request_date = forms.DateTimeField()
    is_done = forms.BooleanField(label='انجام شده')

class CustomerRequestUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomerRequest
        fields = '__all__'
