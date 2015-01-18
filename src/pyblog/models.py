from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
 
# 文章
class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    text = models.TextField()
    status=models.IntegerField(default=0) #0:未发布，1：已发布，2：草稿箱，3：回收站
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)
    read_num = models.IntegerField(default=0)
    comment_num = models.IntegerField(default=0)
    category_id = models.IntegerField
    
    def publish(self):
        self.status = 1;
        self.published_date = timezone.now()
        self.save()
    
    def draft(self):
        self.status = 2
        self.save()
    
    def delete(self):
        self.status=3
        self.save()
        
    def __str__(self):
        return self.title

class Comment(models.Model):
    nick_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    site_url = models.CharField(max_length=50)
    comment = models.TextField()
    comment_date = models.DateTimeField(default=timezone.now)
    post_id = models.ForeignKey(Post)
    
class Category(models.Model):
    name = models.CharField(max_length=30)
    
    