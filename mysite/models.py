from django.db import models

# Create your models here.
class Post(models.Model):  #繼承
    title=models.CharField(max_length=200)
    slug=models.CharField(max_length=200)
    body=models.TextField()#內容
    pub_date=models.DateTimeField(auto_now_add=True)#自動取得現在時間
    
    class Meta:
        ordering=('-pub_date',)  #資料排序，依照時間限後排序
    
    def __str__(self) -> str:
        return self.title #印出標題就好


class Comment(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    text=models.CharField(max_length=200)
    pub_date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.text
 
class Product(models.Model):
    SIZES=(
        ('S','Small'),
        ('M','Medium'),
        ('L','Large'),
    )
    suk=models.CharField(max_length=5)
    name=models.CharField(max_length=20)
    price=models.PositiveIntegerField()
    size=models.CharField(max_length=1,choices=SIZES)#做成選單

#創建資料庫的概念
#資料名稱和資料型態
