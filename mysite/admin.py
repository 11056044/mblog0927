from django.contrib import admin
from mysite.models import Post,Product,Comment #匯入資料
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display=('title','slug','pub_date')#管理時可看到

class CommentAdmin(admin.ModelAdmin):
    list_display=('text','pub_date')

admin.site.register(Post,PostAdmin) #註冊
admin.site.register(Product)
admin.site.register(Comment,CommentAdmin)

