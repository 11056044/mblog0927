from django.db import models

# Create your models here.
class Post(models.Model):  #繼承
    title=models.CharField(max_length=200)
    slug=models.CharField(max_length=200)#
    body=models.TextField()#內容
    pub_date=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering=('-pub_date',)  #資料排序，依照時間限後排序
    
    def __str__(self) -> str:
        return self.title

        
#創建資料庫的概念
#資料名稱和資料型態
