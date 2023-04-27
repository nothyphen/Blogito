from django import forms
from .models import Comment, ContactUs

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'text')

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ('name', 'email', 'subject', 'massage')