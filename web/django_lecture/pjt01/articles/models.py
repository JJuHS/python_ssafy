from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        # 우리 눈에 보이는 게시글은 pk 와 title 로 구성
        return f'[{self.pk} {self.title}]'
    