from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def about(request):
    return render(request, 'about.html')

def post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post.html', {'post': post})

def contact(request):
    return render(request, 'contact.html')   