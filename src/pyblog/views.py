from django.shortcuts import render_to_response, get_object_or_404, redirect,render
from pyblog.models import Post
from pyblog.forms import PostForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    # 已发布文章倒序展示
    posts = Post.objects.filter(published_date__isnull=False).order_by('-published_date')
    # 热门文章倒序展示
    pretty_posts = Post.objects.filter(published_date__isnull=False).order_by('comment_num') 
    return render(request,'index.html',{'posts':posts,'pretty_posts':pretty_posts})

def draft(request):
    # 已发布文章倒序展示
    posts = Post.objects.filter(published_date__isnull=False).order_by('-create_date')
    # 热门文章倒序展示
    pretty_posts = Post.objects.filter(published_date__isnull=False).order_by('comment_num') 
    return render_to_response('index.html',{'posts':posts,'pretty_posts':pretty_posts})


def post_list(request):
    posts = Post.objects.filter(published_date__isnull=False).order_by('-published_date')
    return render_to_response('post_list.html',{'posts':posts})
#     return render(request,'pyblog/post_list.html',{})

def post_detail(request,pk):
    print('文章ID为：'+pk);
    # post = Post.objects.get(id=pk)
    post = Post.objects.get(id=pk)
    print(post)
    return render_to_response('post_detail.html',{'post':post}) 
@login_required
def post_new(request):
    if request.method =='POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            #post.author=1
            user = User.objects.get(id=1)
            post.author = user
            post.save()
            return redirect('pyblog.views.post_detail',pk=post.id)
    else :
        form = PostForm()
    return render_to_response('post_edit.html',{'form':form}) 
@login_required
def post_edit(request,pk):
    post = get_object_or_404(Post,id=pk)
    if request.method =='POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            user = User.objects.get(id=1)
            post.author = user
            post.save()
            return redirect('pyblog.views.post_detail',pk=post.id)
    else :
        form = PostForm(instance=post)
    return render_to_response('post_edit.html',{'form':form}) 
@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post,id=pk)
    post.publish()
    return redirect('pyblog.views.post_list')
@login_required
def post_remove(request,pk):
#     post = Post.objects.get(id=pk)
#     post.delete()
    Post.objects.filter(id=pk).delete()
    return redirect('pyblog.views.index')
@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('-create_date')
    return render_to_response('post_draft_list.html', {'posts':posts})

