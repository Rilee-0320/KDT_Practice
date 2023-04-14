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


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review = models.ForeignKey(to='reviews.Review', on_delete=models.CASCADE)
    content = models.TextField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'"{self.content}" by {self.user}'