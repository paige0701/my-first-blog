from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone
from blog.forms import PostForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic import TemplateView


# Create your views here.

def beforelogin(request):

    return render(request, 'beforelogin.html')


def post_list(request):

    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    return render(request, 'blog/post_list.html', {'posts': posts})

def post_list_with_category(request, category):
    print(category)
    print("$$")
    p = Post()

    # category = p.get_category_name(category)

    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date').filter(category=category)
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list_category.html', {'posts': posts})



def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post} )


def post_new(request):

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)


    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form':form})


def post_edit(request,pk):

    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)

    else:
        form = PostForm(instance=post)

    return render(request,'blog/post_edit.html', {'form':form} )
