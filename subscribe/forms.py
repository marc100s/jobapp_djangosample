from django import forms

def validate_comma(value):
  if "," in value:
      raise forms.ValidationError("Invalid Last Name")
  return value

class SubscribeForm(forms.Form):
    first_name = forms.CharField(max_length=100, required=True, label="Enter Your First Name", help_text="Enter character only")
    last_name = forms.CharField(max_length=100, disabled=False, label="Enter Your Last Name", validators=[validate_comma])
    email = forms.EmailField(max_length=100, label="Enter Your Email")
    
    # def clean_first_name(self):
    #     data = self.cleaned_data['first_name']
    #     if "," in data:
    #         raise forms.ValidationError("Invalid First Name")
    #     return data
    
    