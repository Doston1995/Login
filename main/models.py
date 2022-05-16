from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length = 255, blank = True, null = True)


class Blog(models.Model):
    title = models.CharField(max_length = 255, blank = True, null = True)
    description = models.TextField()
    slug = models.CharField(max_length = 255, blank = True, null = True)
    image = models.ImageField(upload_to = 'blogImages/')
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add = True)
