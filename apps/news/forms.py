from django import forms

from apps.forms import FormMixin


class CommentForm(forms.Form, FormMixin):
    content = forms.CharField()
    news_id = forms.IntegerField()








