from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Post
def index(request):
    posts = Post.objects.all().order_by('-created_at')
    context = {'posts': posts}
    return render(request, 'myapp/index.html', context)
def create_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        author = request.user
        post = Post(title=title, content=content, author=author)
        post.save()
        return redirect('index')
    else:
        return render(request, 'myapp/create_post.html')