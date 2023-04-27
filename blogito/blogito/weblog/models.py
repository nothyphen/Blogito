from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    image = models.ImageField(default=False, upload_to="static/images")
    title = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=80, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='blog_posts')
    updated = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

class Comment (models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80, blank=True, null=True)
    email = models.EmailField()
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['date']
    def __str__(self):
        return self.text
    
class About(models.Model):
    text = models.TextField()

class Contact(models.Model):
    text = models.TextField(max_length=50)
    twitter = models.CharField(max_length=50)
    instagram = models.CharField(max_length=50)
    linkdin = models.CharField(max_length=50)

class ContactUs(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    massage = models.TextField()
