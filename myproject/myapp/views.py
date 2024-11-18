# Create your views here.
from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect

# View trang chủ
def index(request):
    posts = Post.objects.all().order_by('-created_at')
    context = {'posts': posts}
    return render(request, 'myapp/index.html', context)

# View tạo bài viết
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

# View đăng ký
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Chào mừng {user.username}, tài khoản của bạn đã được tạo!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'myapp/register.html', {'form': form})

# View đăng xuất
def custom_logout(request):
    logout(request)
    return redirect('index')
