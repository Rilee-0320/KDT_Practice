from django.contrib import admin
from .models import Article

# Register your models here.
# admin site에 등록(register)하겠다는 의미
admin.site.register(Article)