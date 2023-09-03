from django import forms
from tinymce.widgets import TinyMCE

class ArticleForm(forms.Form):
    content = forms.CharField(widget=TinyMCE())
