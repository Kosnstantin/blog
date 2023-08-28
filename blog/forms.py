from blog.models import Post, Comments
from django.forms import ModelForm, TextInput, Textarea, Select


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["category", "title", "text"]
        widgets = {
            "category": Select(attrs={"class": "form-control"}),
            "title": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter task name"}
            ),
            "task": Textarea(
                attrs={"class": "form-control", "placeholder": "Enter task"}
            ),
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ["text"]
        widgets = {
            "text": Textarea(
                attrs={"class": "form-control", "placeholder": "Enter comment"}
            ),
        }
