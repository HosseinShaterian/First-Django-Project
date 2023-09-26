from django import forms
from .models import CustomerRequest, SERVICE_CHOICES


class CustomerRequestCreateForm(forms.Form):
    name = forms.CharField(max_length=100, label='نام:')
    address = forms.CharField(max_length=500,label='آدرس:')
    phone = forms.CharField(max_length=20)
    # type_of_service = forms.IntegerField()
    type_of_service = forms.ChoiceField(choices=SERVICE_CHOICES, widget=forms.Select())
    device_name = forms.CharField(max_length=100)
    # request_date = forms.DateTimeField()
    # اعمال ویجت DateInput برای فیلد request_date
    # request_date = forms.DateTimeField(widget=forms.DateInput(attrs={'type': 'date'}))
    request_date = forms.DateTimeField(
    widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
    input_formats=['%Y-%m-%dT%H:%M'],
)
    is_done = forms.BooleanField(label='انجام شده', required=False)

class CustomerRequestUpdateForm(forms.ModelForm):
     # تعیین فیلد type_of_service به عنوان یک فیلد ChoiceField با گزینه‌های SERVICE_CHOICES
    type_of_service = forms.ChoiceField(choices=SERVICE_CHOICES, widget=forms.Select())
    # اعمال ویجت DateInput برای فیلد request_date
    # request_date = forms.DateTimeField(widget=forms.DateInput(attrs={'type': 'date'}))
    request_date = forms.DateTimeField(
    widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
    input_formats=['%Y-%m-%dT%H:%M'],
)

    class Meta:
        model = CustomerRequest
        fields = '__all__'
