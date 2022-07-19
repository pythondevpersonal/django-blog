from audioop import reverse
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Core(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(null=True)
    author = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='core')
    slug = models.SlugField(unique=True,max_length=20,null=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(default=datetime.now)
    
    def get_absolute_url(self):
        return reverse('core:single',args=[self.slug])
    
    class Meta:
        ordering = ['published']
    
    def __str__(self) :
        return self.title