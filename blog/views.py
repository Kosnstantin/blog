from datetime import datetime
from django.shortcuts import get_object_or_404, render, redirect
from blog.models import Post
from blog.forms import PostForm


# def post_list(request):
#     if Post.objects.all().filter(published=True):
#         posts = Post.objects.all().filter(published=True)
#         context = {"items": posts}
#         response = render(request, "blog/post_list.html", context)
#     elif Post.objects.all().filter(published=False):
#         posts = Post.objects.all().filter(published=False)
#         context = {"items": posts}
#         response = render(request, "blog/post_list.html", context)
#     return response


def post_list(request):
    posts = Post.objects.all().filter(published=True)
    context = {"items": posts}
    return render(request, "blog/post_list.html", context)


def post_draft(request):
    posts = Post.objects.all().filter(published=False)
    context = {"items": posts}
    return render(request, "blog/post_draft.html", context)


def post_detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    context = {"post": post}
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
            # return redirect("post_detail", post_pk=post.pk)
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
