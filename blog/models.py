from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Тут хранятся описания таблиц


class Post(models.Model):
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, blank=True, null=True
    )
    title = models.CharField(max_length=100, verbose_name="Title")
    text = models.TextField(verbose_name="Text")
    created_date = models.DateTimeField(auto_now_add=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"


class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(verbose_name="Text")
    publish_date = models.DateTimeField(auto_now_add=True, verbose_name="publish_date")
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.text}"


class Category(models.Model):
    text = models.CharField(max_length=100, verbose_name="Add category")

    def __str__(self):
        return f"{self.text}"


class Feedback(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(verbose_name="Text")
    publish_date = models.DateTimeField(auto_now_add=True, verbose_name="publish_date")
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    rating = models.IntegerField(
        verbose_name="Rating 1-5",
        default=3,
        validators=[MinValueValidator(0), MaxValueValidator(5)],
    )

    def __str__(self):
        return f"{self.text}"
