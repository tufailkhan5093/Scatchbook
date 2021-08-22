from django import forms
from .models import Step3,message1, message2
from ckeditor.fields import RichTextField



class Update(forms.ModelForm):
    class Meta:
        model=Step3

        fields=['first','second','third']
        widgets={
            'first':RichTextField(),
            'second':forms.Textarea(attrs={'class':'form-control'}),
            'third':forms.Textarea(attrs={'class':'form-control'}),
            
        }

class Message1(forms.ModelForm):
    class Meta:
        model=message1

        fields=['msg']
        widgets={
            'msg':RichTextField(),   
        }

class Message2(forms.ModelForm):
    class Meta:
        model=message2

        fields=['msg']
        widgets={
            'msg':RichTextField(),   
        }