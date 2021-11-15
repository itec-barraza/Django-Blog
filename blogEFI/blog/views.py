from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Post, Categoria
from .forms import AddPost
from django.contrib.auth.models import User


def blog(request):
    posts = Post.objects.all()
    return render(
        request,
        "blog/blog.html",
        {'posts': posts}
    )


def category(request, category_id):
    category = Categoria.objects.get(id=category_id)
    posts = Post.objects.filter(category=category)
    return render(
        request,
        "blog/category.html",
        {'posts': posts,
         'category': category}
    )


def user(request, user_id):
    user = User.objects.get(id=user_id)
    posts = Post.objects.filter(author_id=user)
    return render(
        request,
        "blog/user.html",
        {'posts': posts,
         'user': user}
    )


def addPost(request):
    if request.method == "POST":
        form = AddPost(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print(form)
            instance = form.save(commit=False)
            instance.save()
            return redirect('/blog/')
    form = AddPost()
    posts = Post.objects.all()
    # users = User.objects.all()
    # categories = Categoria.objects.all()
    # return render(
    #     request,
    #     "blog/post.html",
    #     {'categories': categories,
    #      'users': users}
    # )
    return render(
        request,
        "blog/post.html",
        {'form': form})

# Create your views here.
