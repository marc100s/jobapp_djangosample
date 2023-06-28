from django import forms

from subscribe.models import Subscribe
from django.utils.translation import gettext_lazy as _

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe 
        fields = '__all__'
        # exclude = ('last_name',)
        labels={
            'first_name':_('Enter first name'),
            'last_name':_('Enter last name'),
            'email':_('Enter email')
        }
        # help_texts={'first_name':_('Enter characters only')}
        error_messages={
            'first_name': {
                'required' : _('You must enter your first name'),
                }, 
            'email': {
                'required' : _('You must enter your email address'),
            }
        }
        
        # fields = ['first_name', 'last_name', 'email']

# def validate_comma(value):
#   if "," in value:
#       raise forms.ValidationError("Invalid Last Name")
#   return value


    # first_name = forms.CharField(max_length=100, required=True, label="Enter Your First Name", help_text="Enter character only")
    # last_name = forms.CharField(max_length=100, disabled=False, label="Enter Your Last Name", validators=[validate_comma])
    # email = forms.EmailField(max_length=100, label="Enter Your Email")
    

    