from django.db import models
from django.conf import settings

# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    content = models.TextField()
    movie = models.CharField(max_length=80)
    
    def __str__(self):
        return f'제목:{self.title}; 영화제목:{self.movie}'
