from django.contrib import admin
from blog.models import Post, Comments, Category, Feedback

# Register your models here.

admin.site.register(Post)
admin.site.register(Comments)
admin.site.register(Category)
admin.site.register(Feedback)
