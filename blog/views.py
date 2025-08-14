from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

def home(request):
    posts = Post.objects.all().order_by('-created_at')

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()             # saves the post to the database
            return redirect('home') # refreshes the page
    else:
        form = PostForm()

    context = {"title": "My First Django Page", "posts": posts, "form": form}
    return render(request, "blog/home.html", context)

def post_detail(request, pk):
    from django.shortcuts import get_object_or_404
    post = get_object_or_404(Post, pk=pk)
    context = {"post": post}
    return render(request, "blog/post_detail.html", context)
