from blog.models import Post, Comments, Feedback
from django.forms import ModelForm, TextInput, Textarea, Select, NumberInput


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["category", "title", "text", "author"]
        widgets = {
            "category": Select(attrs={"class": "form-control"}),
            "title": TextInput(
                attrs={"class": "form-control", "placeholder": "Enter task name"}
            ),
            "task": Textarea(
                attrs={"class": "form-control", "placeholder": "Enter task"}
            ),
            "author": Select(attrs={"class": "form-control"}),
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ["text"]
        labels = {"text": ""}
        widgets = {
            "text": Textarea(
                attrs={"class": "form-control", "placeholder": "Enter comment"}
            ),
        }

class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ["text", "rating"]
        labels = {"text": ""}
        widgets = {
            "text": Textarea(
                attrs={"class": "form-control", "placeholder": "Enter review"}
            ),
            "rating": NumberInput(attrs={"class": "form-control", "min": 0, "max": 5}),
        }
