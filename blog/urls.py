from django.contrib import admin
from django.urls import path
from blog.views import (
    post_list,
    post_detail,
    post_new,
    post_edit,
    post_delete,
    post_draft,
    published_post,
    categories,
    comment_delete,
    feedback,
)

urlpatterns = [
    path("", post_list, name="post_list"),
    path("post_draft", post_draft, name="post_draft"),
    path("post/detail/<int:post_pk>", post_detail, name="post_detail"),
    path("post/category/<int:category_pk>", categories, name="categories"),
    path("post/published/<int:post_pk>", published_post, name="published_post"),
    path("post/edit/<int:post_pk>", post_edit, name="post_edit"),
    path("post/delete/<int:post_pk>", post_delete, name="post_delete"),
    path(
        "post/delete/<int:post_pk>/<int:comment_pk>",
        comment_delete,
        name="comment_delete",
    ),
    path("post/new", post_new, name="post_new"),
    path("post/detail/feedback/<int:post_pk>", feedback, name="feedback"),
]
