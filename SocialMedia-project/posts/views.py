from django.shortcuts import render
from .forms import PostCreateForm
from django.contrib.auth.decorators import login_required
from .models import Post

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostCreateForm(data = request.POST,files= request.FILES)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            return render(request,'posts/post_save.html')

        else:
            print("This post is not save")

    else:
        form = PostCreateForm(data = request.GET)
    context ={
        'form':form
    }
    return render(request,'posts/create.html',context)

def feed(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request,'posts/feed.html',context)