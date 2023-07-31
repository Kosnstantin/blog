from blog.models import Post
from django.forms import ModelForm, TextInput, Textarea


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "text"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter task name'
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter task'
            })
        }
