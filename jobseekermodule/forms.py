from django import forms
from .models import *
class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['name', 'email', 'resume', 'cover_letter']

    def __init__(self, *args, **kwargs):
        super(JobApplicationForm, self).__init__(*args,**kwargs)



