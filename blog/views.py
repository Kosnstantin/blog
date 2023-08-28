from datetime import datetime
from django.shortcuts import get_object_or_404, render, redirect
from blog.models import Post, Comments, Category
from blog.forms import PostForm, CommentForm


def post_list(request):
    posts = Post.objects.all().filter(published=True)
    category = Category.objects.all()
    counter = posts.count()
    context = {"items": posts, "category": category, "counter": counter}
    return render(request, "blog/post_list.html", context)


def categories(request, category_pk):
    posts = Post.objects.filter(category=category_pk)
    category = Category.objects.all()
    counter = posts.count()
    context = {"items": posts, "category": category, "counter": counter}
    return render(request, "blog/post_list.html", context)


def post_draft(request):
    posts = Post.objects.all().filter(published=False)
    counter = posts.count()
    context = {"items": posts, "counter": counter}
    return render(request, "blog/post_draft.html", context)


def published_post(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.published = True
    post.save()
    context = {"post": post}
    return render(request, "blog/post_detail.html", context)


def post_detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    comments = Comments.objects.filter(post=post_pk)
    counter = comments.count()
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.published_date = datetime.now()
            comment.save()
            return redirect("post_detail", post_pk=post.pk)
    else:
        comment_form = CommentForm()
    context = {
        "post": post,
        "comments": comments,
        "counter": counter,
        "comment_form": comment_form,
    }
    return render(request, "blog/post_detail.html", context)


def post_new(request):
    error = ""
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_date = datetime.now()
            post.publish_date = datetime.now()
            post.save()
            return redirect("post_list")
    else:
        error = "Iнший метод запиту"
        form = PostForm()

    context = {"form": form, "error": error}

    return render(request, "blog/post_new.html", context)


def post_edit(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == "GET":
        form = PostForm(instance=post)
        context = {"form": form}
        return render(request, "blog/post_edit.html", context)
    else:
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_date = datetime.now()
            post.publish_date = datetime.now()
            post.save()
            # return redirect("post_detail", post_pk=post.pk)
            return redirect("post_list")


def post_delete(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk).delete()
    return redirect("post_list")


def comment_delete(request, comment_pk, post_pk):
    post = Post.objects.get(pk=post_pk)
    comment = get_object_or_404(Comments, pk=comment_pk).delete()
    return redirect("post_detail", post_pk=post.pk)
