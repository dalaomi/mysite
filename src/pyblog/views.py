from django.shortcuts import render_to_response
from pyblog.models import Post
# Create your views here.

def index(request):
    # 已发布文章倒序展示
    posts = Post.objects.filter(published_date__isnull=False).order_by('-published_date')
    # 热门文章倒序展示
    pretty_posts = Post.objects.filter(published_date__isnull=False).order_by('comment_num') 
    return render_to_response('index.html',{'posts':posts,'pretty_posts':pretty_posts})

def post_list(request):
    posts = Post.objects.filter(published_date__isnull=False).order_by('-published_date')
    return render_to_response('post_list.html',{'posts':posts})
#     return render(request,'pyblog/post_list.html',{})

def post_detail(request,pk):
    print('文章ID为：'+pk);
    post = Post.objects.get(id=pk)
    print(post)
    return render_to_response('post_detail.html',{'post':post}) 

def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('-create_date')
    return render_to_response('post_draft_list.html', {'posts':posts})

