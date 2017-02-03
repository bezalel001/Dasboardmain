from django.forms import ModelForm
from cpdashboard.models import Initiative, Comment, Objective
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit




class UploadFileForm(forms.Form):
    file = forms.FileField()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('submit', 'Upload'))
        self.helper.layout.append(Submit('cancel', 'Cancel'))

class DateInput(forms.DateInput):
    input_type = 'date'



class InitiativeEditForm(ModelForm):
  
    class Meta:
        model = Initiative
        fields = ['actual_start_date', 'projected_end_date','actual_end_date', 'projected_end_cost','projected_manhours', 'actual_cost', 'actual_manhours','is_under_pressure']
        widgets = {
            'actual_start_date': DateInput(),
            'projected_end_date': DateInput(),
            'actual_end_date': DateInput(),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('submit', 'Update'))
        self.helper.layout.append(Submit('cancel', 'Cancel'))


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('submit', 'Post'))
        self.helper.layout.append(Submit('cancel', 'Cancel'))

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)



class ObjectiveEditForm(ModelForm):
  
    class Meta:
        model = Objective
        fields = ['description', 'objective_commentary', 'result', 'perspective']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('submit', 'Update'))
        self.helper.layout.append(Submit('cancel', 'Cancel'))