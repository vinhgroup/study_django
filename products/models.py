from django.db import models

class Person(models.Model):
    itle = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    #print("data")
    def store(itle, slug, content):
        return Person()