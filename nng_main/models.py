from django.db import models

# Create your models here.
class Post(models.Model):
    #post author
    author = models.CharField(max_length = 200, default='The Ultimate Leader')
    title = models.CharField(max_length = 400, default = 'NNG Social')
    date = models.DateTimeField(auto_now=True, auto_now_add=False)
    body = models.TextField(max_length = 4000, default = '')

    def __str__(self):
        return self.title

class Comment(models.Model):
    #Comment AUthor
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length = 300, default='')
    #Comment Body
    body = models.CharField(max_length = 400, default='')
    # post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='posts',)

    def __str__(self):
        return self.author